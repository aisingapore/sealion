# Gemma-SEA-LION-v4-27B-VL

<!-- Provide a quick summary of what the model is/does. -->

Last updated: 2025-10-17

**SEA-VLM** is an instruct-tuned vision-text model for the Southeast Asia (SEA) region.

Gemma-SEA-LION-v4-27B-VL has undergone post-training using instruction-image pairs datasets in Burmese, English, Indonesian, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese, comprising approximately 540k samples in total, to create *Gemma-SEA-LION-v4-27B-VL*.

Gemma-SEA-LION-v4-27B-VL inherits Gemma 3's:

- Large 128K context length
- Image and text understanding capabilities, including document comprehension, visual Q&A, and image-grounded reasoning
- Advanced function calling and structured outputs to allow for seamless integration into larger systems

## Model Details

### Model Description

We performed post-training in English and SEA languages on Gemma-SEA-LION-v4-27B-IT, a decoder model using the Gemma 3 architecture, to create Gemma-SEA-LION-v4-27B-VL.

For tokenization, the model employs the default tokenizer used in Gemma 3 27B IT.

- **Developed by:** SEACrowd and Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** SEACrowd and Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s) (NLP):** Burmese, English, Indonesian, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese
- **License:** [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- **Finetuned from model:** [Gemma-SEA-LION-v4-27B-IT](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT)

As of 15 October 2025, Gemma-SEA-LION-v4-27B-VL excels at Southeast Asian (SEA) tasks when compared to other open models with fewer than 200 billion parameters and demonstrates performance comparable to that of larger and top closed models. For detailed rankings, please refer to the [leaderboard](https://leaderboard.sea-lion.ai/).

## Uses

### Out-of-Scope Use

The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

## Bias, Risks, and Limitations

*The model was not tested for robustness against adversarial prompting.* It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies.

**Limitations**

In terms of text capability, Gemma-SEA-LION-v4-27B-VL has been trained and fine-tuned exclusively on the vision-text backend. As a result, its text capabilities are expected to be comparable to those of Gemma-SEA-LION-v4-27B-IT, and may not exhibit significant improvements or differences in this area.

## How to Get Started with the Model

Use the code below to get started with the model using the 🤗 Transformers library.

```python
from transformers import pipeline
import torch

pipe = pipeline(
    "image-text-to-text",
    model="aisingapore/Gemma-SEA-LION-v4-27B-VL",
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
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    }
]

output = pipe(text=messages, max_new_tokens=200)
print(output[0]["generated_text"][-1]["content"])

```
## Training Details

### Training Data

The dataset comprises vision-text paired in Burmese, English, Indonesian, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese languages, collected from a mixture of sources including web data, code, open-source datasets.

### Training Procedure

#### Training Hyperparameters

- **Training regime:**

We perform SFT using 540k of vision-text samples written in 10 languages. Then, we perform model merging with Gemma3-27B-IT to preserve general vision-text knowledge.


For details on Gemma-SEA-LION-v4-27B-VL performance, please refer to the SEA-LION.ai blogpost, [SEA-LION v4 VL new members](https://sea-lion.ai/sea-lion-v4-VL-new-members/).

## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** Nvidia H200 140GB GPUs
- **Hours used:** 13 hrs
- **Cloud Provider:** SMC H200
- **Compute Region:** Singapore
- **Carbon Emitted:** appx. 27 kg CO2 e

## More Information

This is the repository for the commercial instruction-tuned model. The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore.

