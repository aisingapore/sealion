# SEA-LION (Southeast Asian Languages In One Network)
# <img align="center" src="images/purple_sealion-64x64.png"> A Family of Southeast Asian Language Models

Updated: 5 March 2024

SEA-LION is a family of open source language models developed by AI Singapore to better understand and represent the diverse contexts, languages, and cultures of Southeast Asia (SEA). 

## Open Source

We have benefited greatly from open source, and believe that efforts to better represent our region are well served by truly open source efforts. We contributions include the following (open-source compliant):

1. *Pre-Training* data
2. Model *training* code
3. Model *weights*
4. *Fine-Tuning* data
5. Evaluation *benchmarks*

## Key Features

- 3 to 7 billion parameters (larger models to be released through 2024)
- Instruct-tuned in Bahasa Indonesia, with more to follow
- Trained on 980B tokens of text data from 11 languages spoken across SEA
- Specialized vocabulary and tokenization for optimal performance on SEA languages
- Excels on tasks in regional languages
- Open source under the MIT License for community contribution and adoption

## Getting Started

To use SEA-LION:

```python
# please use transformers 4.34.1
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("aisingapore/sealion3b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("aisingapore/sealion3b", trust_remote_code=True)

tokens = tokenizer("Sea lion in the sea", return_tensors="pt")
output = model.generate(tokens["input_ids"], max_new_tokens=20)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### How To Download SEA-LION

SEA-LION models are available for download on HuggingFace at:

**Base Models**
* [SEA-LION 3B](https://huggingface.co/aisingapore/sea-lion-3b)
* [SEA-LION 7B](https://huggingface.co/aisingapore/sea-lion-7b)

**Instruct-Tuned**
* [SEA-LION 7B-instruct-research](https://huggingface.co/aisingapore/sealion7b-instruct-research)
* **LATEST**[SEA-LION 7B-instruct](https://huggingface.co/aisingapore/sea-lion-7b-instruct)

## Model Details

SEA-LION is based on the MPT architecture with 32 layers and comes in two sizes:

- [SEA-LION 3B](https://huggingface.co/aisingapore/sea-lion-3b) : 3 billion parameters 
- [SEA-LION 7B](https://huggingface.co/aisingapore/sea-lion-7b) : 7 billion parameters
- [SEA-LION 7B-instruct-research](https://huggingface.co/aisingapore/sealion7b-instruct-research): 7 billion parameters, instruct-tuned in Bahasa Indonesia
- **LATEST**[SEA-LION 7B-instruct](https://huggingface.co/aisingapore/sealion7b-instruct): 7 billion parameters, instruct-tuned in Bahasa Indonesia

It was trained on a diverse dataset of 980B tokens spanning 11 natural languages:

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

The model uses a vocabulary of 256,000 tokens and a context length of 2048 tokens. For tokenization, the model employs a custom SEA byte-pair encoding (BPE) tokenizer which is specially tailored for SEA languages, ensuring optimal model performance.

## Performance

SEA-LION achieves better or competitive performances on tasks in regional languages:

| Model Name               | Sent (F1) | QA (F1)  | Tox (F1) | MT-EN-ID (ChrF++)| (COMET22)| MT-ID-EN (ChrF++)| (COMET22)| AbsSum (ROUGE-L)| NLI (Acc) | Causal (Acc) |
|--------------------------|:---------:|:--------:|:--------:|:----------------:|:--------:|:----------------:|:--------:|:---------------:|:---------:|:------------:|
| sealion7b-instruct-nc    | **76.13** | 24.86    | **24.45**| **52.50**        | **86.97**| 46.82            | 81.34    | **15.44**       | **33.20** | **23.80**    |
| Mistral-7B-Instruct-v0.1 | 73.66     | **26.08**| 18.60    | 31.08            | 55.29    | 51.20            | 82.38    | 14.41           | 29.20     | 11.00        |
| Llama-2-7b-chat-hf       | 41.92     | 4.23     | 0.00     | 47.96            | 77.86    | **55.76**        | **86.08**| 4.59            | 0.00      | 0.00         |
| falcon-7b-instruct       | 0.00      | 8.47     | 7.21     | 1.66             | 30.07    | 16.82            | 46.32    | 1.55            | 0.00      | 2.20         |

SEA-LION has an average performance on general tasks in English (as measured by Hugging Face's LLM Leaderboard):

| Model       | ARC   | HellaSwag | MMLU  | TruthfulQA | Average |
|-------------|:-----:|:---------:|:-----:|:----------:|:-------:|
| SEA-LION 7B | 39.93 | 68.51     | 26.87 |      35.09 | 42.60   |


For full details on the datasets, metrics, and results, please see the model cards:
* [SEA-LION 3B](https://huggingface.co/aisingapore/sealion3b)
* [SEA-LION 7B](https://huggingface.co/aisingapore/sealion7b)
* [SEA-LION 7B-instruct](https://huggingface.co/aisingapore/sealion7b-instruct-nc)

## SEA-LION Demo

A video demo of SEA-LION is available [here](https://aisingapore.github.io/sealion/)

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

For questions, comments, or issues, please open a GitHub issue or contact us 
via this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6)

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
