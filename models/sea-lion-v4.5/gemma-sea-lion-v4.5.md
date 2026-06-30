# Gemma-SEA-LION-v4.5-E2B-IT

_Last update: 2026-05-19_

SEA-LION is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

**Gemma-SEA-LION-v4.5-E2B-IT** built upon the gemma-4-E2B-it architecture with 2.3B effective (5.1B with embeddings). To ensure deep domain adaptation, the model underwent distillation from google/gemma-4-31B-it on an updated aisingapore/SEA-Instruct-2602, instilling multilingual and multicultural fluency across English and key SEA languages: Burmese, Indonesian, Filipino (Tagalog), Malay, Tamil, Thai, and Vietnamese.

Gemma-SEA-LION-v4.5-E2B-IT inherits the following features from Gemma 4:

- **Native System Prompt Support** – Gemma 4 introduces native support for the `system` role, enabling more structured and controllable conversations.
- **Reasoning** – Highly capable reasoning model, with configurable thinking modes.
- **Extended Multimodalities** – Processes Text, Image with variable aspect ratio and resolution support (all models), Video, and Audio (featured natively).
- **Optimized for On-Device** – designed for efficient local execution on laptops and mobile devices.
- **Enhanced Coding & Agentic Capabilities** – Achieves notable improvements in coding benchmarks alongside native function-calling support, powering highly capable autonomous agents.

## Model Details

### Model Description

SEA-LION stands for Southeast Asian Languages In One Network.

We performed post-training in English and SEA languages on `gemma-4-E2B-it`, a multimodal learning model using the Gemma 4 architecture, to create Gemma-SEA-LION-v4.5-E2B-IT.

For tokenization, the model employs the default tokenizer used in `gemma-4-E2B-it`.

- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Transformer Decoder with Vision and Audio Encoder
- **Training Stage:** Post-Training (Logit Distillation & Model Merging)
- **Context length:** 128k
- **Language(s):** fine-tuned on Burmese, Indonesian, Filipino, Malay, Tamil, Thai, and Vietnamese
- **License:** [Apache-2.0](https://ai.google.dev/gemma/apache_2)
- **Finetuned from model:** <https://huggingface.co/google/gemma-4-E4B-it>

### Model Sources

- **Repository:** [SEA-LION v4.5 - an aisingapore Collection](https://huggingface.co/collections/aisingapore/sea-lion-v45)

## How to Get Started with the Model

### Download the Models

Gemma-SEA-LION-v4.5-E2B-IT models are available for download via the following channels:
🤗[HuggingFace SEA-LION v4.5 Collection](<(https://huggingface.co/collections/aisingapore/sea-lion-v45)>)

| Model                           | Download                                                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gemma-SEA-LION-v4.5-E2B-IT      | [HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4.5-E2B-IT), [Ollama](https://ollama.com/aisingapore/Gemma-SEA-LION-v4.5-E2B-IT)      |
| Gemma-SEA-LION-v4.5-E2B-IT-GGUF | [HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4.5-E2B-IT-GGUF), [Ollama](https://ollama.com/aisingapore/Gemma-SEA-LION-v4.5-E2B-IT) |

Use the code below to get started with the model with 🤗 Transformers libraries.

```
pip install -U transformers torch accelerate
```

```
from transformers import AutoProcessor, AutoModelForCausalLM
MODEL_ID = "aisingapore/Gemma-SEA-LION-v4.5-E2B-IT"
# Load model
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype="auto",
    device_map="auto"
)
# Prompt
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a short joke about HDB flat in Singapore."},
]
# Process input
text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)
inputs = processor(text=text, return_tensors="pt").to(model.device)
input_len = inputs["input_ids"].shape[-1]
# Generate output
outputs = model.generate(**inputs, max_new_tokens=1024)
response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)
# Parse output
processor.parse_response(response)
```

## Training Details

The instruction fine-tuning text dataset comprises a collection of OSS & synthetic data, including approximately 8.54 million instruction-text pairs and advanced tool-calling instruction pairs specifically curated for the region.

### Training Data

🤗[aisingapore/SEA-Instruct-2602](https://huggingface.co/datasets/aisingapore/SEA-Instruct-2602)

### Training Regime

To maintain high efficiency, our post-training pipeline is centred entirely on knowledge distillation.

## Evaluation

### Testing Data, Factors & Metrics

We evaluated Gemma-SEA-LION-v4.5-E2B-IT on general language, multi-turn chat, instruction-following capabilities, and vision-language benchmarks.

#### Testing Data

**General language capabilities**

For the evaluation of general language capabilities, we employed the [SEA-HELM evaluation benchmark](https://arxiv.org/abs/2502.14301) across a variety of tasks. These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarisation (Abssum), Causal Reasoning (Causal), Natural Language Inference (NLI), Linguistic Diagnostics (LINDSEA), Cultural Knowledge (Kalahi) and Global MMLU Lite/Thai Exam.

**Instruction-following and Multi-turn Chat**

We evaluated the models on Instruction-following and Multi-turn Chat capabilities with SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)) respectively. The two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

#### Factors

All evaluations were run with the model specific generation parameters defined in the model config. Each evaluation comprised of 8 runs with different seeds and the final results were averaged across these runs.

For all tasks, the model was expected to provide an answer tag from which the answer was automatically extracted. For tasks where options were provided, the answer should comprise one of the pre-defined options.

The evaluation was done **zero-shot** with native prompts on a sample of 100-1000 instances for each dataset.

- **SEA-IFEval:** Evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalised by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).
- **SEA-MTBench:** Evaluates a model's ability to engage in Multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-oss-120b` as the judge model and compare against `gpt-oss-120b` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction).

#### Metrics

The following metrics were used for text capabilities:

| **Task**                       | **Metric**                        |
| ------------------------------ | --------------------------------- |
| Sentiment Analysis             | Accuracy                          |
| Extractive QA (ID, VI, TH, TA) | ChrF++                            |
| MCQ-QA (TL, MY, MS)            | Accuracy                          |
| Metaphor                       | Accuracy                          |
| Abstractive Summarisation      | Rouge-L                           |
| Translations                   | MetricX-24 score (with reference) |
| Causal Reasoning               | Accuracy                          |
| Natural Language Inference     | Accuracy                          |
| LINDSEA                        | Accuracy                          |
| Global MMLU Lite               | Accuracy                          |
| ThaiExam                       | Accuracy                          |
| Kalahi                         | Accuracy                          |
| SEA-IFEval                     | Accuracy                          |
| SEA-MTBench                    | Win rate against a reference      |

#### Results

<!--![LeaderboardResults!](Gemma-SEA-LION-v4.5-E2B-IT_SEA-HELM_scores.png "LeaderboardCaptured20May")-->

For details on Gemma-SEA-LION-v4.5-E2B-IT performance, please refer to the <https://leaderboard.sea-lion.ai/>.

## Technical Specifications

### Model Architecture

The architecture is based on the dense model architecture of Gemma4 E2B, can be found in the [gemma-4-E2B-it Model Card](https://huggingface.co/google/gemma-4-E2B-it#dense-models).

## Uses

### Out-of-Scope Use

The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

### Bias, Risks, and Limitations

The model was not tested for robustness against adversarial prompting. It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies.
