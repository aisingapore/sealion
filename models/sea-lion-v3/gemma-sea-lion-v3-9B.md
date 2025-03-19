# Gemma-SEA-LION-v3-9B

## Introduction
Our Gemma-SEA-LION-v3-9B models have been continued pre-trained on top of the Gemma2 base model that is 9 billion parameters in size, and has a **context length of 8192**.

The training data for Gemma-SEA-LION-v3-9B comprises approximately **200B tokens** of Burmese, Chinese, English, Filipino, Indonesia, Khmer, Lao, Malay, Tamil, Thai and Vietnamese. The training data is sampled from the Dolma dataset, the original SEA-LION pretraining data, and Wiki sources for Burmese, Chinese, English, Filipino, Khmer, Lao, Malay, Indonesian, Tamil, Thai and Vietnamese. In addition, the training data for SFT for the Instruct model includes Javanese and Sudanese.

Gemma-SEA-LION-v3-9B benefits from the strong Gemma2 performance in Southeast Asian (SEA) languages, allowing it to significantly outperform its predecessors across SEA evaluation metrics, indicating improved language capabilities for the SEA region.

Due to its pre-training and fine-tuning data mix, Gemma-SEA-LION-v3-9B exhibits a boost in natural language reasoning (NLR) abilities in Indonesian, Tamil, Thai and Vietnamese, and achieves state-of-the-art performances in SEA instruction-following and multi-turn chat, while retaining Gemma2’s general abilities.

At a glance:
- **Model type:** Decoder
- **Tokenizer**: Default tokenizer used in Gemma2 9B
- **Training Data Size**: 200B tokens of SEA data
- **Context Length**: 8192 
- **Available Formats**:
  - Base (Gemma-SEA-LION-v3-9B)
  - Instruct (Gemma-SEA-LION-v3-9B-IT)
  - GGUF (Gemma-SEA-LION-v3-9B-IT-GGUF)
- **Supported Languages:** 
   1. Burmese
   2. Chinese
   3. English
   4. Filipino
   5. Indonesia
   6. Khmer
   7. Lao
   8. Malay
   8. Tamil
   9. Thai
   10. Vietnamese
