# Llama-SEA-LION-v3.5-70B
## Introduction


At a glance:
- **Model type:** 
- **Tokenizer**: 
- **Context Length**: 128K 
- **Available Formats**:
  - Reasoning (Llama-SEA-LION-v3.5-70B-R)
  - GGUF (Llama-SEA-LION-v3.5-70B-R-GGUF) _`coming soon`_
- **Supported Languages:** 
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


## Llama-SEA-LION-v3-70B-R
### Training Infrastructure


### Tokenizer


### Training Data


### Benchmark Performance

## Llama-SEA-LION-v3-70B-IT
### Fine-Tuning Methodology


### Fine-Tuning Data


### Benchmark Performance


<br>

## Download the Model(s)
Llama-SEA-LION-v3.5-70B-R models are available for download via the following channels:

[HuggingFace SEA-LION v3.5 Collection](https://huggingface.co/collections/aisingapore/sea-lion-v35-67fc3ab84300d7e6088fa32c)


| Model                | Download   |
|----------------------|------------|
| Llama-SEA-LION-v3.5-70B-R           | [HuggingFace](https://huggingface.co/aisingapore/Llama-SEA-LION-v3.5-70B-R), [Kaggle]()      |
| Llama-SEA-LION-v3.5-70B-R-GGUF | _coming soon_ |

<br>

## Usage 
Llama-SEA-LION-v3-70B-R can be run using the 🤗 Transformers library 

```python
import transformers
import torch

model_id = "aisingapore/Llama-SEA-LION-v3-70B-R"

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
