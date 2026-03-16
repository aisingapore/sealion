# SEA-LION-E5-Embedding-600M

Last update: 2026-03-16

**SEA-LION** is a collection of Large Language Models (LLMs) and encoders which have been pretrained and fine-tuned for the Southeast Asia (SEA) region.

<!-- Introduction -->
## Introduction
SEA-LION stands for *Southeast Asian Languages In One Network*. 

The **SEA-LION-Embedding-E5-600M** model is a Sentence Transformer optimised for 11 Southeast Asian languages. It has been fine-tuned from the [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) base, mapping sentences and paragraphs to a 1024-dimensional dense vector space. This model is designed for high-accuracy semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and RAG (Retrieval-Augmented Generation) workflows. It leverages the robust XLM-RoBERTa architecture pretrained on 100 languages, optimised here for 11 Southeast Asian languages: Burmese, Chinese, English, Filipino, Indonesian, Khmer, Lao, Malay, Tamil, Thai, and Vietnamese.

## Model Details

### Model Description

The SEA-LION-E5-Embedding-600M model is a Sentence Transformer built on the [Multilingual E5 Text Embeddings](https://arxiv.org/pdf/2402.05672) which was initialised from [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) architecture.

- **Model Type:** Sentence Transformer
- **Base Architecture:** E5 (Transformer Encoder)
- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Context length:** 512
- **Languages:** Burmese, Chinese, English, Filipino, Indonesian, Khmer, Lao, Malay, Tamil, Thai, and Vietnamese
- **License:** [MIT](https://tlo.mit.edu/understand-ip/exploring-mit-open-source-license-comprehensive-guide)
- **Finetuned from model:** [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large)

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://www.sbert.net/)
- **Repository:** [aisingapore/SEA-LION-E5-Embedding-600M](https://huggingface.co/aisingapore/SEA-LION-E5-Embedding-600M)

## Uses

SEA-LION-E5-Embedding-600M details one of the variants available within this collection. If you are deploying our models for your specific use case, we would love to hear from you! Please feel free to [contact us](mailto:sealion@aisingapore.org) to share your experience or explore potential collaborations.

| Model Variant | Model Repository | Suggesting Applications & Use Cases |
| --- | --- | --- |
| **Fine-tuned Embedding Models** | - [aisingapore/SEA-LION-E5-Embedding-600M](https://huggingface.co/aisingapore/SEA-LION-E5-Embedding-600M) <br> - [aisingapore/SEA-LION-ModernBERT-Embedding-300M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-Embedding-300M) <br> - [aisingapore/SEA-LION-ModernBERT-Embedding-600M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-Embedding-600M) | - Retrieval-Augmented Generation (RAG) <br> - Information retrieval, and search <br> - Similarity comparisons |
| **Pre-trained Encoder Models** | - [aisingapore/SEA-LION-ModernBERT-300M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-300M) <br> - [aisingapore/SEA-LION-ModernBERT-600M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-600M) <br> | - Fill mask <br>- Text classification <br> - Fine-tuning for downstream tasks (e.g., sentiment analysis, classification). |
| **Pre-trained Model Checkpoints** | - [aisingapore/SEA-LION-ModernBERT-300M-checkpoints](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-300M-checkpoints) <br> - [aisingapore/SEA-LION-ModernBERT-600M-checkpoints](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-600M-checkpoints) <br> | - Continued Pre-Training (CPT) <br> - Fine-tuning for downstream tasks (e.g., sentiment analysis, classification). |

## Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```
pip install -U sentence_transformers>=2.2.2
```
Then you can load this model and run inference.

```
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "aisingapore/SEA-LION-E5-Embedding-600M",
    prompts={
        "STS": "Instruct: Retrieve semantically similar text.\nQuery: ",
        "Clustering": "Instruct: Classify text into its appropriate category\nQuery: ",
        "Classification": "Instruct: Classify text into its appropriate category\nQuery: ",
        "Retrieval": "Instruct: Given a passage that is guaranteed to contain the answer, retrieve relevant passages that answer the query.\nQuery: ",
        "BitextMining": "Instruct: Retrieve parallel sentences.\nQuery: ",
        "PairClassification": "Instruct: Retrieve semantically similar text.\nQuery: ",
        "Reranking": "Instruct: Retrieve semantically similar text.\nQuery: ",
        "InstructionRetrieval": "Instruct: Given a instruction and a output, retrieve the most relevant output that answer the instruction.\nQuery: ",
        "MultiLabelTextClassification": "Instruct: Classify the given text into its appropriate classes\nQuery: ",
        "QARetrieval": "Instruct: Given a passage that is guaranteed to contain the answer, retrieve relevant passages that answer the query.\nQuery: ",
        "Summarization": "Instruct: Summarize the given text.\nQuery: "
    },
)

sentences = [
    "The weather is lovely today.",
    "อากาศวันนี้ดีมาก",
    "Dia berkendara ke stadion.",
]
embeddings = model.encode(sentences, prompt_name="STS")
print(embeddings.shape)
# [3, 1024]

similarities = model.similarity(embeddings, embeddings)
print(similarities)
#tensor([[1.0000, 0.8594, 0.5534],
#        [0.8594, 1.0000, 0.6343],
#        [0.5534, 0.6343, 1.0000]])
```
## Training Details

### Training Data

This model was tuned using a multi-stage training pipeline with the following datasets:

- **Contrastive Pre-training:** 245 million text pairs (EN-EN and EN-SEA) to enhance cross-lingual alignment.
- **Fine-tuning:** 13 million diverse text pairs (spanning EN-EN, CN-CN, EN-SEA, and SEA-SEA) to create the final fine-tuned model.

| **Language** | Percentage |
| --- | --- |
| EN-EN | 20% |
| CN-CN | 20% |
| EN-SEA | 10% |
| SEA-SEA | 50% |

### Training Procedure

#### Preprocessing

Following the foundational training, the model's cross-lingual alignment was substantially enhanced by undergoing contrastive pre-training utilising 245 million text pairs, specifically focusing on English-to-English and English-to-Southeast Asian language mappings (EN-EN and EN-SEA). Finally, to ensure the model could effectively follow user instructions and handle complex interactions, it was instruction-tuned using a diverse dataset of 13 million text pairs spanning EN-EN, CN-CN, EN-SEA, and SEA-SEA, culminating in the final highly capable instruction-tuned model.

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model is evaluated across three primary benchmark suites to provide a comprehensive assessment of embedding quality across Southeast Asian, Chinese, and English contexts:

- **SEA-BED (Southeast Asia Embedding Benchmark)** (<https://arxiv.org/pdf/2508.12243>): The primary testing suite, consisting of 169 datasets across 10 Southeast Asian languages (Burmese, Filipino, Indonesian, Khmer, Malay, Lao, Tamil, Tetum, Thai, and Vietnamese). Notably, 71% of these datasets are native-authored or human-curated to preserve regional linguistic properties.
- **CMTEB (Chinese Massive Text Embedding Benchmark)**: A specialised subset of MTEB focused on Chinese language tasks, used to evaluate performance in one of the region's most prominent scripts.
- **MTEB (Massive Text Embedding Benchmark)**: The industry-standard global benchmark used to gauge general-purpose English embedding performance across a wide array of tasks.

### Results

For details on Performance comparison of embedding models on SEA-BED, please refer to the [SEA-HELM](https://leaderboard.sea-lion.ai/embedding/SEA).

## Environmental Impact

Carbon emission was estimated using the fact sheet from TRG [Datacenters](https://www.trgdatacenters.com/resource/h200-power-consumption/).

- **Hardware Type:** Nvidia H200 140GB GPUs
- **Hours used:** 896 hrs
- **Cloud Provider:** SMC H200
- **Compute Region:** Singapore
- **Carbon Emitted:** appx. 252.13 kg CO2 e

## Technical Specifications

### Model Architecture and Objective

SEA-LION-E5-Embedding-600M is an encoder-only model based on XLM-R Large with E5-style contrastive pre-training and mean pooling.

| Parameter | SEA-LION-E5-Embedding-600M |
| --- | --- |
| **d_model** | 1024 |
| **head_dim** | 16 |
| **Vocabulary** | 250,000 (SentencePiece) |
| **Sequence Length** | 512 |
| **Pooling Mode** | Mean tokens (with attention mask) |

## Glossary

- **E5:** "EmbEddings from bidirEctional Encoder rEpresentations" – a weakly-supervised contrastive pre-training method for text embeddings.
- **SEA-BED:** Southeast Asia Embedding Benchmark – a comprehensive evaluation suite for embedding models on SEA languages.
- **Asymmetric Retrieval:** Retrieval tasks where query and document formulations differ; E5 uses prefixes to handle this.
- **Mean Pooling:** Aggregating token embeddings by averaging (weighted by attention mask) to produce a fixed-size sentence representation.

## More Information

While this model supports masked language modeling, it is primarily optimised via contrastive fine-tuning for downstream tasks such as sequence classification, token classification, or question answering. Please note that these weights have not been specifically aligned for safety; therefore, developers should implement their own safety evaluations and security measures. The authors disclaim all liability for any claims, damages, or other liabilities arising from the use of the released code or weights.

For more info, please contact us at [sealion@aisingapore.org](mailto:sealion@aisingapore.org)

