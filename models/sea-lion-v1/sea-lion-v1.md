# SEA-LION v1
## Introduction
SEA-LION version 1, released in December 2023, was our first collection of Large Language Models (LLMs) that were specifically **pretrained** and **instruct-tuned** for the Southeast Asia (SEA) region, making a significant leap forward in the field of Natural Language Processing in understanding the SEA regional context.

SEA-LION v1 comes in two model sizes – one with 3 billion parameters (SEA-LION-v1-3B) and another with 7 billion parameters (SEA-LION-v1-7B). Both variants are built on the robust MPT architecture and utilise a vocabulary size of 256K, with **context length of 2048 tokens**.

Our SEA-LION-v1-7B model was then further instruct-tuned to produce SEA-LION-v1-7B-IT.

At a glance:
- **Model type:** Decoder
- **Tokenizer**: Custom SEABPETokenizer
- **Available Formats**:
  - 3B Base (SEA-LION-v1-3B)
  - 7B Base (SEA-LION-v1-7B)
  - 7B Instruct (SEA-LION-v1-7B-IT)
  - 7B GGUF (SEA-LION-v1-7B-IT-GGUF)
- **Languages:**
   1. English
   2. Chinese
   3. Indonesian
   4. Malay
   5. Thai
   6. Vietnamese
   7. Filipino
   8. Tamil
   9. Burmese
   10. Khmer
   11. Lao
- **License:** MIT

## SEA-LION-v1-3B / SEA-LION-v1-7B
### Model Architecture
SEA-LION-v1-3B and SEA-LION-v1-7B are both decoder models built on the robust MPT architecture:
| Parameter         | SEA-LION-v1-3B | SEA-LION-v1-7B |
|------------------|:------------:|:------------:|
| Layers          | 32         | 32         |
| d_model        | 2560       | 4096       |
| head_dim       | 20         | 32         |
| Vocabulary     | 256000     | 256000     |
| Sequence Length | 2048       | 2048       |


