# SEA-LION (Southeast Asian Languages In One Network)

# <img align="center" src="images/purple_sealion-64x64.png"> A Family of Southeast Asian Language Models

***Updated: 12 March 2024***

SEA-LION is a family of open-source language models developed by AI Singapore that better understands Southeast Asia's diverse contexts, languages, and cultures (SEA). We hope it makes LLMs more accessible and better represents the region's breadth of cultures and languages.

## Truly Open Source

We have benefited greatly from the open-source community and believe that efforts to better represent our region will similarly be well served by open-source efforts. We therefore make the following (open-source compliant) contributions:

1. *Pre-Training* data
2. Model *training* code
3. Model *weights*
4. *Fine-Tuning* data
5. Evaluation *benchmarks*

## Key Features

- 3 to 7 billion parameters (larger models to be released through 2024)
- Instruction-tuned in English and Bahasa Indonesia, with more to follow
- Trained on 980B tokens of text data from 11 languages spoken across SEA
- Specialized vocabulary and tokenization for optimal performance on SEA languages
- Excels on tasks in regional languages
- Open source under the MIT License for community contribution and adoption

## Getting Started

To use SEA-LION:

```python
# please use transformers 4.34.1
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("aisingapore/sea-lion-3b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("aisingapore/sea-lion-3b", trust_remote_code=True)

tokens = tokenizer("Sea lion in the sea", return_tensors="pt")
output = model.generate(tokens["input_ids"], max_new_tokens=20, eos_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### How To Download SEA-LION

SEA-LION models are available for download on HuggingFace at:

**Base Models**
* [SEA-LION-3B](https://huggingface.co/aisingapore/sea-lion-3b)
* [SEA-LION-7B](https://huggingface.co/aisingapore/sea-lion-7b)

**Instruction-Tuned**
* [SEA-LION-7B-Instruct-Research](https://huggingface.co/aisingapore/sea-lion-7b-instruct-research)
* **LATEST** [SEA-LION-7B-Instruct](https://huggingface.co/aisingapore/sea-lion-7b-instruct)

## Model Details

SEA-LION is based on the MPT architecture with 32 layers and comes in two sizes:

- [SEA-LION-3B](https://huggingface.co/aisingapore/sea-lion-3b) : 3 billion parameters 
- [SEA-LION-7B](https://huggingface.co/aisingapore/sea-lion-7b) : 7 billion parameters
- [SEA-LION-7B-Instruct-Research](https://huggingface.co/aisingapore/sea-lion-7b-instruct-research): 7 billion parameters, instruction-tuned in Bahasa Indonesia
- **LATEST** [SEA-LION-7B-Instruct](https://huggingface.co/aisingapore/sea-lion-7b-instruct): 7 billion parameters, instruction-tuned in English and Bahasa Indonesia

SEA-LION has been trained on a diverse dataset of 980B tokens spanning 11 natural languages:

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

The dataset is available here [SEA-LION-PILE](https://huggingface.co/datasets/aisingapore/sea-lion-pile).

The models use a vocabulary of 256,000 tokens and a context length of 2048 tokens. For tokenization, the model employs a custom SEA byte-pair encoding (BPE) tokenizer which is specially tailored for SEA languages, ensuring optimal model performance.

## Benchmark

We use a holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering), but also linguistic and cultural diagnostic tests which are meticulously handcrafted. These are tailored to Southeast Asia.

The benchmark was introduced here [BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa).

## Performance

SEA-LION achieves better or competitive performances on tasks in regional languages:

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

SEA-LION has an average performance on general tasks in English (as measured by Hugging Face's LLM Leaderboard):

| Model       | ARC   | HellaSwag | MMLU  | TruthfulQA | Average |
|-------------|:-----:|:---------:|:-----:|:----------:|:-------:|
| SEA-LION-7B | 39.93 | 68.51     | 26.87 |      35.09 | 42.60   |

For full details on the datasets, metrics, and results, please see the model cards:

* [SEA-LION-3B](https://huggingface.co/aisingapore/sea-lion-3b)
* [SEA-LION-7B](https://huggingface.co/aisingapore/sea-lion-7b)
* [SEA-LION-7B-Instruct-Research](https://huggingface.co/aisingapore/sea-lion-7b-instruct-research)
* **LATEST** [SEA-LION-7B-Instruct](https://huggingface.co/aisingapore/sea-lion-7b-instruct)

## SEA-LION Demo

A video demo of SEA-LION is available [here](https://aisingapore.github.io/sealion/).

## Prompting Guide
A basic prompting guide is provided [here](docs/promptguide.md)

## Pre-Training Config and Guide

SEA-LION 3B and 7B models are trained on 32 nodes of A100 40GB on AWS EC2.  
The configuration used for pre-training and an overview guide is provided [here](pre-training/README-PRE-TRAINING.md).

## QLoRA Fine-Tuning Guide

The SEA-LION models can be fine-tuned using the HuggingFace TRL library.  
An overview guide and sample configurations are provided [here](examples/fine-tuning/README.md).

## Contributing

We welcome contributions to SEA-LION! Check out the [contributing guide](CONTRIBUTING.md) to get started.

Some ways to contribute:

- Report bugs and issues
- Enhance the documentation
- Add more model evaluation tasks and metrics
- Train versions of the model in more SEA languages

## License

SEA-LION is licensed under the [MIT License](LICENSE).

## To Cite SEA-LION

If you use SEA-LION in your work, please cite it as:

```bibtex
@misc{sea_lion_2023,
  title={SEA-LION (Southeast Asian Languages In One Network): A Family of Large Language Models for Southeast Asia},
  author={AI Singapore},
  year={2023},
  howpublished={\url{https://github.com/aisingapore/sealion}}
}
```

## Acknowledgements

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore.
Any opinion, finding, conclusion or recommendation expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore, or the National University of Singapore.

## Contact

For questions, comments, or issues, please open a GitHub issue or contact us via this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6).

## Citations

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
