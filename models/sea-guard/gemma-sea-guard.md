# Gemma-SEA-Guard-12B

<!-- Provide a quick summary of what the model is/does. -->

**SEA-Guard** is a collection of safety-focused Large Language Models (LLMs) designed specifically for the Southeast Asia (SEA) region. 
While the collection comprises four distinct models, we currently offer a single API endpoint that exclusively serves the [Gemma-based model](https://playground.sea-lion.ai/sea-guard). 
You can generate an API key to access this model at [sea-lion api key manager](https://playground.sea-lion.ai/key-manager).

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

SEA-LION stands for *Southeast Asian Languages In One Network* and is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned for the Southeast Asia (SEA) region. 

This model is a fine-tuned version of [Gemma 3 12B IT](https://huggingface.co/google/gemma-3-12b-it) on 1M instruction-following pairs. 
For more details on training data, please refer to the paper [SEA-Guard](https://arxiv.org/abs/2602.01618).

For tokenization, the model employs the default tokenizer used in Gemma 3.
- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s) (text):** Burmese, English, Indonesian, Malay, Tagalog, Tamil, Thai, and Vietnamese
- **License:** [Gemma](https://ai.google.dev/gemma/terms)
- **Finetuned from model:** [Gemma 3 12B IT](https://huggingface.co/google/gemma-3-12b-it)
  
### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** 🤗[HuggingFace SEA-Guard Collection](https://huggingface.co/collections/aisingapore/sea-guard)

## Intended Uses and Limitations

This model is optimized to return a binary classification in text form: ["safe", "unsafe"]. 
However, users must be aware that the model is subject to the limitations common to generative AI, 
including the potential to hallucinate or generate ungrounded, irrelevant text. 
Due to these inherent risks, human oversight is advised, and the model’s outputs should not be treated as absolute determinations without secondary verification.

## Uses


### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The output of the model is only "safe" or "unsafe". Users can directly use it without any finetune or in-context learning since it is already trained with cultural safety for SEA contexts.
We also release the API of this model at [sea-lion.ai](https://playground.sea-lion.ai/key-manager).

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
Users can also continue training this model further on the target tasks, e.g., vision-text safety datasets.
Also, this model is supported by vLLM for fast inference.

## Training and Evaluation Data

For more details on training data, please refer to the paper [SEA-Guard](https://arxiv.org/abs/2602.01618).

## Training Procedure

We employ a supervised-finetuning technique (SFT) on Llama-factory with the following hyperparameters.

### Testing Data, Factors & Metrics

We use [SEA-SafeguardBench](arxiv.org/abs/2512.05501) to evaluate our SEA-Guard. Note that we also evaluated the vision-text safety classification in [our research paper](https://arxiv.org/abs/2602.01618)

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

AUPRC is the primary metric to evaluate the safety classification of our models.



## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**
```
@misc{tasawong2026seaguardculturallygroundedmultilingual,
      title={SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia}, 
      author={Panuthep Tasawong and Jian Gang Ngui and Alham Fikri Aji and Trevor Cohn and Peerat Limkonchotiwat},
      year={2026},
      eprint={2602.01618},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.01618}, 
}
```

## More Information

This is the repository for the commercial instruction-tuned model. 
Notwithstanding the model's safety-aligned training, developers and users are advised to conduct their own safety fine-tuning and implement appropriate security measures. 
In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. 
Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore.

## Contact

sealion@aisingapore.org