- **License:**  [Gemma Community License](https://ai.google.dev/gemma/terms)


## Gemma-SEA-LION-v3-9B
### Training Infrastructure
Gemma-SEA-LION-v3-9B was trained using [MosaicML Composer](https://github.com/mosaicml/composer) on the following hardware:
| Training Details     | Gemma-SEA-LION-v3-9B |
|----------------------|:--------------------:|
| SingTel HGX-100      |          8 instances |
| Nvidia H100 80GB GPU |          64          |
| Training Duration    |          10 days     |

**Configuration**
| HyperParameter    | Gemma-SEA-LION-v3-9B |
|-------------------|:--------------------:|
| Precision         | bfloat16             |
| Optimizer         | decoupled_adamw      |
| Scheduler         | weight_stable_decay  |
| Learning Rate     | 1.0e-5               |
| Global Batch Size | 512                  |
| Micro Batch Size  | 1                    |

### Tokenizer

For tokenisation, the model employs the default tokenizer used in Gemma2 9B.

### Training Data
Gemma-SEA-LION-v3-9B base model was continued pre-trained on 200B tokens of the following data:

| Language                 | Source           | Total Tokens (B) | Percentage (%) | Total percentage (%) |
| ------------------------ | ---------------- | ---------------- | -------------- | -------------------- |
| Code                     | Stackv2          | 40               | 20             | 20                   |
| English                  | Dolma            | 37.5             | 18.75          | 25                   |
|                          | Fineweb-Edu      | 7.5              | 3.75           |
|                          | Others           | 5                | 2.5            |
| Chinese                  | SEA-LION Pile v1 | 12               | 6              | 13                   |
|                          | Others           | 14               | 7              |
| Vietnamese               | SEA-LION Pile v1 | 8.4              | 4.2            | 13                   |
|                          | VinBigData       | 16               | 8              |
|                          | Others           | 1.6              | 0.8            |
| Indonesian               | SEA-LION Pile v1 | 7                | 3.5            | 13                   |
|                          | SEA-LION Pile v2 | 7                | 3.5            |
|                          | Others           | 12               | 6              |
| Thai                     | SEA-LION Pile v1 | 10.7             | 5.35           | 10                   |
|                          | WangChanBERTa    | 8.5              | 4.25           |
|                          | Others           | 0.8              | 0.4            |
| Filipino - Malay - Tamil | SEA-LION Pile v1 | 4.28             | 2.14           | 3                    |
|                          | Others           | 1.72             | 0.86           |
| Khmer - Lao - Burmese    | SEA-LION Pile v1 | 5.2              | 2.6            | 3                    |
|                          | Others           | 0.8              | 0.4            |

Note: 
- All token counts are counted using Gemma2 9B tokenizer
- SEA-LION Pile v1 is processed from Common Crawl WET, which is published [here](https://huggingface.co/datasets/aisingapore/sea-lion-pile). The cutoff date of this version is September 2020.
- SEA-LION Pile v2 is processed from Common Crawl WARC from October 2020 to April 2024.
- Tamil news is sourced with permission from [Seithi](https://seithi.mediacorp.sg/)

### Benchmark Performance
We evaluated Gemma-SEA-LION-v3-9B base model on general language capabilities.

#### General Language Capabilities
For the evaluation of general language capabilities, we employed the [SEA-HELM](benchmarks/sea-helm.md) (also known as BHASA) evaluation benchmark across a variety of tasks.
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarization (Summ), Causal Reasoning (Causal) and Natural Language Inference (NLI).

Note: SEA-HELM is implemented using prompts to elicit answers in a strict format. For all tasks, the model is expected to provide an answer tag from which the answer is automatically extracted. For tasks where options are provided, the answer should comprise one of the pre-defined options. The scores for each task is normalised to account for baseline performance due to random chance.

The evaluation was done **five-shot** with native prompts on a sample of 100-1000 instances for each dataset.

For more details on Gemma-SEA-LION-v3-9B base benchmark performance, please refer to the SEA-HELM leaderboard, https://leaderboard.sea-lion.ai/

<br>

## Gemma-SEA-LION-v3-9B-IT

Gemma-SEA-LION-v3-9B-IT is a multilingual instruction-following model which has been fine-tuned with around **500,000 English instruction-completion pairs** alongside a larger pool of around **1,000,000 instruction-completion pairs** from other ASEAN languages, such as Indonesian, Thai and Vietnamese.

### Fine-Tuning Methodology
Gemma-SEA-LION-v3-9B-IT was built using a combination of a full parameter fine-tune, on-policy alignment, and model merges of the best performing checkpoints. The training process for fine-tuning was approximately 15 hours, with alignment taking 2 hours, both on 8x H100-80GB GPUs.

### Fine-Tuning Data
Gemma-SEA-LION-v3-9B-IT was trained on a wide range of synthetic instructions, alongside publicly available instructions hand-curated by the team with the assistance of native speakers. In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data source. 

#### Indonesian, Javanese & Sudanese Specific SEA-LION
Our partners at GoTo have continued pretrained and instruction tuned a variant of Gemma-SEA-LION-v3-9B, specifically enhancing its capabilities for Indonesian, Javanese, and Sundanese languages. Find the continued pretrained model at [Gemma2 9B CPT SahabatAIv1 Base](https://huggingface.co/GoToCompany/gemma2-9b-cpt-sahabatai-v1-base), and its corresponding instructioned tuned version at [Gemma2 9B CPT SahabatAIv1 Instruct](https://huggingface.co/GoToCompany/gemma2-9b-cpt-sahabatai-v1-instruct). 


### Benchmark Performance
We evaluated Gemma-SEA-LION-v3-9B-IT on both general language capabilities and instruction-following capabilities.

#### General Language Capabilities
For the evaluation of general language capabilities, we employed the [SEA-HELM](benchmarks/sea-helm.md) (also known as BHASA) evaluation benchmark across a variety of tasks.
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarization (Summ), Causal Reasoning (Causal) and Natural Language Inference (NLI).

Note: SEA-HELM is implemented using prompts to elicit answers in a strict format. For all tasks, the model is expected to provide an answer tag from which the answer is automatically extracted. For tasks where options are provided, the answer should comprise one of the pre-defined options. The scores for each task is normalised to account for baseline performance due to random chance.

The evaluation was done **zero-shot** with native prompts on a sample of 100-1000 instances for each dataset.

#### Instruction-following Capabilities
Since Gemma-SEA-LION-v3-9B-IT is an instruction-following model, we also evaluated it on instruction-following capabilities with two datasets, [IFEval](https://arxiv.org/abs/2311.07911) and [MT-Bench](https://arxiv.org/abs/2306.05685).

As these two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localize and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

**IFEval**

IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. Additionally, accuracy is normalized by the proportion of responses in the correct language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).


**MT-Bench**

MT-Bench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-4-1106-preview` as the judge model and compare against `gpt-3.5-turbo-0125` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction). A tie is given a score of 0.5.


For more details on Gemma-SEA-LION-v3-9B-IT benchmark performance, please refer to the SEA-HELM leaderboard, https://leaderboard.sea-lion.ai/

<br>

## Gemma-SEA-LION-v3-9B-IT-GGUF
The following quantized GGUF formats of our Gemma-SEA-LION-v3-9B-IT model are available:
- gemma2-9b-cpt-sea-lionv3-instruct-F16
- gemma2-9b-cpt-sea-lionv3-instruct-Q2_K
- gemma2-9b-cpt-sea-lionv3-instruct-Q3_K_M
- gemma2-9b-cpt-sea-lionv3-instruct-Q4_0
- gemma2-9b-cpt-sea-lionv3-instruct-Q4_K_M
- gemma2-9b-cpt-sea-lionv3-instruct-Q5_0
- gemma2-9b-cpt-sea-lionv3-instruct-Q5_K_M
- gemma2-9b-cpt-sea-lionv3-instruct-Q6_K
- gemma2-9b-cpt-sea-lionv3-instruct-Q8_0

Please refer to our [How To Download](#how-to-download) section for more details on how to access them.


## Download the Model(s)
Gemma-SEA-LION-v3-9B models are available for download via the following channels:

[HuggingFace SEA-LION v3 Collection](https://huggingface.co/collections/aisingapore/sea-lionv3-672589a39cdadd6a5b199581)


| Model                | Download   |
|----------------------|------------|
| gemma2-9b-cpt-sea-lionv3-base           | [HuggingFace](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-base), [Kaggle](https://www.kaggle.com/models/ai-singapore/gemma2-9b-cpt-sea-lionv3-base)      |
| gemma2-9b-cpt-sea-lionv3-instruct | [HuggingFace](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct), [Kaggle](https://www.kaggle.com/models/ai-singapore/gemma2-9b-cpt-sea-lionv3-instruct)      |
| gemma2-9b-cpt-sea-lionv3-instruct-gguf | [HuggingFace](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct-gguf), [Ollama](https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct)      |

<br>

## Usage 
**NOTE** This model has not been trained to use a system prompt or to use tool calling.

Gemma-SEA-LION-v3-9B-IT can be run using the 🤗 Transformers library 
```python
# Please use transformers==4.45.2

import transformers
import torch

model_id = "aisingapore/gemma2-9b-cpt-sea-lionv3-instruct"

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
2. Current SEA-LION models, including this commercially permissive release, have not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.


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

