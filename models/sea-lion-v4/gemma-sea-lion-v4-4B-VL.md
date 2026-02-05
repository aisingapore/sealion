# Gemma-SEA-LION-v4-4B-VL

<!-- Provide a quick summary of what the model is/does. -->

Last updated: 2026-02-05

SEA-LION is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

**Gemma-SEA-LION-v4-4B-VL** is a 4-billion parameter Vision-Language Model (VLM) built upon the gemma-3-4b-it architecture. To ensure **domain adaptation** for the region, the model underwent rigorous post-training on a curated dataset of approximately **8.54 million** instruction-text pairs. This curated dataset included various SEA Languages such as Burmese, Malay, Tagalog and Tamil. This extensive post-training instills **multilingual** and **multicultural** fluency for both SEA languages and English.

Gemma-SEA-LION-v4-4B-VL inherits the image and text capabilities from gemma-3-4b-it alongside its large context length of 128K tokens. Additionally, beyond extending the multilingual capabilities of the original gemma model for SEA languages, we experimented with:

1. Adding function calling to the model to allow for this model to be used in tool calling applications
2. The visual parsing capabilities in Thai, Chinese and English

## Model Details

### Model Description

We performed post-training in English and SEA languages on Gemma-SEA-LION-v4-27B-IT, a decoder model using the Gemma 3 architecture, to create Gemma-SEA-LION-v4-4B-VL.

For tokenization, the model employs the default tokenizer used in gemma-3-4b-it.

- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s) (NLP):** fine-tuned on Burmese, English, Khmer, Malay, Tagalog and Tamil
- **License:** [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- **Finetuned from model:** [gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it)

As of Feb 2026, Gemma-SEA-LION-v4-4B-VL outperforms other open models in the small parameter class on SEA tasks, achieving performance comparable to larger, proprietary models. For detailed rankings, please refer to the [leaderboard](https://leaderboard.sea-lion.ai/).

## Uses

### Out-of-Scope Use

The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

## Bias, Risks, and Limitations

*The model was not tested for robustness against adversarial prompting.* It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies.

**Limitations**

In terms of text capability, Gemma-SEA-LION-v4-4B-VL has been trained and fine-tuned exclusively on the vision-text backend. As a result, its text capabilities are expected to be comparable to those of Gemma-SEA-LION-v4-27B-IT, and may not exhibit significant improvements or differences in this area.

## How to Get Started with the Model

Use the code below to get started with the model using the 🤗 Transformers library.

```python 
pip install transformers>=4.50.0

```

```python
from transformers import pipeline
import torch

pipe = pipeline(
    "image-text-to-text",
    model="aisingapore/Gemma-SEA-LION-v4-4B-VL",
    device="cuda",
    torch_dtype=torch.bfloat16
)
messages = [
  {
      "role": "system",
      "content": [{"type": "text", "text": "You are a helpful assistant."}]
  },
  {
      "role": "user",
      "content": [
          {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
          {"type": "text", "text": "Response in Indonesian. What animal is on the candy? Describe in Indonesian and English."}
      ]
  }
]

output = pipe(text=messages, max_new_tokens=200)
print(output[0]["generated_text"][-1]["content"])
# Okay, let's take a look!
# Based on the image, the animal on the candy is a **turtle**.
# You can see the shell shape and the head and legs.

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

- **Training regime:**  Our post-training workflow consists of Instruction Fine-tuning, Model Merging and Reinforcement Learning.

For details on Gemma-SEA-LION-v4-4B-VL performance, please refer to the SEA-HELM leaderboard, <https://leaderboard.sea-lion.ai/>.

## Hardware 
- **Hardware Type:** Nvidia H200 140GB GPUs
- **Cloud Provider:** SMC H200
- **Compute Region:** Singapore

## More Information

This is the repository for the commercial instruction-tuned model. The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore.

