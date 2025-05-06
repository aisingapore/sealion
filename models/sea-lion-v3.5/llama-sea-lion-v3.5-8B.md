# Llama-SEA-LION-v3.5-8B
## Introduction
Llama-SEA-LION-v3.5-8B-R is a hybrid model offering versatile functionality, handling both complex reasoning tasks and general text generation, with mode selection managed through the tokenizer's chat template.

We performed instruction tuning in English and also in SEA languages such as Filipino, Indonesian, Tamil, Thai and Vietnamese on our [continued pre-trained Llama-SEA-LION-v3-8B-IT](../sea-lion-v3/llama-sea-lion-v3-8B.md), a decoder model using the Llama 3.1 architecture, to create Llama-SEA-LION-v3.5-8B-R. 

By leveraging on SEA-LION v3’s strong foundation, Llama-SEA-LION-v3.5-8B-R ensures broader accessibility and usability, empowering diverse communities and use cases throughout the region. It is particularly suited for cost-efficient, low-latency applications where regional language support and advanced reasoning is critical.

For tokenisation, the model employs the default tokenizer used in Llama 3.1 70B Instruct. The model has a context length of 128k.


At a glance:
- **Model type:** Decoder
- **Tokenizer**: Default tokenizer used in Llama 3.1 8B Instruct
- **Context Length**: 128K 
- **Available Formats**:
  - Reasoning (Llama-SEA-LION-v3.5-8B-R)
  - GGUF (Llama-SEA-LION-v3.5-8B-R-GGUF)
- **Supported Languages:** 
  1. Burmese
  2. Chinese
  3. English
  4. Filipino
  5. Indonesia
  6. Javanese
  7. Khmer
  8. Lao
  9. Malay
  10. Sundanese
  11. Tamil
  12. Thai
  13. Vietnamese
- **License:**  [Llama3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct/blob/main/LICENSE)


## Llama-SEA-LION-v3.5-8B-R

### Post-Training

Llama-SEA-LION-v3.5-8B-R was trained with an additional series of supervised fine-tuning atop our existing Llama-SEA-LION-v3-8B-IT models across multiple stages, culminating in a final tune with distilled reasoning data of **1.5M** traces from Deepseek-R1 across multiple SEA languages such as Indonesian Tamil, Thai, Tagalog and Vietnamese.

A distinctive feature of Llama-SEA-LION-v3.5-8B-R is its dynamic reasoning toggle. By default, the model operates in a detailed reasoning mode, thoughtfully guiding users through step-by-step solutions. Users retain full control, easily switching reasoning mode off using customizable chat template configurations, allowing concise interactions suitable for straightforward queries. During the tuning process, reasoning and non-reasoning data were simultaneously incorporated, resulting in a versatile model adaptable to varied user needs.

We also scaled up our instruction set to **30M** instructions (across a training time of a month on a single node for the 70B), incorporating the latest in open-source alongside multiple rounds of synthetic aggregation and rewrite, improving the quality of its responses and leaning the model towards accounting for our region's unique cultural diversity and history. It comprises a mix of curated publicly available open source data, synthetic generations from stronger models and handwritten instructions centered around Southeast Asian culture (particularly from Project SEALD), general multilingual instruction-following and chat prompt-response pairs.

Llama-SEA-LION-v3.5-8B-R training uniquely emphasizes region-specific data aggregation and synthetic instruction generation, undergoing multiple refinement cycles and model merging to enhance multilingual proficiency and reasoning capabilities, ensuring exceptional performance across both complex and general-purpose tasks. This ensures that Llama-SEA-LION-v3.5-8B-R maintains its superior performance while mitigating issues like catastrophic forgetting.

### Benchmark Performance

We evaluated Llama-SEA-LION-v3.5-8B-R on both general language capabilities and instruction-following capabilities.

