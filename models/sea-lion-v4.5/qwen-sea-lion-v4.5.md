# Model Card for Qwen-SEA-LION-v4.5-27B-IT

Last update: 2026-05-19

**SEA-LION** is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

The **Qwen-SEA-LION-v4.5-27B-IT** sub-collection — comprising the standard high-fidelity model and its speed-optimized companion, the **27B-IT-Assistant** — is built upon the Qwen3.6-27B dense architecture, a 27-billion parameter model featuring a hybrid Linear and Full Attention design. To ensure deep domain adaptation, both models underwent extensive distillation from Qwen/Qwen3.5-397B-A17B on the updated aisingapore/SEA-Instruct-2602 dataset. This instills native multilingual and multicultural fluency across English and key SEA languages (Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese), with the Assistant variant specifically engineered to maximize throughput and minimize inference latency in production environments.

**Qwen-SEA-LION-v4.5-27B-IT-Assistant** is a draft model using speculative decoding method to employ a lightweight **block diffusion** model to draft multiple tokens in parallel trained from **Qwen-SEA-LION-v4.5-27B-IT**. This is the drafter model, which must be paired with aisingapore/Qwen-SEA-LION-v4.5-27B-IT.

Qwen-SEA-LION-v4.5-27B-IT inherits the following features from Qwen3.6:

- **Context Window (262K):** Reduce if facing OOM errors but keep ≥128K to preserve full reasoning capabilities.
- **Unified Vision-Language:** Early fusion training delivers good performance across multimodal reasoning, coding, and visual tasks.
- **Scalable RL:** Trained in million-agent environments for robust, real-world SEA adaptability.
- **Broad Linguistic Coverage:** Deeply specialized in SEA cultural nuances while supporting 201 languages globally.
- **Advanced Infrastructure:** Utilizes highly efficient multimodal training and asynchronous RL frameworks.
- **Agentic Coding:** High-precision handling of repository-level reasoning and frontend workflows.
- **Thinking Preservation:** Retains historical reasoning context to streamline iterative development and reduce compute overhead.

## Model Details

### Model Description

SEA-LION stands for Southeast Asian Languages In One Network.

We performed post-training in English and SEA languages on Qwen3.6-27B, a multimodal learning model using the Qwen3.6 architecture, to create Qwen-SEA-LION-v4.5.

For tokenization, the model employs the default tokenizer used in Qwen3.6.

- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Causal Language Model with Vision Encoder
- **Training Stage:** Post-Training (Logit Distillation & Model Merging))
- **Context length:** 262k
- **Language(s):** fine-tuned on Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese
- **License:** [Apache-2.0](https://github.com/QwenLM/Qwen3.6/blob/main/LICENSE)
- **Finetuned from model:** <https://huggingface.co/Qwen/Qwen3.6-27B>

### Model Sources

**Qwen-SEA-LION-v4.5-27B-IT** models are available for download via the following channels:

[HuggingFace SEA-LION v4.5 Collection](https://huggingface.co/collections/aisingapore/sea-lion-v45)

| Model                               | Download                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| Qwen-SEA-LION-v4.5-27B-IT           | [HuggingFace](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4.5-27B-IT)           |
| Qwen-SEA-LION-v4.5-27B-IT-Assistant | [HuggingFace](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4.5-27B-IT-Assistant) |

## How to Get Started with the Model

Use the code below to get started with the model with 🤗 Transformers libraries.

```
pip install "transformers>=4.57.0" accelerate vllm
```

```python
# ============================================================
# TEXT-ONLY INFERENCE example
# ============================================================

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "aisingapore/Qwen-SEA-LION-v4.5-27B-IT"

# ── Load tokenizer ──
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# ── Load model in bfloat16 across all available GPUs ──
# attn_implementation="sdpa" is safer for the hybrid DeltaNet arch;
# flash_attention_2 compatibility depends on your transformers version
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="sdpa",  # use sdpa for DeltaNet hybrid layers
)

# ── Message: text-only, same Malay query from original snippet ──
messages = [
    {
        "role": "user",
        "content": "Tolong carikan flat 4-bilik dekat Tampines, bajet bawah $500,000. "
                   "Nak tahu juga berapa anggaran pinjaman bulanan."
    }
]

# ── Apply chat template — text-only, thinking disabled ──
# enable_thinking=False → instruct/non-thinking mode
# Qwen3.6 does NOT support /no_think soft switch unlike Qwen3
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,      # hard-disable CoT thinking blocks
)

# ── Tokenize ──
inputs = tokenizer(text, return_tensors="pt").to(model.device)

# ── Generate — non-thinking mode params ──
# presence_penalty=1.5 is important for Qwen3.6 non-thinking mode
# to suppress repetition; not available in model.generate() directly,
# so use do_sample=True with the temperature/top_p/top_k trio
generated_ids = model.generate(
    **inputs,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,    # non-thinking instruct mode
    top_p=0.80,
    top_k=20,
    # Note: presence_penalty requires vLLM/SGLang for full effect;
    # in transformers use repetition_penalty as a proxy
    repetition_penalty=1.1,
)

# ── Decode only newly generated tokens ──
output_ids = generated_ids[0][inputs["input_ids"].shape[1]:]
response = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
print(response)
```

#### Tool Calling example

```python
# ============================================================
# TOOL CALLING (Transformers, local)
# ============================================================

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "aisingapore/Qwen-SEA-LION-v4.5-27B-IT"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="sdpa",
)

messages = [
    {
        "role": "user",
        "content": "Tolong carikan flat 4-bilik dekat Tampines, bajet bawah $500,000. "
                   "Nak tahu juga berapa anggaran pinjaman bulanan."
    }
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
                    "location": {
                        "type": "string",
                        "description": "Town or area name"
                    },
                    "flat_type": {
                        "type": "string",
                        "description": "Flat type e.g. 3-room, 4-room, 5-room"
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Maximum price in SGD"
                    }
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
                    "loan_amount": {
                        "type": "number",
                        "description": "Loan amount in SGD"
                    },
                    "interest_rate": {
                        "type": "number",
                        "description": "Annual interest rate as percentage"
                    },
                    "loan_tenure_years": {
                        "type": "integer",
                        "description": "Loan period in years"
                    }
                },
                "required": ["loan_amount"]
            }
        }
    }
]

# ============================================================
# apply_chat_template returns BatchEncoding with keys:
#   input_ids, attention_mask (and sometimes token_type_ids)
# ============================================================

inputs = tokenizer.apply_chat_template(
    messages,
    tools=tools,
    return_tensors="pt",
    return_dict=True,          # ← returns BatchEncoding dict with attention_mask
    add_generation_prompt=True,
    enable_thinking=False,     # disable CoT for structured tool call output
).to(model.device)

# ── Unpack BatchEncoding dict with ** — fixes the AttributeError ──
generated_ids = model.generate(
    **inputs,                  # ← unpack: passes input_ids + attention_mask
    max_new_tokens=512,
    do_sample=False,
)

# ── Decode only new tokens — slice off the prompt portion ──
output_ids = generated_ids[0][inputs["input_ids"].shape[1]:]
response = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
print(response)

```

**Agentic Example:**

```python
# ============================================================
# NO-VLLM AGENTIC LOOP
# ============================================================

import os
import json
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = "aisingapore/Qwen-SEA-LION-v4.5-27B-IT"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    token=os.getenv("HF_TOKEN"),
)

print("Loading model across GPUs...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    token=os.getenv("HF_TOKEN"),
    torch_dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="sdpa",
)

device_info = getattr(model, "hf_device_map", None) or str(model.device)
print(f"Model loaded. Device: {device_info}")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_hdb_listings",
            "description": "Search for HDB flats available for sale",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "Town or area name"},
                    "flat_type": {"type": "string", "description": "e.g. 4-room"},
                    "max_price": {"type": "number", "description": "Max price in SGD"},
                },
                "required": ["location", "flat_type"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_mortgage",
            "description": "Calculate estimated monthly mortgage payment",
            "parameters": {
                "type": "object",
                "properties": {
                    "loan_amount": {"type": "number", "description": "Loan amount SGD"},
                    "interest_rate": {"type": "number", "description": "Annual rate %"},
                    "loan_tenure_years": {"type": "integer", "description": "Loan years"},
                },
                "required": ["loan_amount"],
            },
        },
    },
]

def execute_tool(name: str, arguments: dict) -> str:
    """Mock tool executor — replace with real API calls."""
    if name == "search_hdb_listings":
        return json.dumps({
            "listings": [
                {
                    "address": "Blk 472 Tampines St 43",
                    "flat_type": arguments.get("flat_type"),
                    "resale_price": 488000,
                    "floor_area_sqm": 93,
                    "remaining_lease": "67 years",
                },
                {
                    "address": "Blk 512 Tampines Ave 4",
                    "flat_type": arguments.get("flat_type"),
                    "resale_price": 475000,
                    "floor_area_sqm": 89,
                    "remaining_lease": "62 years",
                },
            ]
        })
    elif name == "calculate_mortgage":
        principal = arguments["loan_amount"]
        r = (arguments.get("interest_rate", 2.6) / 100) / 12
        n = arguments.get("loan_tenure_years", 25) * 12
        monthly = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return json.dumps({
            "loan_amount": principal,
            "monthly_repayment_sgd": round(monthly, 2),
        })
    return json.dumps({"error": f"Unknown tool: {name}"})

def generate_response(messages: list) -> str:
    """
    Single model.generate() call.
    Returns the raw decoded string (may contain tool call JSON).
    """
    # ── Render chat template to string first ──
    text = tokenizer.apply_chat_template(
        messages,
        tools=TOOLS,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,      # no  blocks for tool calling
 )

 # ── Tokenize separately ──
 inputs = tokenizer(text, return_tensors="pt").to(model.device)

 # ── Generate ──
 with torch.no_grad(): # saves memory during inference
 generated_ids = model.generate(
 **inputs,
 max_new_tokens=512,
 do_sample=False, # greedy for deterministic tool JSON
 )

 # ── Decode new tokens only ──
 output_ids = generated_ids[0][inputs["input_ids"].shape[1]:]
 return tokenizer.decode(output_ids, skip_special_tokens=True).strip()

def parse_tool_calls(response_text: str) -> list:
 """
 Parse Hermes-style tool call JSON from model output.
 Qwen3.6 emits tool calls wrapped in ... tags.
 Returns list of {"name": ..., "arguments": {...}} dicts.
 Falls back to empty list if no tool calls found.
 """
 import re
 tool_calls = []

 # ── Match {...} blocks ──
 pattern = r"(.*?)"
 matches = re.findall(pattern, response_text, re.DOTALL)

 for match in matches:
 try:
 call = json.loads(match.strip())
 tool_calls.append(call)
 except json.JSONDecodeError:
 print(f" [WARN] Could not parse tool call JSON: {match[:100]}")

 return tool_calls

def run_agent(user_query: str, max_steps: int = 10) -> str:
 """
 Transformers-native agentic loop — no vLLM or API server needed.

 Loop:
 1. Generate response
 2. Parse tool calls from output
 3. Execute tools, append results
 4. Repeat until no tool calls in response
 """
 messages = [
 {
 "role": "system",
 "content": (
 "You are a helpful Singapore housing assistant. "
 "Always call the relevant tools to get accurate data before answering. "
 "Give a clear, concise summary after gathering all information."
 ),
 },
 {"role": "user", "content": user_query},
 ]

 print(f"\n{'='*60}")
 print(f"USER: {user_query}")
 print(f"{'='*60}")

 for step in range(max_steps):
 print(f"\n[Step {step + 1}] Generating...")

 response_text = generate_response(messages)
 print(f" Raw output: {response_text[:200]}...")

 # ── Try to parse tool calls from the response ──
 tool_calls = parse_tool_calls(response_text)

 if tool_calls:
 print(f" → Found {len(tool_calls)} tool call(s)")

 # ── Append assistant turn with raw response ──
 messages.append({
 "role": "assistant",
 "content": response_text,
 })

 # ── Execute each tool and append results ──
 for call in tool_calls:
 fn_name = call.get("name", "")
 fn_args = call.get("arguments", {})

 # ── arguments may be a string or dict depending on model output ──
 if isinstance(fn_args, str):
 fn_args = json.loads(fn_args)

 print(f" • {fn_name}({json.dumps(fn_args, ensure_ascii=False)})")
 result = execute_tool(fn_name, fn_args)
 print(f" ↳ {result[:150]}")

 # ── Append tool result as tool role message ──
 messages.append({
 "role": "tool",
 "name": fn_name,
 "content": result,
 })

 continue # loop back for next generation

 # ── No tool calls — this is the final answer ──
 print(f"\n{'='*60}")
 print(f"AGENT FINAL ANSWER:\n{response_text}")
 print(f"{'='*60}\n")
 return response_text

 return "[Agent stopped: exceeded maximum steps]"

# ── Run examples ──
if __name__ == "__main__":

 run_agent(
 "Tolong carikan flat 4-bilik dekat Tampines, bajet bawah $500,000. "
 "Nak tahu juga berapa anggaran pinjaman bulanan."
 )
```

Output

```
============================================================
AGENT FINAL ANSWER:

Tampines

4-room

500000

============================================================
```

Use the code below to get aisingapore/Qwen3.6-27B-Assistant booster with vLLM.

```
CUDA_VISIBLE_DEVICES=0 vllm serve aisingapore/Qwen-SEA-LION-v4.5-27B-IT \
--speculative-config '{"method": "dflash", "model": "aisingapore/Qwen3.6-27B-Assistant", "num_speculative_tokens": 16}' \
--attention-backend flash_attn \
--max-num-batched-tokens 32768 \
--gdn-prefill-backend triton
```

## Training Details

### Training Data

🤗[aisingapore/SEA-Instruct-2602](https://huggingface.co/datasets/aisingapore/SEA-Instruct-2602)

### Training Regime

Our post-training workflow consists solely of distillation and model merging.

## Evaluation

### Testing Data, Factors & Metrics

We evaluated Qwen-SEA-LION-v4.5 on general language, multi-turn chat and instruction-following capabilities.

#### Results

For details on Qwen-SEA-LION-v4.5-27B-IT performance, please refer to the [SEA-LION Leaderboard](https://leaderboard.sea-lion.ai/).

## Technical Specifications

### Model Architecture

The architecture is based on the highly efficient Qwen3.6 foundation. The detailed architecture can be found at <https://huggingface.co/Qwen/Qwen3.6-27B#model-overview>.

## Uses

### Out-of-Scope Use

The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

### Bias, Risks, and Limitations

The model was not tested for robustness against adversarial prompting. It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies.
