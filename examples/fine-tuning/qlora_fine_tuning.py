import json
import logging
import os
import random
import sys
from dataclasses import dataclass, field
from typing import Optional

import datasets
import torch
import transformers
import trl
from accelerate import Accelerator
from accelerate.logging import get_logger
from accelerate.utils import set_seed
from data_functions import create_datasets
from omegaconf import OmegaConf
from peft import AutoPeftModelForCausalLM, LoraConfig
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
)
from trl import DataCollatorForCompletionOnlyLM, SFTTrainer

logger = get_logger(__name__, log_level="info")


def mock_write(console, logger):
    def _mock_write(text):
        logger.info(text)
        real_write = type(console).write
        real_write(console, text)

    return _mock_write


@dataclass
class ScriptArguments:
    config_path: Optional[str] = field(
        default="sft/sft_config.yaml", metadata={"help": "SFT parameters config file"}
    )


parser = HfArgumentParser(ScriptArguments)
conf = parser.parse_args_into_dataclasses()[0]

conf = OmegaConf.load(conf.config_path)

# create output directory
os.makedirs(conf.output_dir, exist_ok=True)
with open(os.path.join(conf.output_dir, "config.yaml"), "w") as file:
    OmegaConf.save(config=conf, f=file)

# basic logging functions
format = "[ %(asctime)s | %(levelname)s | %(module)s ] %(message)s"
log_filepath = os.path.join(
    conf.output_dir, f"{conf.output_dir.strip('/').split('/')[-1]}.log"
)
error_filepath = os.path.join(
    conf.output_dir, f"{conf.output_dir.strip('/').split('/')[-1]}_error.log"
)
logging.basicConfig(
    filename=log_filepath,
    format=format,
    force=True,
)

accelerator = Accelerator()
if accelerator.is_main_process:
    datasets.utils.logging.set_verbosity_warning()
    transformers.utils.logging.set_verbosity_info()

    file_handler = logging.FileHandler(log_filepath)
    formatter = logging.Formatter(format)
    file_handler.setFormatter(formatter)
    sys.stdout.write = mock_write(sys.stdout, logger)
    sys.stderr.write = mock_write(sys.stderr, logger)
else:
    datasets.utils.logging.set_verbosity_error()
    transformers.utils.logging.set_verbosity_error()

# set random seed
if conf.seed == None:
    conf.seed = random.randint(0, 2**32 - 1)

if accelerator.is_main_process:
    print(f"Setting seed value to: {conf.seed}")
set_seed(conf.seed)
trl.set_seed(conf.seed)

# Grab config first
if accelerator.is_main_process:
    print(f"Loading HF Config...")
config = AutoConfig.from_pretrained(
    conf.name_or_path,
    trust_remote_code=True,
)
if conf.attn_impl is not None and hasattr(config, "attn_config"):
    config.attn_config["attn_impl"] = conf.attn_impl

if accelerator.is_main_process:
    print(f"Setting up model parameters...")
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

base_model = AutoModelForCausalLM.from_pretrained(
    conf.name_or_path,
    config=config,
    load_in_4bit=True,
    quantization_config=bnb_config,
    device_map={"": accelerator.local_process_index},
    torch_dtype=torch.bfloat16,
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

# Setup tokenizer
tokenizer = AutoTokenizer.from_pretrained(conf.name_or_path, trust_remote_code=True)
tokenizer.pad_token_id = 3
tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training

# Setup training arguments
training_args = TrainingArguments(
    output_dir=conf.output_dir,
    per_device_train_batch_size=conf.per_device_train_batch_size,
    gradient_accumulation_steps=conf.gradient_accumulation_steps,
    per_device_eval_batch_size=conf.per_device_eval_batch_size,
    learning_rate=conf.learning_rate,
    logging_steps=conf.logging_steps,
    num_train_epochs=conf.num_train_epochs,
    report_to=conf.log_with,
    save_steps=conf.save_steps,
    save_total_limit=1,
    lr_scheduler_type=conf.lr_scheduler_type,
    warmup_steps=conf.num_warmup_steps,
    optim=conf.optimizer_type,
    weight_decay=conf.weight_decay,
    seed=conf.seed,
    bf16=True,
    remove_unused_columns=True,
    gradient_checkpointing=conf.gradient_checkpointing,
    gradient_checkpointing_kwargs={"use_reentrant": True},
    run_name=conf.run_name,
    ddp_find_unused_parameters=False,
    torch_compile=False,
    neftune_noise_alpha=conf.neftune_noise_alpha,
    dataloader_num_workers=4,
)

# Setup datasets
train_dataset, eval_dataset, count_dict = create_datasets(tokenizer, conf)
with open(os.path.join(conf.output_dir, "token_counts.json"), "w") as file:
    json.dump(count_dict, file)

if accelerator.is_main_process:
    print("Sanity check: output sample training examples")
    for index in random.sample(range(len(train_dataset)), 10):
        print("*" * 20)
        print(f"Sample {index} of the training set:.")
        print(train_dataset[index]["text"])
        print()

# setup data collator for response only training
if conf.prompt_format == "sealion":
    response_template = [29864, 229553, 249853, 4]
collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer)

# setup trainer
trainer = SFTTrainer(
    model=base_model,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    peft_config=peft_config,
    dataset_text_field="text",
    max_seq_length=conf.seq_length,
    tokenizer=tokenizer,
    args=training_args,
    data_collator=collator,
    dataset_num_proc=16,
)

if accelerator.is_main_process:
    print("-" * 30)
    print("Setup completed! Begin model training.")
trainer.train()

if accelerator.is_main_process:
    print("Training completed! Saving checkpoints...")
    print("-" * 30)
trainer.save_model(conf.output_dir)

output_dir = os.path.join(conf.output_dir, "final_checkpoint")
trainer.model.save_pretrained(
    output_dir,
    safe_serialization=True,
)
tokenizer.save_pretrained(output_dir)

# Free memory for merging weights
del base_model
accelerator.free_memory()
torch.cuda.empty_cache()

# merge model weights
if accelerator.is_main_process:
    print("Merging model weights")

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
    tokenizer.save_pretrained(output_merged_dir)
