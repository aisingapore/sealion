# SEA-LION (Southeast Asian Languages In One Network)

# <img align="center" src="images/purple_sealion-64x64.png"> A Family of Southeast Asian Language Models

***Updated: 30 July 2024***

SEA-LION is a family of open-source language models developed by AI Singapore that better understands Southeast Asia's diverse contexts, languages, and cultures (SEA). We hope it makes LLMs more accessible and better represents the region's breadth of cultures and languages.

Our first versions of SEA-LION, released in December 2023, were trained from scratched using [SEA-LION-PILE](https://huggingface.co/datasets/aisingapore/sea-lion-pile) (about 1 trillion tokens). Our new version of SEA-LION is based on continued pre-training good open source models. Version 2 is based on Llama 3. We believe that this approach i.e. continued pre-training might be more sustainable over the longer-run. 

## Truly Open Source

We have benefited greatly from the open-source community and believe that efforts to better represent our region will similarly be well served by open-source efforts. SEA-LION will therefore be open and transparent in the following areas:

1. *Pre-Training* data
2. Model *training* code
3. Model *weights*
4. *Fine-Tuning* data
5. Evaluation *benchmarks*

# LATEST MODELS

## Key Features of SEA-LION-V2 *Latest*

- Continued Pre-Trained and Fine-Tuned Llama 3 (with more models to follow)
- Instruction tuned in English, Bahasa Indonesia, Thai, Vietnamese, and Tamil 
- Trained with to 50B tokens from SEA languages
- Outperforms base Llama 3 and other models in both general and SEA capabilities
- Open source under the Meta Llama 3 Community License for community contribution and adoption

## How To Download SEA-LION-V2

SEA-LION models are available for download on HuggingFace at:

### SEA-LION-V2
**Base Models**
* [Llama3-8B-CPT-SEA-LION-V2-Base](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-base)

**Instruction-Tuned Models**
* [Llama3-8B-CPT-SEA-LION-V2-Instruct](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct)

**Quantized Models**
* [Llama3-8B-CPT-SEA-LION-V2-Instruct-GGUF](https://huggingface.co/aisingapore/llama3-8b-cpt-sealionv2-instruct-gguf)

## Getting Started

To use SEA-LION-V2:

```python
# Please use transformers==4.43.2

import transformers
import torch

model_id = "aisingapore/llama3-8b-cpt-sealionv2-instruct"

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

## Model Details
See Hugging Face for model details.

## Performance and Benchmark

SEA-LION achieves better or competitive performances on tasks in regional languages, while retaining the general performance of Llama 3.

Our [leaderboard is here](https://leaderboard.sea-lion.ai).

We use a holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering), but also linguistic and cultural diagnostic tests which are meticulously handcrafted. These are tailored to Southeast Asia.

The benchmark was introduced here [BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa).

## Deployment Framework

### Text Generation Inference (TGI)

Please refer to [serving the SEA-LION model with TGI](https://github.com/aisingapore/sealion-tgi).

### vLLM

Please refer to [serving the SEA-LION model with vLLM](https://github.com/aisingapore/sealion-vllm).

### Ollama

To run SEA-LION locally with Ollama
1. [Download and install Ollama](https://ollama.com)
2. Run and chat with SEA-LION with the following command
```python
ollama run 
```


## Contributing

We welcome contributions to SEA-LION! Check out the [contributing guide](CONTRIBUTING.md) to get started.

Some ways to contribute:

- Report bugs and issues
- Enhance the documentation
- Add more model evaluation tasks and metrics
- Train versions of the model in more SEA languages

## Model License

See Hugging Face for model license details

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


**Base Models**
* [SEA-LION-3B](https://huggingface.co/aisingapore/sea-lion-3b)
* [SEA-LION-7B](https://huggingface.co/aisingapore/sea-lion-7b)

**Instruction-Tuned Models**
* [SEA-LION-7B-Instruct-Research](https://huggingface.co/aisingapore/sea-lion-7b-instruct-research)
* [SEA-LION-7B-Instruct](https://huggingface.co/aisingapore/sea-lion-7b-instruct)

**Model Details**

Please see model cards on Hugging Face.

Additional information and guides about SEA-LION-V1 can be found [here](sea-lion-v1/SEALIONV1_README.md)