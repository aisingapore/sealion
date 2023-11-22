import os
import math
from dataclasses import dataclass, field
from typing import Optional
import torch
from accelerate import Accelerator

from peft import (
    AutoPeftModelForCausalLM,
    LoraConfig,
    prepare_model_for_kbit_training,
)
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    AutoConfig,
)

from trl import SFTTrainer
from data_functions import *
from helper_functions import *
from omegaconf import OmegaConf


@dataclass
class ScriptArguments:
    config_path: Optional[str] = field(
        default="sft/sft_config.yaml", metadata={"help": "SFT parameters config file"}
    )


parser = HfArgumentParser(ScriptArguments)
conf = parser.parse_args_into_dataclasses()[0]
conf = OmegaConf.load(conf.config_path)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

# Grab config first
print(f"Loading HF Config...")
conf.attn_impl = "triton"
try:
    config = AutoConfig.from_pretrained(
        conf.name_or_path,
        trust_remote_code=True,
    )
    if conf.attn_impl is not None and hasattr(config, "attn_config"):
        config.attn_config["attn_impl"] = conf.attn_impl

except Exception as e:
    raise RuntimeError(
        "If you are having auth problems, try logging in via `huggingface-cli login` "
        + "or by setting the environment variable `export HUGGING_FACE_HUB_TOKEN=... "
        + "using your access token from https://huggingface.co/settings/tokens."
    ) from e


base_model = AutoModelForCausalLM.from_pretrained(
    conf.name_or_path,
    config=config,
    quantization_config=bnb_config,
    device_map={"": Accelerator().local_process_index},
    trust_remote_code=True,
)

peft_config = LoraConfig(
    r=conf.peft.lora_r,
    lora_alpha=conf.peft.lora_alpha,
    lora_dropout=conf.peft.lora_dropout,
    target_modules=OmegaConf.to_object(conf.peft.target_modules),
    bias="none",
    task_type="CAUSAL_LM",
)

# prepare model for training
base_model = prepare_model_for_kbit_training(base_model)

tokenizer = AutoTokenizer.from_pretrained(conf.name_or_path, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training

training_args = TrainingArguments(
    output_dir=conf.output_dir,
    per_device_train_batch_size=conf.per_device_train_batch_size,
    gradient_accumulation_steps=conf.gradient_accumulation_steps,
    per_device_eval_batch_size=conf.per_device_eval_batch_size,
    learning_rate=conf.learning_rate,
    logging_steps=conf.logging_steps,
    # max_steps=conf.max_steps,
    # num_train_epochs=conf.num_train_epochs,
    report_to=conf.log_with,
    save_steps=conf.save_steps,
    # group_by_length=conf.group_by_length,
    lr_scheduler_type=conf.lr_scheduler_type,
    warmup_steps=conf.num_warmup_steps,
    optim=conf.optimizer_type,
    weight_decay=conf.weight_decay,
    bf16=True,
    remove_unused_columns=True,
    gradient_checkpointing=conf.gradient_checkpointing,
    run_name=conf.run_name,
    ddp_find_unused_parameters=False,
    # evaluation_strategy="steps",
    # eval_steps=5,
)

train_dataset, eval_dataset = create_datasets(tokenizer, conf)

# get number of steps during packing
steps_dataset = train_dataset
steps_dataset.infinite = False
counter = 0
for _ in steps_dataset:
    counter += 1
steps = math.ceil(
    counter
    / (
        conf.num_gpus
        * conf.gradient_accumulation_steps
        * conf.per_device_train_batch_size
    )
)
total_steps = conf.num_train_epochs * steps
print(f"Number of training steps: {total_steps}")
training_args.max_steps = total_steps

trainer = SFTTrainer(
    model=base_model,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    peft_config=peft_config,
    packing=True,
    max_seq_length=conf.seq_length,
    tokenizer=tokenizer,
    args=training_args,
)

trainer.train()
trainer.save_model(conf.output_dir)

output_dir = os.path.join(conf.output_dir, "final_checkpoint")
trainer.model.save_pretrained(
    output_dir,
    safe_serialization=True,
)

with open(os.path.join(conf.output_dir, "config.yaml"), "w") as file:
    OmegaConf.save(config=conf, f=file)

# Free memory for merging weights
del base_model
torch.cuda.empty_cache()

model = AutoPeftModelForCausalLM.from_pretrained(
    output_dir,
    device_map="auto",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
)
model = model.merge_and_unload()

output_merged_dir = os.path.join(conf.output_dir, "final_merged_checkpoint")
model.save_pretrained(
    output_merged_dir,
    safe_serialization=True,
)
