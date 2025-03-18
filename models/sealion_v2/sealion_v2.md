# SEA-LION V2
## Introduction
SEA-LION version 2, released in July 2024, has been continued-pretrained on top of the [Meta-Llama-3-8B-Instruct model](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) that is 8 billion parameters in size, with **context length of 8192 tokens**.

Using continued-pretraining let us leverage the powerful capabilities of the Llama3 base model and build a stronger model with far fewer resources than pre-training from scratch. Compared to the 980B tokens used in for SEA-LION V1, approximately **48B** tokens across 5 SEA languages (English, Indonesia, Tamil, Thai and Vietnamese) was used for the continued pre-training of SEA-LION V2. 

At a glance:
- **Model type:** Decoder
- **Tokenizer**: Default tokenizer used in Llama 3 8B Instruct
- **Training Data Size**: 48B tokens of SEA data
- **Context Length**: 8192 
- **Available Formats**:
  - Base (llama3-8b-cpt-sea-lionv2-base)
  - Instruct (llama3-8b-cpt-sea-lionv2.1-instruct)
  - GGUF (llama3-8b-cpt-sea-lionv2.1-instruct-gguf)
- **Supported Languages:** 
   1. English 
   2. Indonesian 
   3. Thai
   4. Vietnamese
   5. Tamil
