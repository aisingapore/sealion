---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
Gemma-SEA-LION-v4-27B (Both Model for Github) Last updated: 2025-08-25 
---

# Gemma-SEA-LION-v4-27B

Last updated: 2025-08-25


**SEA-LION** is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region.

<!-- Introduction -->
## Introduction
SEA-LION stands for *Southeast Asian Languages In One Network*. 

Gemma-SEA-LION-v4-27B is based on Gemma 3 (which supports over 100 languages) and is a multilingual model that
has undergone continued pre-training on approximately **500B tokens**, sampled from a pool of 1 trillion tokens across 11 SEA languages: Burmese, English, Indonesia, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese, 
to create *Gemma-SEA-LION-v4-27B*. Subsequently, we performed post-training on 
Gemma-SEA-LION-v4-27B using multiple RL algorithms to produce *Gemma-SEA-LION-v4-27B-IT*.

Gemma-SEA-LION-v4-27B inherits Gemma 3’s: 

- Large 128K context length 

- Image and text understanding capabilities, including document comprehension, visual Q&A, and image-grounded reasoning

- Advanced function calling and structured outputs to allow for seamless integration into larger systems

For tokenization, the model employs the default tokenizer used in Gemma 3 27B IT.

At a glance:

- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k 
- **Language(s):**  Burmese, English, Indonesia, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese
- **License:** [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- **Continued pretrained and finetuned from model:** [Gemma-3-27B-IT](https://huggingface.co/google/gemma-3-27b-it)

As of 25 Aug 2025, Gemma-SEA-LION-v4-27B-IT excels at Southeast Asian (SEA) tasks when compared to other open models with fewer than 200 billion parameters and demonstrates performance comparable to that of larger and top closed models. For detailed rankings, please refer to the [leaderboard](https://leaderboard.sea-lion.ai/).

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

The dataset comprises Burmese, English, Indonesia, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese languages, collected from a mixture of sources including web data, code, open-source datasets, and synthetically generated datasets, amounting to a total of 500 billion tokens.

The 500 billion tokens are sampled from a much larger pool of 1 trillion tokens from open-sourced datasets with the optimal datamix shown below determined by our experiments.


| Language                         | Dataset Name             | Total Tokens (B) | Percentage (%) | Total percentage (%) |
|-----------------------------------|-------------------------|------------------|----------------|---------------------|
| Code                              | StarCoder (OLMo 2 Version) | 50B             | 10             | 10                  |
| EN                                | Fineweb-Edu             | 80B              | 16             | 40                  |
|                                  | DCLM-OLMo2-HQ           | 80B              | 16             |                     |
|                                  | Non-CC-EN               | 40B              | 8              |                     |
| ZH                                | SEA-LION Pile v1        | 13.5B            | 2.7            | 9                   |
|                                  | Fineweb2                | 13.5B            | 2.7            |                     |
|                                  | Fineweb2-HQ             | 4.5B             | 0.9            |                     |
| VI                                | SEA-LION Pile v1        | 4.25B            | 0.85           | 8.5                 |
|                                  | SEA-LION Pile v2        | 12.75B           | 2.55           |                     |
|                                  | Fineweb2                | 8.5B             | 1.7            |                     |
|                                  | Non-CC-VI               | 17B              | 3.4            |                     |
| ID                                | SEA-LION Pile v1        | 5.66B            | 1.13           | 8.5                 |
|                                  | SEA-LION Pile v2        | 17B              | 3.4            |                     |
|                                  | Fineweb2                | 11.33B           | 2.27           |                     |
|                                  | Non-CC-ID               | 8.5B             | 1.7            |                     |
| TH                                | SEA-LION Pile v1        | 3.035B           | 0.61           | 8.5                 |
|                                  | SEA-LION Pile v2        | 9.107B           | 1.82           |                     |
|                                  | Fineweb2                | 3.035B           | 0.61           |                     |
|                                  | WangChanBERTa           | 3.035B           | 0.61           |                     |
|                                  | Dolmav1                 | 3.035B           | 0.61           |                     |
|                                  | Non-CC-TH               | 21.25B           | 4.25           |                     |
| TL, TA, MS, KM, LO and MY         | ALL_LANG                | 77.5B            | 15.5           | 15.5                |



Note:

- All token counts are counted using Gemma 3 tokenizer.

- Pre-training was conducted with batches of 8k token lengths.

- SEA-Pile v1 is processed from Common Crawl WET, which is published [here](https://huggingface.co/datasets/aisingapore/sea-lion-pile). 
The main proportion is from mC4 dataset (corpus [link](https://huggingface.co/datasets/bertin-project/mc4-sampling)). 
The cutoff date of this version is September 2020.

- SEA-Pile v2 is processed from Common Crawl WARC from October 2020 to April 2024.

- Tamil news is sourced with permission from [Seithi](https://seithi.mediacorp.sg/)

- We utilized 0.5% of synthetically generated datasets for the low-resource language, Khmer.


### Training Procedure

**Training regime:** 

| Hyperparameter    | Gemma-SEA-LION-v4-27B |
|-------------------|-----------------------|
| Precision         | bfloat16              |
| Optimizer         | decoupled_adamw       |
| Scheduler         | CosineAnnealing       |
| Learning Rate     | 4.00E-08              |
| Global Batch Size | 1024                  |


Gemma-SEA-LION-v4-27B has undergone post-training using a QA pairs dataset in Burmese, English, Indonesia, Khmer, Lao, Malay, Tagalog, Tamil, Thai and Vietnamese, comprising approximately 10M samples in total, to create *Gemma-SEA-LION-v4-27B-IT*.

The instruction fine-tuning dataset combines our SEA-Instruct, Infinity-Instruct, and OpenMath-Instruct 2 with open-source datasets. For the Online RL datasets, open sourced datasets such as nvidia/Llama-Nemotron-Post-Training-Dataset (RL set) and zwhe99/DeepMath-103K were used. For alignment, rejected-chosen pairs are generated from the target model, with the chosen responses obtained by rewriting and improving upon the rejected outputs. Prompt sampling is guided by a gradient-based analysis process.

Our post-training workflow consists of multiple stages: instruction fine-tuning, model merging, online RL for both instruction following and math using DRGPPO, and then followed by on-policy alignment via APO.


## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->
We evaluated Gemma-SEA-LION-v4-27B models on both general language capabilities and instruction-following capabilites. 
### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

We evaluated Gemma-SEA-LION-v4-27B models on both general language capabilities and instruction-following capabilites.

General language capabilities

For the evaluation of general language capabilities, we employed the [SEA-HELM evaluation benchmark](https://arxiv.org/abs/2502.14301) across a variety of tasks. 
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), 
Abstractive Summarisation (Abssum), Causal Reasoning (Causal), Natural Language Inference (NLI), Linguistic Diagnostics (LINDSEA), Cultural Knowledge (Kalahi) and Global MMLU Lite.

Instruction-following and Multi-turn Chat

We evaluated the models on instruction-following and multi-turn chat capabilities with SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)) respectively. 
The two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.


#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

All evaluations were run with the model specific generation parameters defined in the model config. Each evaluation comprised of 8 runs with different seeds and the final results were averaged across these runs.

For all tasks, the model was expected to provide an answer tag from which the answer was automatically extracted. For tasks where options were provided, the answer should comprise one of the pre-defined options.

The evaluation was done zero-shot with native prompts on a sample of 100-1000 instances for each dataset. 

SEA-IFEval

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, 
for example beginning a response with a specific word/phrase or answering with a certain number of sections. 
Additionally, accuracy is normalised by the proportion of responses in the correct language 
(if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).

SEA-MTBench

SEA-MTBench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. 
We use `gpt-4.1-2025-04-14` as the judge model and compare against `gpt-4.1-2025-04-14` as the baseline model. 
The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: 
Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction).


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

The following metrics were used:
| Task                                | Metric                                 |
|--------------------------------------|----------------------------------------|
| Sentiment Analysis                   | Accuracy                               |
| Extractive QA (ID, VI, TH, TA)       | ChrF++                                 |
| MCQ-QA (TL, MY, MS)                  | Accuracy                               |
| Metaphor                             | Accuracy                               |
| Abstractive Summarisation            | Rouge-L                                |
| Translations                         | MetricX-24 score (with reference)      |
| Causal Reasoning                     | Accuracy                               |
| Natural Language Inference           | Accuracy                               |
| LINDSEA                              | Accuracy                               |
| Global MMLU Lite                     | Accuracy                               |
| Kalahi                               | Accuracy                               |
| SEA-IFEval                           | Accuracy                               |
| SEA-MTBench                          | Win rate against a reference           |
| Toxicity Detection                   | Accuracy                               |


### Results

For details on Gemma-SEA-LION-v4-27B model performances, please refer to the SEA-HELM leaderboard, [Leaderboard results on SEA-HELM](https://leaderboard.sea-lion.ai/).



## Gemma-SEA-LION-v4-27B-IT Quantized Version
The following quantized versions of our Gemma-SEA-LION-v4-27B-IT model are available:

- Gemma-SEA-LION-v4-27B-IT-Q4_K_M
- Gemma-SEA-LION-v4-27B-IT-Q8_0
- Gemma-SEA-LION-v4-27B-IT-BF16
- Gemma-SEA-LION-v4-27B-IT-NVFP4
- Gemma-SEA-LION-v4-27B-IT-FP8-Dynamic


Please refer to our [Download the Models](#download-the-models) section for more details on how to access them.

## How to Get Started with the Model

## Download the Models

Gemma-SEA-LION-v4-27B models are available for download via the following channels:
🤗[HuggingFace SEA-LION v4 Collection]((https://huggingface.co/collections/aisingapore/sea-lion-v4-68aa7bb8061d497a4f9f2fec))

|Model	                        |Download                                                      |
|-------------------------------|--------------------------------------------------------------|
|Gemma-SEA-LION-v4-27B	        |[HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B)|
|Gemma-SEA-LION-v4-27B-IT	|[HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT) |
|Gemma-SEA-LION-v4-27B-IT-GGUF	|[HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT-GGUF), [Ollama](https://ollama.com/aisingapore/Gemma-SEA-LION-v4-27B-IT) |
|Gemma-SEA-LION-v4-27B-IT-NVFP4	|[HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT-NVFP4) |
|Gemma-SEA-LION-v4-27B-IT-FP8-Dynamic	|[HuggingFace](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-IT-27B-FP8-Dynamic) |

## Usage

Use the code below to get started with the model using the 🤗 Transformers library.
```python
from transformers import pipeline
import torch

pipe = pipeline(
    "text-generation",
    model="aisingapore/Gemma-SEA-LION-v4-27B-IT",
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
            {"type": "text", "text": "Write a poem on southeast asian countries in Indonesian."}
        ]
    }
]

output = pipe(text=messages, max_new_tokens=200)
print(output[0]["generated_text"][-1]["content"])
```


## Disclaimer

The models have not been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.


### Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

*The models were not tested for robustness against adversarial prompting.* It is important for users to be aware that our models exhibit certain limitations that warrant consideration. 
Like many LLMs, the models can hallucinate and occasionally generates irrelevant content, 
introducing fictional elements that are not grounded in the provided context. 
Users should also exercise caution in interpreting and validating the model's responses 
due to the potential inconsistencies.

**Limitations**

In terms of vision capability, Gemma-SEA-LION-v4-27B has been trained and fine-tuned exclusively on the text back-end.
As a result, its vision capabilities are expected to be comparable to those of Gemma 3 IT 27B, 
and may not exhibit significant improvements or differences in this area. [🤗 google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it )



## More Information

This is the repository for the commercial instruction-tuned model. 
The models have *not* been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable 
for any claims, damages, or other liabilities arising from the use of the released weights and codes.

For more info, please contact us at [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6) or sealion@aisingapore.org
