---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
Qwen-SEA-LION-v4-VL Last updated: 2025-11-27
---

# Qwen-SEA-LION-v4-VL

<!-- Provide a quick summary of what the model is/does. -->

Last update: 2025-12-1


**SEA-LION** is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.



**Qwen-SEA-LION-v4-4B-VL** are 4/8-billion parameter Vision-Language Models (VLM) built upon the Qwen3-VL-4B/8B-Instruct architecture. To ensure **domain adaptation** for the region, the model underwent rigorous supervised fine-tuning (SFT) on a curated dataset of approximately **9 million** instruction-text pairs. This extensive post-training instills **multilingual** and **multicultural** fluency, covering English and 7 key SEA languages: Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese.

Qwen-SEA-LION-v4-4B/8B-VL inherits the following features from Qwen3-VL:

- Long-Context Multimodal Architecture (Native 256K context window)
- Edge-Optimized Inference (Resource Efficient)
- Enhanced Vision-Language Capabilities
- Tool Use

<!-- Introduction -->
## Introduction

SEA-LION stands for *Southeast Asian Languages In One Network*. 

Qwen-SEA-LION-v4-4B/8B-VL are 4/8-billion parameter Vision-Language Models (VLM) built upon the Qwen3-VL-4B/8B-Instruct architecture. To ensure **domain adaptation** for the region, the model underwent rigorous supervised fine-tuning (SFT) on a curated dataset of approximately **9 million** instruction-text pairs. This extensive post-training instills **multilingual** and **multicultural** fluency, covering English and 7 key SEA languages: Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese.

Qwen-SEA-LION-v4-4B/8B-VL inherits the following features from Qwen3-VL:

- Long-Context Multimodal Architecture (Native 256K context window)

- Edge-Optimized Inference (Resource Efficient)

- Enhanced Vision-Language Capabilities

- Tool Use


For tokenization, the model employs the default tokenizer used in Qwen3-VL.

- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 256k
- **Language(s):** fine-tuned on Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese
- **License:** [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
- **Finetuned from model:** [Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct), [Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)


## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

The instruction fine-tuning text dataset comprises of a collection of OSS & synthetic data.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Training Hyperparameters

- **Training regime:** Our workflow consists of instruction fine-tuning and model merging. <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->


## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

We evaluated Qwen-SEA-LION-v4-4B/8B-VL on general language capabilities.

*General language capabilities*

For the evaluation of general language capabilities, we employed the [SEA-HELM evaluation benchmark](https://arxiv.org/abs/2502.14301) across a variety of tasks. These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarisation (Abssum), Causal Reasoning (Causal), Natural Language Inference (NLI), Linguistic Diagnostics (LINDSEA), Cultural Knowledge (Kalahi) and Global MMLU Lite.

*Instruction-following and Multi-turn Chat*

We evaluated the models on instruction-following and multi-turn chat capabilities with SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)) respectively. The two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

#### Factors

All evaluations were run with the model specific generation parameters defined in the model config. Each evaluation comprised of 8 runs with different seeds and the final results were averaged across these runs.

For all tasks, the model was expected to provide an answer tag from which the answer was automatically extracted. For tasks where options were provided, the answer should comprise one of the pre-defined options.

The evaluation was done **zero-shot** with native prompts on a sample of 100-1000 instances for each dataset.

*SEA-IFEval*

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalised by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).

*SEA-MTBench*

