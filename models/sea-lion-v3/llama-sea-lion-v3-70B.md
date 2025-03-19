# Llama-SEA-LION-v3-70B
## Introduction

Our Llama-SEA-LION-v3-70B models have been continued pre-trained on top of [Llama 3.1 70B Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) that is 70 billion parameters in size. Similar to our Llama-SEA-LION-v3-8B model, our Llama-SEA-LION-v3-70B also has a **context length of 128K tokens**, making them our SEA-LION models with the longest context length to date. 

Llama-SEA-LION-v3-70B was trained on data comprised of approximately **200B tokens** across 11 SEA languages: Burmese, Chinese, English, Filipino, Indonesia, Khmer, Lao, Malay, Tamil, Thai and Vietnamese.

Llama-SEA-LION-v3-70B-IT was fine-tuned in two stages on approximately **12.3M English instruction-completion pairs** alongside a pool of **4.5M Southeast Asian instruction-completion pairs** from SEA languages such as Indonesian, Javanese, Sundanese, Tamil, Thai and Vietnamese.

At a glance:
- **Model type:** Decoder
- **Tokenizer**: Default tokenizer used in Llama 3.1 70B Instruct
- **Available Formats**:
  - Base (llama3.1-70b-cpt-sea-lionv3-base)
  - Instruct (llama3.1-70b-cpt-sea-lionv3-instruct)
  - GGUF (llama3.1-70b-cpt-sea-lionv3-instruct-gguf)
- **Languages supported:** 
  1. Burmese
  2. Chinese
  3. English
  4. Filipino
  5. Indonesia
  6. Javanese (Instruct/GGUF only)
  7. Khmer
  8. Lao
  9. Malay
  10. Sundanese (Instruct/GGUF only)
  11. Tamil
  12. Thai
  13. Vietnamese
- **License:**  [Llama3.1 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE)


