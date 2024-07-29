# SEA-LION (Southeast Asian Languages In One Network)

# <img align="center" src="images/purple_sealion-64x64.png"> A Family of Southeast Asian Language Models

***Updated: 30 July 2024***

SEA-LION is a family of open-source language models developed by AI Singapore that better understands Southeast Asia's diverse contexts, languages, and cultures (SEA). We hope it makes LLMs more accessible and better represents the region's breadth of cultures and languages.

Our first versions of SEA-LION, released in December 2023, were trained from scratched using [SEA-LION-PILE](https://huggingface.co/datasets/aisingapore/sea-lion-pile) (about 1 trillion tokens). Our new version of SEA-LION is based on continued pre-training good open source models. Version 2 is based on LLaMA3. We believe that this approach i.e. continued pre-training might be more sustainable over the longer-run. 

## Truly Open Source

We have benefited greatly from the open-source community and believe that efforts to better represent our region will similarly be well served by open-source efforts. SEA-LION will therefore be open and transparent in the following areas:

1. *Pre-Training* data
2. Model *training* code
3. Model *weights*
4. *Fine-Tuning* data
5. Evaluation *benchmarks*

# LATEST MODELS

## Key Features of SEA-LION-V2 *Latest*

- Continued Pre-Trained and Fine-Tuned LLaMA3 (with more models to follow)
- Instruction tuned in English, Bahasa Indonesia, Thai, Vietnamese, and Tamil 
- Trained with to 50B tokens from SEA languages
- Outperforms base LLaMA3 and other models in both general and SEA capabilities
- Open source under the MIT License for community contribution and adoption

## How To Download SEA-LION-V2

SEA-LION models are available for download on HuggingFace at:

### SEA-LION-V2
**Base Models**
* [LlaMA3-8B-SEA-LION-V2-Base](https://huggingface.co/aisingapore/llama3-8b-sea-lion-v2)

**Instruction-Tuned**
* [LlaMA3-8B-SEA-LION-V2-Instruct](https://huggingface.co/aisingapore/llama3-8b-sea-lion-v2-instruct)

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

## Model Details
See Hugging Face for model details.

## Performance and Benchmark

SEA-LION achieves better or competitive performances on tasks in regional languages, while retaining the general performance of LLaMA3.

Our [leaderboard is here](https://leaderboard.sea-lion.ia).

We use a holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering), but also linguistic and cultural diagnostic tests which are meticulously handcrafted. These are tailored to Southeast Asia.

The benchmark was introduced here [BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa).

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

## Deployment Framework

### Text-Generation-Inference (TGI)

SEA-LION is natively supported in TGI from [v1.4.0](https://github.com/huggingface/text-generation-inference/releases/tag/v1.4.0).

### vLLM

For SEA-LION vLLM intergration, please refer to this [guide for instructions](https://github.com/aisingapore/sealion/tree/vllm/vllm).


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
@misc{sea_lion_2024,
  title={SEA-LION (Southeast Asian Languages In One Network): A Family of Large Language Models for Southeast Asia},
  author={AI Singapore},
  year={2024},
  howpublished={\url{https://github.com/aisingapore/sealion}}
}
```

## Acknowledgements

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore.
Any opinion, finding, conclusion or recommendation expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore, or the National University of Singapore.

## Contact

For questions, comments, or issues, please open a GitHub issue or contact us via this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6).

## References

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
# OTHER MODELS

## SEA-LION-V1

- 3 to 7 billion parameters 
- Instruction tuned in English and Bahasa Indonesia
- Trained with 980B tokens of text data from 11 languages spoken across SEA
- Specialized vocabulary and tokenization for optimal performance on SEA languages
- Excels on tasks in regional languages
- Open source under the MIT License for community contribution and adoption

### SEA-LION-V1
**Base Models**
* [SEA-LION-3B](https://huggingface.co/aisingapore/sea-lion-3b)
* [SEA-LION-7B](https://huggingface.co/aisingapore/sea-lion-7b)

**Instruction-Tuned**
* [SEA-LION-7B-Instruct-Research](https://huggingface.co/aisingapore/sea-lion-7b-instruct-research)
* [SEA-LION-7B-Instruct](https://huggingface.co/aisingapore/sea-lion-7b-instruct)

## Model Details
Please see model cards on Hugging Face.