#### General Language Capabilities
For the evaluation of general language capabilities, we employed the [SEA-HELM (also known as BHASA) evaluation benchmark](https://arxiv.org/abs/2309.06085v2) across a variety of tasks.
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarisation (Abssum), Causal Reasoning (Causal), Natural Language Inference (NLI), and linguistic diagnostics (LINDSEA).

Note: SEA-HELM is implemented using prompts to elicit answers in a strict format. For all tasks, the model is expected to provide an answer tag from which the answer is automatically extracted. For tasks where options are provided, the answer should comprise one of the pre-defined options. The scores for each task is normalised to account for baseline performance due to random chance.

The evaluation was done **zero-shot** with native prompts on a sample of 100-1000 instances for each dataset.

#### Instruction-following Capabilities
Since Llama-SEA-LION-v3.5-8B-R is an instruction-following model, we also evaluated it on instruction-following capabilities with two datasets, SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)).

As these two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

**SEA-IFEval**

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalised by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).

**SEA-MTBench**

SEA-MTBench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-4-1106-preview` as the judge model and compare against `gpt-3.5-turbo-0125` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction). A tie is given a score of 0.5.

For more details on Llama-SEA-LION-v3.5-8B-R benchmark performance, please refer to the [SEA-HELM leaderboard](https://leaderboard.sea-lion.ai/).

<br>

## Llama-SEA-LION-v3.5-8B-R-GGUF

The following quantized GGUF formats of our Llama-SEA-LION-v3.5-8B-R model are available:
- Llama-SEA-LION-v3.5-8B-R-F16
- Llama-SEA-LION-v3.5-8B-R-Q2_K
- Llama-SEA-LION-v3.5-8B-R-Q3_K_M
- Llama-SEA-LION-v3.5-8B-R-Q4_0
- Llama-SEA-LION-v3.5-8B-R-Q4_K_M
- Llama-SEA-LION-v3.5-8B-R-Q5_0
- Llama-SEA-LION-v3.5-8B-R-Q5_K_M
- Llama-SEA-LION-v3.5-8B-R-Q6_K
- Llama-SEA-LION-v3.5-8B-R-Q8_0

Please refer to our [Download the Model(s)](#download-the-model-s) section for more details on how to access them.

<br>

## Download the Model(s)
Llama-SEA-LION-v3.5-8B-R models are available for download via the following channels:

[HuggingFace SEA-LION v3.5 Collection](https://huggingface.co/collections/aisingapore/sea-lion-v35-67fc3ab84300d7e6088fa32c)


| Model                | Download   |
|----------------------|------------|
| Llama-SEA-LION-v3.5-8B-R           | [HuggingFace](https://huggingface.co/aisingapore/Llama-SEA-LION-v3.5-8B-R)      |
| Llama-SEA-LION-v3.5-8B-R-GGUF | [HuggingFace](https://huggingface.co/aisingapore/Llama-SEA-LION-v3.5-8B-R-GGUF), [Ollama](https://ollama.com/aisingapore/Llama-SEA-LION-v3.5-8B-R) |

<br>

## Usage 
Llama-SEA-LION-v3.5-8B-R can be run using the 🤗 Transformers library 
```python
import transformers
import torch

model_id = "aisingapore/Llama-SEA-LION-v3.5-8B-R"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)
messages = [
    {"role": "user", "content": "Apa sentimen dari kalimat berikut ini?\nKalimat: Buku ini sangat membosankan.\nJawaban: "},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])
```

### Thinking Mode Toggle
Llama-SEA-LION-v3.5-8B-R defaults to reasoning with `thinking_mode="on"` passed to the chat template. To use non-thinking mode ie. standard generations, pass `thinking_mode="off"` to the chat template instead.
```python
import transformers
import torch

model_id = "aisingapore/Llama-SEA-LION-v3.5-70B-R"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

tokenizer = pipeline.tokenizer

messages = [
    {"role": "user", "content": "Apa sentimen dari kalimat berikut ini?\nKalimat: Buku ini sangat membosankan.\nJawaban: "},
]

prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False, thinking_mode="off")

outputs = pipeline(
    prompt,
    max_new_tokens=256,
)

print(outputs[0]["generated_text"])
```

## Disclaimer

It is important for users to be aware that our models exhibits certain limitations that warrant consideration:
1. The model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies in its reasoning. 
2. The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.