SEA-MTBench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-4.1-2025-04-14` as the judge model and compare against `gpt-4.1-2025-04-14` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction).

#### Metrics

The following metrics were used for text capabilities:

| **Task** | **Metric** |
| --- | --- |
| Sentiment Analysis | Accuracy |
| Extractive QA (ID, VI, TH, TA) | ChrF++ |
| MCQ-QA (TL, MY, MS) | Accuracy |
| Metaphor | Accuracy |
| Abstractive Summarisation | Rouge-L |
| Translations | MetricX-24 score (with reference) |
| Causal Reasoning | Accuracy |
| Natural Language Inference | Accuracy |
| LINDSEA | Accuracy |
| Global MMLU Lite | Accuracy |
| ThaiExam | Accuracy |
| Kalahi | Accuracy |
| SEA-IFEval | Accuracy |
| SEA-MTBench | Win rate against a reference |

### Retaining VL Capabilities

We also evaluated our models on two types of tasks using datasets specifically focused on Southeast Asian examples to benchmark and compared our models' performances against the original base models (Qwen3-VL-4B/8B).

- Visual Question Answering (VQA): We utilised Multiple Choice Question (MCQ) style tasks, including MARVL, CVQA, and WorldCuisines.
- Image Captioning: We employed the XM3600 dataset, evaluating strictly on examples relevant to the SEA region.

Key Insight: Despite our fine-tuning process focusing primarily on text data (approximately 8 million regional Q&A and instruction pairs), our evaluations confirm that Qwen-SEA-LION-v4 (4B/8B) successfully retains the high-performance vision-language capabilities of the original base models.

#### Factors

The evaluation was done **zero-shot** with native prompts.

#### Metrics

The following metrics were used to measure performance:

- **Normalised accuracy** was the primary metric for the VQA tasks (CVQA, MARVL, and WorldCuisines).
- **RefCLIP Score** was used for the XM3600 image captioning task.

### Results

For details on Qwen-SEA-LION-v4-VL performances, please refer to the SEA-HELM leaderboard, <https://leaderboard.sea-lion.ai/>.


## Download the Models

Qwen-SEA-LION-v4-VL models are available for download via the following channels:
🤗[HuggingFace SEA-LION v4 Collection]((https://huggingface.co/collections/aisingapore/sea-lion-v4))

|Model	                        |Download                                                      |
|-------------------------------|--------------------------------------------------------------|
|Qwen-SEA-LION-v4-4B-VL	        |[HuggingFace](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-4B-VL)|
|Qwen-SEA-LION-v4-8B-VL	        |[HuggingFace](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-8B-VL)|

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->


## How to Get Started with the Model

Use the code below to get started with the model with 🤗 Transformers libraries.

```bash
  pip install transformers>=4.57.0 
```


```python
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor

# default: Load the model on the available device(s)
model = Qwen3VLForConditionalGeneration.from_pretrained(
    "aisingapore/Qwen-SEA-LION-v4-8B-VL", dtype="auto", device_map="auto"
)

# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.
# model = Qwen3VLForConditionalGeneration.from_pretrained(
#     "aisingapore/Qwen-SEA-LION-v4-8B-VL",
#     dtype=torch.bfloat16,
#     attn_implementation="flash_attention_2",
#     device_map="auto",
# )

processor = AutoProcessor.from_pretrained("Qwen/Qwen3-VL-4B-Instruct")

messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}]
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Write a poem on southeast asian countries in Indonesian."}
        ],
    }
]

# Preparation for inference
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
)
inputs = inputs.to(model.device)

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)  
```

### Disclaimer

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model has not been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable for any claims, 
damages, or other liabilities arising from the use of the released weights and codes.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

*The model was not tested for robustness against adversarial prompting.* It is important for users to be aware that our model exhibits certain limitations that warrant consideration. 
Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, 
introducing fictional elements that are not grounded in the provided context. 
Users should also exercise caution in interpreting and validating the model's responses 
due to the potential inconsistencies.

## More Information

This is the repository for the commercial instruction-tuned model. The model has *not* been aligned 
for safety. Developers and users should perform their own safety fine-tuning and related security 
measures. In no event shall the authors be held liable for any claims, damages, or other liabilities
arising from the use of the released weights and codes.

For more info, please contact us at  [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6) or [sealion@aisingapore.org](mailto:sealion@aisingapore.org)