### Training Infrastructure
SEA-LION v1 was trained using [MosaicML Composer](https://github.com/mosaicml/composer) on the following hardware:
| Training Details             | SEA-LION-v1-3B  | SEA-LION-v1-7B  |
|------------------------------|:-------------:|:-------------:|
| AWS EC2 p4d.24xlarge        | 30 instances | 32 instances |
| Nvidia A100 40GB GPU        | 240         | 256         |
| Training Duration           | 14 days     | 22 days     |


**Configuration:**
| HyperParameter     | SEA-LION-v1-3B          | SEA-LION-v1-7B          |
|--------------------|:---------------------:|:---------------------:|
| Precision         | bfloat16            | bfloat16            |
| Optimizer        | decoupled_adamw      | decoupled_adamw      |
| Scheduler        | cosine_with_warmup   | cosine_with_warmup   |
| Learning Rate    | 1.6e-4               | 6.0e-5               |
| Global Batch Size | 1200                | 2048                |
| Micro Batch Size  | 5                   | 4                   |

For full details on our SEA-LION v1 training infrastructure and configuration, please refer to our [SEA-LION Pre-Training Setup Guide](./pre-training/README-PRE-TRAINING.md)


### Tokenizer
For tokenization, both SEA-LION-v1-3B and SEA-LION-v1-7B employed our custom SEABPETokenizer, which is specially tailored for SEA languages, ensuring optimal model performance.

SEABPETokenizer was trained by sampling 20M lines from the model training data, using the SentencePiece framework. The tokenizer type is Byte-Pair Encoding (BPE).

### Training Data
SEA-LION-v1-3B and SEA-LION-v1-7B were trained on 980B tokens of text data from 11 languages spoken across SEA:
- English
- Chinese
- Indonesian
- Malay
- Thai
- Vietnamese
- Filipino
- Tamil
- Burmese
- Khmer
- Lao

These 980B tokens comprised of the following data mix:
| Data Source                 | Unique Tokens | Multiplier | Total Tokens | Percentage |
|-----------------------------|--------------:|-----------:|------------:|-----------:|
| RefinedWeb - English        | 571.3B       | 1          | 571.3B      | 58.20%     |
| mC4 - Chinese               | 91.2B        | 1          | 91.2B       | 9.29%      |
| mC4 - Indonesian            | 3.68B        | 4          | 14.7B       | 1.50%      |
| mC4 - Malay                 | 0.72B        | 4          | 2.9B        | 0.29%      |
| mC4 - Filipino              | 1.32B        | 4          | 5.3B        | 0.54%      |
| mC4 - Burmese               | 1.2B         | 4          | 4.9B        | 0.49%      |
| mC4 - Vietnamese            | 63.4B        | 1          | 63.4B       | 6.46%      |
| mC4 - Thai                  | 5.8B         | 2          | 11.6B       | 1.18%      |
| WangChanBERTa - Thai        | 5B           | 2          | 10B         | 1.02%      |
| mC4 - Lao                   | 0.27B        | 4          | 1.1B        | 0.12%      |
| mC4 - Khmer                 | 0.97B        | 4          | 3.9B        | 0.40%      |
| mC4 - Tamil                 | 2.55B        | 4          | 10.2B       | 1.04%      |
| the Stack - Python          | 20.9B        | 2          | 41.8B       | 4.26%      |
| the Stack - Javascript      | 55.6B        | 1          | 55.6B       | 5.66%      |
| the Stack - Shell           | 1.2B5        | 2          | 2.5B        | 0.26%      |
| the Stack - SQL             | 6.4B         | 2          | 12.8B       | 1.31%      |
| the Stack - Markdown        | 26.6B        | 1          | 26.6B       | 2.71%      |
| RedPajama - StackExchange   | 21.2B        | 1          | 21.2B       | 2.16%      |
| RedPajama - ArXiv           | 30.6B        | 1          | 30.6B       | 3.12%      |

The dataset is available here: [SEA-LION-PILE](https://huggingface.co/datasets/aisingapore/sea-lion-pile).


### Performance
SEA-LION-v1-3B and SEA-LION-v1-7B base models had an average performance on general tasks in English (as measured by Hugging Face's LLM Leaderboard):

| Model        | ARC   | HellaSwag | MMLU  | TruthfulQA | Average |
|--------------|:-------:|:-----------:|:-------:|:------------:|:---------:|
| SEA-LION-v1-3B  | 36.26 | 64.59     | 24.07 | 36.46      | 40.35   |
| SEA-LION-v1-7B  | 39.93 | 68.51     | 26.87 | 35.09      | 42.60   |

For up-to-date comparison of SEA-LION performance against other latest models, please refer to our [SEA-LION Leaderboard](https://leaderboard.sea-lion.ai)


## SEA-LION-v1-7B-IT

SEA-LION-v1-7B-IT is a multilingual model which has been fine-tuned with thousands of English and Indonesian instruction-completion pairs alongside a smaller pool of instruction-completion pairs from other ASEAN languages, using our pre-trained SEA-LION-v1-7B as base. 

These instructions have been carefully curated and rewritten to ensure the model was trained on truly open, commercially permissive and high quality datasets.


### Fine-Tuning Methodology

The SEA-LION-v1-7B-IT was fine-tuned using 8x A100-40GB using parameter efficient fine tuning in the form of LoRA.

To perform similar fine-tuning on our SEA-LION-v1-7B base model using the HuggingFace TRL library, you can refer to sample configurations provided in our [SEA-LION QLoRA Fine-Tuning Guide.](./fine-tuning/README.md)


### Fine-Tuning Data
SEA-LION-v1-7B-IT was trained on a wide range of instructions that were manually and stringently verified by our team. A large portion of the effort was dedicated to ensuring that each instruction-completion pair that the model sees is of a high quality and any errors were corrected and rewritten by native speakers or else dropped from our mix.

In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data source.


### Benchmarks
We evaluated SEA-LION-v1-7B-IT on the BHASA benchmark ([arXiv](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa)) across a variety of tasks.

BHASA stands out amongst other evaluations for SEA languages for its holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering), but also linguistic and cultural diagnostic tests which are meticulously handcrafted.

The evaluation was done zero-shot with Indonesian prompts and only a sample of 100-1000 instances for each dataset was used as per the setting described in the BHASA paper.

- For Natural Language Understanding (NLU) tasks, we tested the model on Sentiment Analysis (Sentiment) using the NusaX dataset, Question Answering (QA) using the TyDiQA dataset, and Toxicity Detection (Toxicity) using the Indonesian Multi-Label Hate Speech Detection dataset. The metrics used are F1 scores for all three tasks.
- For Natural Language Generation (NLG) tasks, we tested the model on Machine Translation from English to Indonesian (Eng>Indo) and from Indonesian to English (Indo>Eng) using the FLORES-200 dataset, and Abstractive Summarization (Summary) using the XLSum dataset. The metrics used for Machine Translation and Abstractive Summarization are ChrF++ and ROUGE-L respectively.
- For Natural Language Reasoning (NLR) tasks, we tested the model on Natural Language Inference (NLI) using the IndoNLI lay dataset and on Causal Reasoning (Causal) using the XCOPA dataset. The metrics are based on accuracy for both tasks.


### Performance
SEA-LION v1 models achieved better or competitive performances on tasks in regional languages at the time of release:

| Model                          | QA (F1) | Sentiment (F1) | Toxicity (F1) | Eng>Indo (ChrF++) | Indo>Eng (ChrF++) | Summary (ROUGE-L) | NLI (Acc) | Causal (Acc) |
|--------------------------------|---------|----------------|---------------|-------------------|-------------------|-------------------|-----------|--------------|
| SEA-LION-7B-Instruct-Research  | 24.86   | 76.13          | 24.45         | 52.50             | 46.82             | 15.44             | 33.20     | 23.80        |
| SEA-LION-7B-Instruct           | 68.41   | 91.45          | 17.98         | 57.48             | 58.04             | 17.54             | 53.10     | 60.80        |
| SeaLLM 7B v1                   | 30.96   | 56.29          | 22.60         | 62.23             | 41.55             | 14.03             | 26.50     | 56.60        |
| SeaLLM 7B v2                   | 44.40   | 80.13          | 55.24         | 64.01             | 63.28             | 17.31             | 43.60     | 82.00        |
| Sailor-7B                      | 65.43   | 59.48          | 20.48         | 64.27             | 60.68             | 8.69              | 15.10     | 38.40        |
| Llama 2 7B Chat                | 11.12   | 52.32          | 0.00          | 44.09             | 57.58             | 9.24              | 0.00      | 0.00         |
| Mistral 7B Instruct v0.1       | 38.85   | 74.38          | 20.83         | 30.60             | 51.43             | 15.63             | 28.60     | 50.80        |
| GPT-4                          | 73.60   | 74.14          | 63.96         | 69.38             | 67.53             | 18.71             | 83.20     | 96.00        |

For up-to-date comparison of SEA-LION performance against other latest models, please refer to our [SEA-LION Leaderboard](https://leaderboard.sea-lion.ai)


## SEA-LION-7B-Instruct-GGUF

Support for SEA-LION-v1-IT-GGUF was merged into `llama.cpp` as of 4th Apr 2024.

SEA-LION can be run using the `llama.cpp` library from commit id [bb43cf7](https://github.com/ggerganov/llama.cpp/commit/bb43cf7e9d86d69ffd9c7f008f75db890a35b45a) or later.

**Prompt Template:**
```
### USER:
{{prompt}}

### RESPONSE:

```

**Recommended `llama.cpp` command:**
```
./main -m sea-lion-7b-instruct-Q4_0.gguf --temp 0 --repeat-penalty 1.2 -e -ngl 32 -p "### USER:\nwhat is a sea lion?\n\n### RESPONSE:\n"
```

**To convert & quantize your own SEA-LION model:**
```
python convert-hf-to-gguf.py {{model path}}

./quantize ggml-model-f16.gguf {{Quant Type}}
```

For other parameters and how to use them, please refer to [llama.cpp documentation.](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)


The following quantized GGUF formats of our SEA-LION-v1-7B-IT model are available:
- sea-lion-7b-instruct-Q2_K
- sea-lion-7b-instruct-Q3_K_M
- sea-lion-7b-instruct-Q4_0
- sea-lion-7b-instruct-Q4_K_M
- sea-lion-7b-instruct-Q5_0
- sea-lion-7b-instruct-Q5_K_M
- sea-lion-7b-instruct-Q6_K
- sea-lion-7b-instruct-Q8_0

Please refer to our [Download the Model(s)](#download-the-model-s) section for more details on how to access them.

## Download the Model(s)
SEA-LION v1 models are available for download via the following channels:

[HuggingFace SEA-LION v1 Collection](https://huggingface.co/collections/aisingapore/sea-lionv1-672589cd29a1781afa6be35e)


| Model                | Download   |
|----------------------|------------|
| SEA-LION-v1-3B          | [HuggingFace](https://huggingface.co/aisingapore/sea-lion-3b)      |
| SEA-LION-v1-7B          | [HuggingFace](https://huggingface.co/aisingapore/sea-lion-7b)      |
| SEA-LION-v1-7B-IT | [HuggingFace](https://huggingface.co/aisingapore/sea-lion-7b-instruct)      |
| SEA-LION-v1-7B-IT-GGUF | [HuggingFace](https://huggingface.co/aisingapore/sea-lion-7b-instruct-gguf)      |


## Usage
SEA-LION-v1-7B-IT can be run using the 🤗 Transformers library

```python
# Please use transformers==4.37.2
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("aisingapore/sea-lion-7b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("aisingapore/sea-lion-7b-instruct", trust_remote_code=True)

prompt_template = "### USER:\n{human_prompt}\n\n### RESPONSE:\n"
prompt = """Apa sentimen dari kalimat berikut ini?
Kalimat: Buku ini sangat membosankan.
Jawaban: """
full_prompt = prompt_template.format(human_prompt=prompt)

tokens = tokenizer(full_prompt, return_tensors="pt")
output = model.generate(tokens["input_ids"], max_new_tokens=20, eos_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Prompting Guide
A basic prompting guide for the SEALION v1 models is provided [here](./sea-lion-v1_promptguide.md)

## Disclaimer

It is important for users to be aware that our models exhibits certain limitations that warrant consideration:
1. The model can hallucinate and occasionally generates irrelevant content, introducing fictional elements that are not grounded in the provided context. Users should also exercise caution in interpreting and validating the model's responses due to the potential inconsistencies in its reasoning. 
2. The model has not been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.
3. It should be noted that the model has not been optimized for multi-turn dialogue interactions, which may result in reduced effectiveness in extended conversations.


## References
Thai Pre-Training Data Reference
```
@misc{lowphansirikul2021wangchanberta,
    title={WangchanBERTa: Pretraining transformer-based Thai Language Models},
    author={Lalita Lowphansirikul and Charin Polpanumas and Nawat Jantrakulchai and Sarana Nutanong},
    year={2021},
    eprint={2101.09635},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```