- **License:**  [Llama3 Community License](https://huggingface.co/meta-llama/Meta-Llama-3-8B/blob/main/LICENSE)


## Llama3 8B CPT SEA-LIONv2 Base
### Training Infrastructure
Llama3 8B CPT SEA-LIONv2 Base was trained using [MosaicML Composer](https://github.com/mosaicml/composer) on the following hardware:

| Training Details     | Llama3 8B CPT SEA-LIONv2 Base |
|----------------------|:--------------------:|
| AWS EC2 p5d.24xlarge |          8 instances |
| Nvidia H100 80GB GPU |          64          |
| Training Duration    |          2 days      |

**Configuration**
| HyperParameter    | Llama3 8B CPT SEA-LIONv2 Base |
|-------------------|:--------------------:|
| Precision         | bfloat16             |
| Optimizer         | decoupled_adamw      |
| Scheduler         | weight_stable_decay  |
| Learning Rate     | 1.0e-5               |
| Global Batch Size | 512                  |
| Micro Batch Size  | 2                    |

### Tokenizer

For tokenisation, the model employs the default tokenizer used in Llama 3 8B Instruct.

### Training Data
The Llama3 8B CPT SEA-LIONv2 Base model was continued pre-trained on 48B tokens of the following data:

| Data Source               | Unique Tokens (B) | Multiplier | Total Tokens (B) | Percentage (%) |
|---------------------------|:-----------------:|:----------:|:----------------:|:--------------:|
| Dolma RefinedWeb - English|        7.650      |          1 |       7.650      |     15.90      |
| Dolma C4 - English        |        1.160      |          1 |        1.16      |      9.21      |
| Dolma Reddit - English    |        1.339      |          1 |       1.339      |      2.42      |
| Dolma Semantic Scholar    |        0.959      |          1 |       0.959      |      2.79      |
| Dolma arXiv               |        0.469      |          1 |       0.469      |      1.99      |
| Dolma StarCoder           |        4.422      |          1 |       4.422      |      0.98      |
| SEA-LION Pile - Indonesian|          3.4      |          2 |         6.8      |     14.17      |
| Wiki* - Indonesian        |          0.3      |          4 |         1.2      |      2.50      |
| SEA-LION Pile - Tamil     |          5.6      |          1 |         5.6      |     11.67      |
| Wiki* + News - Tamil      |          0.6      |          4 |         2.4      |      5.00      |
| SEA-LION Pile - Thai      |         2.28      |          1 |        2.28      |      4.75      |
| WangChanBERTa - Thai      |            5      |          1 |           5      |     10.42      |
| Wiki* - Thai              |         0.18      |          4 |        0.72      |      1.50      |
| SEA-LION Pile - Vietnamese|         6.76      |          1 |        6.76      |     14.08      |
| Wiki* - Vietnamese        |         0.31      |          4 |        1.24      |      2.58      |

Note: 
- All token counts are counted using Llama3 tokenizer
- wiki* sources includes Wikipedia, Wiki Books, Wiki Source and Wiki Voyage
- Tamil news is sourced with permission from [Seithi](https://seithi.mediacorp.sg/)

### Benchmark Performance
We evaluated Llama3 8B CPT SEA-LIONv2 Base model on general language capabilities.

#### General Language Capabilities
For the evaluation of general language capabilities in SEA languages, we employed the [BHASA evaluation benchmark](https://arxiv.org/abs/2309.06085v2) across a variety of tasks.
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarization (Summ), Causal Reasoning (Causal) and Natural Language Inference (NLI).

The evaluation was done **five-shot** with native prompts and only a sample of 100-1000 instances for each dataset was used as per the setting described in the paper.

For more details on Llama3 8B CPT SEA-LIONv2 base benchmark performance, please refer to the SEA HELM leaderboard, https://leaderboard.sea-lion.ai/

<br>

## Llama3 8B CPT SEA-LIONv2.1 Instruct

Llama3 8B CPT SEA-LIONv2.1 Instruct is a multilingual model which has been fine-tuned with around 100,000 English instruction-completion pairs alongside a smaller pool of around 50,000 instruction-completion pairs from other ASEAN languages, such as Indonesian, Thai and Vietnamese.

These instructions have been carefully curated and rewritten to ensure the model was trained on truly open, commercially permissive and high quality datasets.

### Fine-Tuning Methodology
The Llama3 8B CPT SEA-LIONv2.1 Instruct model was fine-tuned using 8x A100-40GB using parameter efficient fine tuning in the form of LoRA.

### Fine-Tuning Data
Llama3 8B CPT SEA-LIONv2.1 Instruct was trained on a wide range of instructions that were manually and stringently verified by our team. A large portion of the effort was dedicated to ensuring that each instruction-completion pair that the model sees is of high quality and any errors were corrected and rewritten by native speakers or else dropped from our mix.

In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data source. 

### Benchmark Performance
We evaluated Llama3 8B CPT SEA-LIONv2.1 Instruct on both general language capabilities and instruction-following capabilities.

#### General Language Capabilities
For the evaluation of general language capabilities, we employed the [BHASA evaluation benchmark](https://arxiv.org/abs/2309.06085v2) across a variety of tasks. These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), Abstractive Summarization (Summ), Causal Reasoning (Causal) and Natural Language Inference (NLI).

Note: BHASA is implemented following a strict answer format, and only spaces and punctuations are cleaned. For tasks where options are provided, the answer should only include one of the pre-defined options, nothing else. If the model continues to generate more tokens (e.g. to explain its answer), it will be considered to be a wrong response. For the F1 score metric (as used in Sentiment Analysis and Toxicity Detection), all answers that do not fall under the pre-defined labels will be treated as a separate label (to mark it as a wrong answer) and included in the calculations so that the model is penalized for not generating one of the pre-defined labels.

The evaluation was done **zero-shot** with native prompts and only a sample of 100-1000 instances for each dataset was used as per the setting described in the paper.


#### Instruction-following Capabilities
Since Llama3 8B CPT SEA-LIONv2.1 Instruct is an instruction-following model, we also evaluated it on instruction-following capabilities with two datasets, [IFEval](https://arxiv.org/abs/2311.07911) and [MT-Bench](https://arxiv.org/abs/2306.05685).

As these two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localize and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.

**IFEval**

IFEval evaluates a model's ability to adhere to constraints provided in the prompt, for example beginning a response with a specific word/phrase or answering with a certain number of sections. The metric used is accuracy normalized by language (if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).


**MT-Bench**

MT-Bench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. We use `gpt-4-1106-preview` as the judge model and compare against `gpt-3.5-turbo-0125` as the baseline model. The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category (Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction)). A tie is given a score of 0.5.

<br>

## Llama3 8B CPT SEA-LIONv2.1 Instruct GGUF
The following quantized GGUF formats of our Llama3 8B CPT SEA-LIONv2.1 Instruct model are available:
- llama3-8b-cpt-sea-lionv2.1-instruct-Q2_K
- llama3-8b-cpt-sea-lionv2.1-instruct-Q3_K_M
- llama3-8b-cpt-sea-lionv2.1-instruct-Q4_0
- llama3-8b-cpt-sea-lionv2.1-instruct-Q4_K_M
- llama3-8b-cpt-sea-lionv2.1-instruct-Q5_0
- llama3-8b-cpt-sea-lionv2.1-instruct-Q5_K_M
- llama3-8b-cpt-sea-lionv2.1-instruct-Q6_K
- llama3-8b-cpt-sea-lionv2.1-instruct-Q8_0

Please refer to our [How To Download](#how-to-download) section for more details on how to access them.

<br>

## Download the Model(s)
SEA-LION V2 models are available for download via the following channels:

[HuggingFace SEA-LION V2 Collection](https://huggingface.co/collections/aisingapore/sea-lionv2-672589c4c7ea47e4174d3e7f)


| Model                | Download   |
|----------------------|------------|
llama3-8b-cpt-sea-lionv2-base           | [HuggingFace](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2-base)      |
| llama3-8b-cpt-sea-lionv2.1-instruct | [HuggingFace](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct)      |
| llama3-8b-cpt-sea-lionv2.1-instruct-gguf | [HuggingFace](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct-gguf), [Ollama](https://ollama.com/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct)      |

<br>

## Usage
Llama3 8B CPT SEA-LIONv2.1 Instruct can be run using the 🤗 Transformers library 
```python
# Please use transformers==4.43.2

import transformers
import torch

model_id = "aisingapore/llama3-8b-cpt-SEA-Lionv2.1-instruct"

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

<br>

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