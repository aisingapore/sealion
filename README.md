# SEA-LION (Southeast Asian Languages In One Network)

# <img align="center" src="images/purple_sealion-64x64.png"> A Family of Southeast Asian Language Models

***Updated: 1 November 2024***

SEA-LION is a family of open-source language models developed by AI Singapore that better understands Southeast Asia's diverse contexts, languages, and cultures (SEA). We hope it makes LLMs more accessible and better represents the region's breadth of cultures and languages.

Version 3 is based on Google's Gemma 2. It is a 9B parameter model and it supports 11 Southeast Asian languages (English, Chinese, Indonesian, Malay, Thai, Vietnamese, Filipino, Tamil, Burmese, Khmer, and Lao) + 2 dialects (Javanese and Sundanese).

## Transparent and Open Source

We have benefited greatly from the open-source community and believe that efforts to better represent our region will similarly be well served by open-source efforts. SEA-LION will therefore be open and transparent in the following areas:

1. *Pre-Training* data [SEA-LION-PILE](https://huggingface.co/datasets/aisingapore/sea-lion-pile)
2. Model *training* code
3. Model *weights*
4. *Fine-Tuning* data
5. Evaluation *benchmarks* [GitHub](https://github.com/aisingapore/bhasa)

# LATEST MODELS

## Key Features of SEA-LION v3

- Continued Pre-Training from Gemma 2 base with 200B tokens from 11 Southeast Asian languages (English, Chinese, Indonesian, Malay, Thai, Vietnamese, Filipino, Tamil, Burmese, Khmer, Lao
- Further fine-tuning to improve general and SEA capabilities, and optimize for instruction following and multi-turn conversations
- Outperforms similar sized open source models, and even some larger models in both general and SEA capabilities
- Our contributions are open source (under MIT license); model licenses are derived from the Gemma, and listed on their respective Hugging Face model cards

See our [HuggingFace](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct) page for more detailed model and license information.

## How To Download SEA-LION v3

SEA-LION models are available for download on HuggingFace at:

**Base Models**
* [Gemma2-9B-CPT-SEA-LION-V3-Base](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-base)

**Instruction-Tuned Models**
* [Gemma2-9B-CPT-SEA-LION-V3-Instruct](https://huggingface.co/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct)

On Kaggle at:

**Intruction-Tuned Model**
* [Gemma2-9B-CPT-SEA-LION-V3-Instruct](https://www.kaggle.com/models/ai-singapore/gemma2-9b-cpt-sea-lionv3-instruct)

On Ollama at:

**Quantized Models**
* [Gemma2-9B-CPT-SEA-LION-V3-Instruct](https://ollama.com/aisingapore/gemma2-9b-cpt-sea-lionv3-instruct)

## Getting Started

To use SEA-LION v3:

```python
# Please use transformers==4.43.2

import transformers
import torch

model_id = "aisingapore/gemma2-9b-cpt-sealionv3-instruct"

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

## Performance and Benchmarks

SEA-LION achieves better or competitive performance on tasks in regional languages while retaining the general performance of Gemma 2.

Our [leaderboard is here](https://leaderboard.sea-lion.ai).

We use a holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering) but also meticulously handcrafted linguistic and cultural diagnostic tests tailored to Southeast Asia.

The benchmark was introduced here [BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa).

## Deployment Framework

### Text Generation Inference (TGI)

Please refer to [serving the SEA-LION model with TGI](https://github.com/aisingapore/sealion-tgi).

### vLLM

Please refer to [serving the SEA-LION model with vLLM](https://github.com/aisingapore/sealion-vllm).

### Ollama

To run SEA-LION locally with Ollama via the command line:
1. [Download and install Ollama](https://ollama.com)
2. Run and chat with SEA-LION with the following command
   ```python
   ollama run aisingapore/llama3-8b-cpt-sea-lionv2-instruct
   ```

or [explore SEA-LION with Chainlit and Ollama here](https://github.com/aisingapore/sealion-chainlit-ollama)

## Contributing

We welcome contributions to SEA-LION! Check out the [contributing guide](CONTRIBUTING.md) to get started.

Some ways to contribute:

- Report bugs and issues
- Enhance the documentation
- Add more model evaluation tasks and metrics
- Train versions of the model in more SEA languages

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

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. Any opinion, finding, conclusion or recommendation expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore, or the National University of Singapore. 

We also grateful for the support of the Infocomm Media Development Authority (IMDA) of Singapore.

SEA-LION would not be possible without a growing list of Singapore, regional, and international collaborators. Please see our website for more details.

## Contact

If you have questions, comments, or issues, please open a GitHub issue or contact us via this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6).


# OTHER MODELS

## SEA-LION v1

- 3 to 7 billion parameters 
- Instruction tuned in English and Bahasa Indonesia
- Trained with 980B tokens of text data from 11 languages spoken across SEA
- Specialized vocabulary and tokenization for optimal performance in SEA languages
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

Additional information and guides about SEA-LION v1 can be found [here](sea-lion-v1/README.md)

## SEA-LION v2

- Continued Pre-Trained and Fine-Tuned Llama 3
- Instruction tuned in English, Bahasa Indonesia, Thai, Vietnamese, and Tamil 
- Trained with up to 50B tokens from SEA languages
- Outperforms base Llama 3 and other models in both general and SEA capabilities
- Our contributions are open source (under MIT license); model licenses are listed on their respective Hugging Face model cards

**Base Models**
* [Llama3-8B-CPT-SEA-LION-V2-Base](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2-base)

**Instruction-Tuned Models**
* [Llama3-8B-CPT-SEA-LION-V2.1-Instruct](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct)
* [Llama3-8B-CPT-SEA-LION-V2-Instruct](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2-instruct)

**Quantized Models**
* [Llama3-8B-CPT-SEA-LION-V2.1-Instruct-GGUF](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2.1-instruct-gguf)
* [Llama3-8B-CPT-SEA-LION-V2-Instruct-GGUF](https://huggingface.co/aisingapore/llama3-8b-cpt-sea-lionv2-instruct-gguf)

**Model Details**
Please see model cards on Hugging Face.

Additional information and guides about SEA-LION v2.x can be found [here](sea-lion-v2/README.md)