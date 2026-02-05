# Apertus-SEA-LION-v4-8B

Last updated: 2026-02-05


**SEA-LION** is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

<!-- Introduction -->
## Introduction
SEA-LION stands for *Southeast Asian Languages In One Network*. 

**Apertus-SEA-LION-v4-8B-IT** is a 8-billion parameter model built upon the Apertus-8B-Instruct architecture. To ensure **domain adaptation** for the region, the model underwent rigorous post-training on a curated dataset of approximately **8.54 million** instruction-text pairs.

This extensive post-training instills **multilingual** and **multicultural** fluency, covering key SEA languages such as Burmese, Malay, Tagalog and Tamil. The dataset also includes 347,000 tool-calling instruction-text pairs to impart these capabilities, in addition to linguistic fluency.

Apertus-SEA-LION-v4-8B-IT is designed as a fully open model; to align with this core philosophy, we have released the datasets used for post-training, as well as the evaluation codes and datasets used to evaluate the model.

These resources can be accessed via the link below.

- [Open post-training datasets](#Training-Data) we used.
- [SEA-HELM Evaluation codes and datasets](<https://github.com/aisingapore/SEA-HELM>)

## Model Details

### Model Description

SEA-LION stands for *Southeast Asian Languages In One Network*.

We performed post-training in English and SEA languages on Apertus-8B-Instruct-2509, a decoder model using the Apertus architecture, and post-training to create Apertus-SEA-LION-v4-8B-IT.

For tokenization, the model employs the default tokenizer used in Apertus-8B-Instruct-2509.

- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 65k
- **Language(s):** fine-tuned on English, Burmese, Tagalog, Malay and Tamil
- **License:** [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
- **Finetuned from model:** [Apertus-8B-Instruct](https://huggingface.co/swiss-ai/Apertus-8B-Instruct-2509)

### Model Sources

- **Repository:** <https://huggingface.co/collections/aisingapore/sea-lion-v4>

## Uses

### Out-of-Scope Use

The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.


### Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

*The models were not tested for robustness against adversarial prompting.* It is important for users to be aware that our models exhibit certain limitations that warrant consideration. 
Like many LLMs, the models can hallucinate and occasionally generates irrelevant content, 
introducing fictional elements that are not grounded in the provided context. 
Users should also exercise caution in interpreting and validating the model's responses 
due to the potential inconsistencies.



## How to Get Started with the Model

Use the code below to get started with the model with 🤗 Transformers libraries.

```python
pip install transformers>=4.56.0

```

```python
# The code is adopted from Apertus example
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "aisingapore/Apertus-SEA-LION-v4-8B-IT"
device = "cuda"  # for GPU usage or "cpu" for CPU usage

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
).to(device)

# prepare the model input
prompt = "Explain the concept of 'Hari Raya Puasa' in simple terms."
messages_think = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages_think,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt", add_special_tokens=False).to(model.device)

# Generate the output
generated_ids = model.generate(**model_inputs, max_new_tokens=32768)

# Get and decode the output
output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```
### Tool Calling

The prompt in the example is in Malay and translates to “Please help me find a 4-room flat near Tampines, budget under $500,000. I also want to know the estimated monthly loan payment.”

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('aisingapore/gemma-sealion-4b-v4-cand5', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "aisingapore/gemma-sealion-4b-v4-cand5",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "Tolong carikan flat 4-bilik dekat Tampines, bajet bawah $500,000. Nak tahu juga berapa anggaran pinjaman bulanan."}
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_hdb_listings",
            "description": "Search for HDB flats available for sale",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "Town or area name"},
                    "flat_type": {"type": "string", "description": "Flat type e.g. 3-room, 4-room, 5-room"},
                    "max_price": {"type": "number", "description": "Maximum price in SGD"}
                },
                "required": ["location", "flat_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_mortgage",
            "description": "Calculate estimated monthly mortgage payment",
            "parameters": {
                "type": "object",
                "properties": {
                    "loan_amount": {"type": "number", "description": "Loan amount in SGD"},
                    "interest_rate": {"type": "number", "description": "Annual interest rate as percentage"},
                    "loan_tenure_years": {"type": "integer", "description": "Loan period in years"}
                },
                "required": ["loan_amount"]
            }
        }
    }
]

input_ids = tokenizer.apply_chat_template(
    messages,
    tools=tools,
    return_tensors="pt",
    add_generation_prompt=True
).to(model.device)

generated_ids = model.generate(
    input_ids,
    max_new_tokens=512,
    do_sample=False,
)

response = tokenizer.decode(
    generated_ids[0][input_ids.shape[1]:],
    skip_special_tokens=False,
).replace("", "").strip()

print(response)
```

## Training Details

### Training Data

The instruction fine-tuning text dataset comprises of a collection of OSS & synthetic data. The datasets used for post-training can be accessed via the link below.

**Datasets for Instruction Fine Tuning**:

- 🤗[aisingapore/SEA-Instruct-2602](https://huggingface.co/datasets/aisingapore/SEA-Instruct-2602)

**Datasets for Tool-calling**:

- 🤗[allenai/Dolci-Instruct-SFT-Tool-Use](https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT-Tool-Use)
- 🤗[Agent-Ark/Toucan-1.5M](https://huggingface.co/datasets/Agent-Ark/Toucan-1.5M)

**Datasets for Reinforcement Learning:**

- 🤗[nvidia/Nemotron-Cascade-RL-Instruction-Following](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-RL-Instruction-Following)
- 🤗[openai/gsm8k](https://huggingface.co/datasets/openai/gsm8k)

### Training Procedure

#### Training Hyperparameters

- **Training regime:** Our post-training workflow consists of instruction fine-tuning and model merging.
- **Training hyperparameters:** The following hyperparameters were used during training:

| Category | Hyperparameter | Value |
| --- | --- | --- |
| **Optimization** | Optimizer | `ADAMW_TORCH_FUSED` (β1=0.9, β2=0.999, ε=1e-08) |
| **Batch Size** | Train Batch Size (per device) | `1` |
|  | Eval Batch Size (per device) | `1` |
| **Hardware** | Distributed Type | `multi-GPU` |
|  | Number of Devices | `64` |
| **Schedule** | LR Scheduler Type | `constant_with_warmup` |
|  | LR Scheduler Warmup Steps | `269` |
| **Other** | Training Steps | `5397` |
|  | Seed | `42` |

## Evaluation

### Testing Data, Factors & Metrics

We evaluated Apertus-SEA-LION-v4-8B-IT on general language capabilities and LLM-specific capabilities using SEA-HELM.

### Results

For details on Apertus-SEA-LION-v4-8B-IT performance, please refer to the [Leaderboard results on SEA-HELM](https://leaderboard.sea-lion.ai/).


## Download the Models

The Apertus-SEA-LION-v4-8B models are available for download via the 🤗 [HuggingFace Apertus-SEA-LION-v4-8B-IT](https://huggingface.co/aisingapore/Apertus-SEA-LION-v4-8B-IT) repository. You can also explore more models in the same collection at 🤗 [HuggingFace SEA-LION v4 Collection](https://huggingface.co/collections/aisingapore/sea-lion-v4).




## More Information

This is the repository for the commercial instruction-tuned model. 
The models have *not* been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable 
for any claims, damages, or other liabilities arising from the use of the released weights and codes.

For more info, please contact us at [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6) or sealion@aisingapore.org