## Llama-SEA-LION-v3-70B
### Training Infrastructure
Llama-SEA-LION-v3-70B was trained in two stages using [MosaicML Composer](https://github.com/mosaicml/composer) on the following hardware:

|   Stage    | Training Details      | Llama-SEA-LION-v3-70B |
|------------|-----------------------|:---------------------------:|
|First Stage | AWS p5e.48xlarge      |        8 instances          |
|            | Nvidia H200 140GB GPU |        64                   |
|            | Training Duration     |        200 hrs (step 0 - 9000)           |
|Second Stage| SingTel HGX-100       |        16 instances          |
|            | Nvidia H100 80GB GPU  |        128                   |
|            | Training Duration     |        495 hrs (step 9000 - 47684)            |

### Configuration
| HyperParameter    | Llama-SEA-LION-v3-70B |
|-------------------|:------------------------:|
| Precision         | bfloat16                 |
| Optimizer         | decoupled_adamw          |
| Scheduler         | weight_stable_decay      |
| Learning Rate     | 1.0e-5                   |
| Global Batch Size | 512                      |

### Tokenizer
For tokenisation, the model employs the default tokenizer used in Llama 3.1 70B Instruct.

### Training Data
Llama-SEA-LION-v3-70B base model was continued pre-trained on 200B tokens of the following data:

| Language                 | Source                                 | Total Tokens (B) | Percentage (%) | Total percentage (%) |
| ------------------------ | -------------------------------------- | ---------------- | -------------- | -------------------- |
| Code                     | Stackv2                                | 40               | 20             | 20                   |
| English                  | Dolma                                  | 37.5             | 18.75          | 25                   |
|                          | Fineweb-Edu                            | 7.5              | 3.75           |
|                          | Others                                 | 5                | 2.5            |
| Chinese                  | SEA-LION Pile v1                       | 12               | 6              | 13                   |
|                          | Others                                 | 14               | 7              |
| Vietnamese               | SEA-LION Pile v1                       | 8.4              | 4.2            | 13                   |
|                          | VinBigData                             | 16               | 8              |
|                          | Others                                 | 1.6              | 0.8            |
| Indonesian               | SEA-LION Pile v1                       | 7                | 3.5            | 13                   |
|                          | SEA-LION Pile v2                       | 7                | 3.5            |
|                          | Others                                 | 12               | 6              |
| Thai                     | SEA-LION Pile v1                       | 10.7             | 5.35           | 10                   |
|                          | WangChanBERTa                          | 8.5              | 4.25           |
|                          | Others                                 | 0.8              | 0.4            |
| Filipino - Malay - Tamil | SEA-LION Pile v1, AI4Bharat Sangraha   | 4.28             | 2.14           | 3                    |
|                          | Others                                 | 1.72             | 0.86           |
| Khmer - Lao - Burmese    | SEA-LION Pile v1                       | 5.2              | 2.6            | 3                    |
|                          | Others                                 | 0.8              | 0.4            |

Note: 
- All token counts are counted using Llama 3.1 70B Instruct tokenizer
- SEA-LION Pile v1 is processed from Common Crawl WET, which is published [here](https://huggingface.co/datasets/aisingapore/sea-lion-pile). The cutoff date of this version is September 2020.
- SEA-LION Pile v2 is processed from Common Crawl WARC from October 2020 to April 2024.
- Tamil data from Sangraha is published [here](https://huggingface.co/datasets/ai4bharat/sangraha). The paper can be found [here](https://arxiv.org/abs/2403.06350).
- Tamil news is sourced with permission from [Seithi](https://seithi.mediacorp.sg/)

### Benchmark Performance
We evaluated Llama-SEA-LION-v3-70B base model on general language capabilities and constraint-following behaviour.

#### General Language Capabilities and Constraint-following Behaviour
For the evaluation of general language capabilities, we employed the [SEA-HELM](benchmarks/sea-helm.md) (also known as BHASA) evaluation benchmark across a variety of tasks.
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarisation (Abssum), Causal Reasoning (Causal) and Natural Language Inference (NLI).

Note: SEA-HELM is implemented using prompts to elicit answers in a strict format. For all tasks, the model is expected to provide an answer tag from which the answer is automatically extracted. For tasks where options are provided, the answer should comprise one of the pre-defined options. The scores for each task is normalised to account for baseline performance due to random chance.

The evaluation was done **five-shot** with native prompts on a sample of 100-1000 instances for each dataset.

Following the implementation of IFEval in OpenLLM leaderboard, we also implement SEA-IFEval to provide a comparison of the ability of the model to follow specific constraints in English and in SEA languages.

**SEA-IFEval**

Based on [IFEval](https://arxiv.org/abs/2311.07911), the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalised by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).

For more details on Llama-SEA-LION-v3-70B base benchmark performance, please refer to the SEA-HELM leaderboard, https://leaderboard.sea-lion.ai/.


## Llama-SEA-LION-v3-70B-IT
### Fine-Tuning Methodology
Llama-SEA-LION-v3-70B-IT was tuned using a combination of a full parameter fine-tune, on-policy alignment, and model merges of the best performing checkpoints. The training process for fine-tuning was approximately 3200 GPU hours, on a single node of 8x H100-80GB GPUs.

### Fine-Tuning Data
Llama-SEA-LION-v3-70B-IT was trained on a wide range of synthetic instructions, alongside publicly available instructions hand-curated by the team with the assistance of native speakers. In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data sources.

### Benchmark Performance
We evaluated Llama-SEA-LION-v3-70B-IT on both general language capabilities and instruction-following capabilities.

#### General Language Capabilities
For the evaluation of general language capabilities, we employed the [SEA-HELM](benchmarks/sea-helm.md) (also known as BHASA) evaluation benchmark across a variety of tasks.
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarisation (Abssum), Causal Reasoning (Causal) and Natural Language Inference (NLI).

Note: SEA-HELM is implemented using prompts to elicit answers in a strict format. For all tasks, the model is expected to provide an answer tag from which the answer is automatically extracted. For tasks where options are provided, the answer should comprise one of the pre-defined options. The scores for each task is normalised to account for baseline performance due to random chance.

The evaluation was done **zero-shot** with native prompts on a sample of 100-1000 instances for each dataset.

#### Instruction-following Capabilities
Since Llama-SEA-LION-v3-70B-IT is an instruction-following model, we also evaluated it on instruction-following capabilities with two datasets, SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)).

As these two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

**SEA-IFEval**

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalised by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).


**SEA-MTBench**

SEA-MTBench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-4-1106-preview` as the judge model and compare against `gpt-3.5-turbo-0125` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction). A tie is given a score of 0.5.


For more details on Llama-SEA-LION-v3-70B-IT benchmark performance, please refer to the SEA-HELM leaderboard, https://leaderboard.sea-lion.ai/.

## Llama-SEA-LION-v3-70B-IT-GGUF
The following quantized GGUF formats of our Llama-SEA-LION-v3-70B-IT model are available:
- llama3.1-70B-cpt-sea-lionv3-instruct-F16
- llama3.1-70B-cpt-sea-lionv3-instruct-Q2_K
- llama3.1-70B-cpt-sea-lionv3-instruct-Q3_K_M
- llama3.1-70B-cpt-sea-lionv3-instruct-Q4_0
- llama3.1-70B-cpt-sea-lionv3-instruct-Q4_K_M
- llama3.1-70B-cpt-sea-lionv3-instruct-Q5_0
- llama3.1-70B-cpt-sea-lionv3-instruct-Q5_K_M
- llama3.1-70B-cpt-sea-lionv3-instruct-Q6_K
- llama3.1-70B-cpt-sea-lionv3-instruct-Q8_0

Please refer to our [How To Download](#how-to-download) section for more details on how to access them.

<br>

## Download the Model(s)
Llama-SEA-LION-v3-70B models are available for download via the following channels:

[HuggingFace SEA-LION v3 Collection](https://huggingface.co/collections/aisingapore/sea-lionv3-672589a39cdadd6a5b199581)


| Model                | Download   |
|----------------------|------------|
| llama3.1-70b-cpt-sea-lionv3-base           | [HuggingFace](https://huggingface.co/aisingapore/llama3.1-70b-cpt-sea-lionv3-base)      |
| llama3.1-70b-cpt-sea-lionv3-instruct | [HuggingFace](https://huggingface.co/aisingapore/llama3.1-70b-cpt-sea-lionv3-instruct)      |
| llama3.1-70b-cpt-sea-lionv3-instruct-gguf | [HuggingFace](https://huggingface.co/aisingapore/llama3.1-70b-cpt-sea-lionv3-instruct-gguf), [Ollama](https://ollama.com/aisingapore/llama3.1-70b-cpt-sea-lionv3-instruct)      |

<br>

## Usage 
Llama-SEA-LION-v3-70B-IT can be run using the 🤗 Transformers library 
```python
import transformers
import torch

model_id = "aisingapore/llama3.1-70B-cpt-sea-lionv3-instruct"

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

## Disclaimer

It is important for users to be aware that our models exhibits certain limitations that warrant consideration:
1. The model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies in its reasoning. 
2. The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

<br>

## References
### Thai Pre-Training Data Reference

```bibtex
@misc{lowphansirikul2021wangchanberta,
    title={WangchanBERTa: Pretraining transformer-based Thai Language Models},
    author={Lalita Lowphansirikul and Charin Polpanumas and Nawat Jantrakulchai and Sarana Nutanong},
    year={2021},
    eprint={2101.09635},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
