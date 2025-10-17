---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
Qwen-SEA-LION-v4-32B-IT (Both Models for Github) Last updated: 2025-10-17 
---

# Qwen-SEA-LION-v4-32B-IT

Last updated: 2025-10-17

*SEA-LION* is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

**Qwen-SEA-LION-v4-32B-IT** is based on Qwen3, which provides a strong foundation with support for over 100 languages and advanced reasoning capabilities. The model underwent continued pre-training on approximately **100B tokens** sampled from the SEA-Pile v2 pretraining corpus of over one trillion tokens across 7 SEA languages: Burmese, Indonesian, Malay, Filipino, Tamil, Thai, and Vietnamese. Finally, it was post-trained on a high-quality dataset of approximately **8 million question-and-answer pairs** to create the final instruction-tuned model.

Qwen-SEA-LION-v4-32B-IT inherits the following features from Qwen3-32B:

- 32,768 of context length natively

## Model Details

### Model Description

SEA-LION stands for *Southeast Asian Languages In One Network*.

We performed continued pre-training in English and SEA languages on Qwen3-32B, a decoder model using the Gemma 3 architecture, and post-training to create Qwen-SEA-LION-v4-32B-IT.

For tokenization, the model employs the default tokenizer used in Qwen3-32B.

- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context Length:** 128k tokens
- **Language(s) (NLP):** Burmese, English, Indonesian, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai, and Vietnamese
- **License:** [Qwen Terms of Service](https://qwen.ai/termsservice) / [Qwen Usage Policy](https://qwen.ai/usagepolicy)
- **Continue pretrained from model:** [Qwen-3-32B](https://huggingface.co/Qwen/Qwen3-32B)

## Uses

### Out-of-Scope Use

The model has *not* been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

## Bias, Risks, and Limitations

### Caveats || Risks

*The model was not tested for robustness against adversarial prompting.*  It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies.

## Limitations

In terms of vision capability, Qwen-SEA-LION-v4-32B-IT has been trained and fine-tuned exclusively on the text back-end. As a result, its vision capabilities are expected to be comparable to those of Qwen3-32B, and may not exhibit significant improvements or differences in this area. (<https://huggingface.co/Qwen/Qwen3-32B> )

## How to Get Started with the Model

Use the code below to get started with the model using the 🤗 Transformers library.

> The model defaults to non-thinking mode. To enable thinking mode, please use `enable_thinking=True`.
>
>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "aisingapore/Qwen-SEA-LION-v4-32B"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Create a poem that captures the seaside scenery across Southeast Asian countries, including transcriptions in their respective languages."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

# parsing thinking content
try:
    # rindex finding 151668 ()
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)
print("content:", content)

```
## Training Details

**Training Datasets**

The instruction fine-tuning dataset combines our SEA-Instruct, Infinity-Instruct, and OpenMath-Instruct 2 with open-source datasets. For the Online RL datasets, open sourced datasets such as nvidia/Llama-Nemotron-Post-Training-Dataset (RL set) and zwhe99/DeepMath-103K were used.

#### Training Procedure

**Training regime**

Our post-training workflow consists of multiple stages: instruction fine-tuning, model merging, online RL for both instruction following and math using DRGPPO, and then followed by on-policy alignment via APO.

## Uses

### Available Versions

- [Qwen-SEA-LION-v4-32B-IT](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-32B-IT)
- [Qwen-SEA-LION-v4-32B-IT-4BIT](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-32B-IT-4BIT)
- [Qwen-SEA-LION-v4-32B-IT-8BIT](https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-32B-IT-8BIT)

### Resource Metrics

| Quantized Variant | Model Size (GB) | VRAM Required (GB) | Time to First Token (s) | Tokens per Second |
| --- | --- | --- | --- | --- |
| BF16 | 65.57 | 61.03 | 0.34 | 58.84 |
| 8-bit (GPTQ) | 34.34 | 32.04 | 0.35 | 68.85 |
| 4-bit (GPTQ) | 19.93 | 19.43 | 0.34 | 78.20 |

*Additional Remarks:*

- TTFT and Toks per Sec: measured with vLLM on localhost and concurrency = 1.
- Reported results are the median (p50) values, calculated across 10 requests.
(11 requests were run and the first result was dropped, to eliminate cold-start delays)
- Model size taken from vLLM upon loading
- Input size 4K, output 1K
- Tests conducted on a system with an NVIDIA H200 GPU

## Evaluation

### Testing Data, Factors & Metrics

We evaluated Qwen-SEA-LION-v4-32B-IT on general language, multi-turn chat and instruction-following capabilities.

#### Testing Data

General language capabilities

For the evaluation of general language capabilities, we employed the [SEA-HELM evaluation benchmark](https://arxiv.org/abs/2502.14301) across a variety of tasks. These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarisation (Abssum), Causal Reasoning (Causal), Natural Language Inference (NLI), Linguistic Diagnostics (LINDSEA), Cultural Knowledge (Kalahi) and Global MMLU Lite.

Instruction-following and Multi-turn Chat

We evaluated the models on instruction-following and multi-turn chat capabilities with SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)) respectively. The two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

#### Factors

All evaluations were run with the model specific generation parameters defined in the model config. Each evaluation comprised of 8 runs with different seeds and the final results were averaged across these runs.

For all tasks, the model was expected to provide an answer tag from which the answer was automatically extracted. For tasks where options were provided, the answer should comprise one of the pre-defined options.

The evaluation was done **zero-shot** with native prompts on a sample of 100-1000 instances for each dataset.

SEA-IFEval

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalised by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).

SEA-MTBench

SEA-MTBench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-4.1-2025-04-14` as the judge model and compare against `gpt-4.1-2025-04-14` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction).

#### Metrics

The following metrics were used:

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
| Kalahi | Accuracy |
| SEA-IFEval | Accuracy |
| SEA-MTBench | Win rate against a reference |
| Toxicity Detection | Accuracy |


For details on Qwen-SEA-LION-v4-27B-IT performance, please refer to the SEA-HELM leaderboard, <https://leaderboard.sea-lion.ai/> .

## More Information

This is the repository for the commercial instruction-tuned model. The model has *not* been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

For more info, please contact us using this [sealion@aisingapore.org](mailto:sealion@aisingapore.org)


