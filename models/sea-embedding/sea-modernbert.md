# SEA-LION-ModernBERT-300M/600M checkpoints and Embedding

Last update: 2026-03-16

**SEA-LION** is a collection of Large Language Models (LLMs) and encoders which have been pretrained and fine-tuned for the Southeast Asia (SEA) region.

<!-- Introduction -->
## Introduction
SEA-LION stands for *Southeast Asian Languages In One Network*. 

This encoder-only model leverages the advanced **ModernBERT** architecture combined with the Gemma 3 SentencePiece tokenizer. The adoption of the **Gemma 3 tokenizer** with ModernBERT allows the model to achieve highly efficient and culturally nuanced text processing. This combination significantly improves the tokenization fertility and compression rates for complex regional scripts and diverse Southeast Asian languages, enabling the model to handle longer context windows and cross-lingual tasks with greater computational efficiency.

To achieve this level of performance, the model was developed through a rigorous, multi-stage training pipeline. The foundation was established through extensive **pre-training on 2 Trillion (2T) tokens**, followed by a mid-training phase on an additional 1 Trillion (1T) tokens. Both of these massive training phases comprehensively covered code alongside 13 specific languages: Burmese, Chinese, English, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Sundanese, Tamil, Thai, and Vietnamese.

## Model Details

### Model Description

The SEA-LION-ModernBERT-based models are built on the ModernBERT architecture and has a vocabulary size of 262K.

For tokenization, the model employs our custom [Gemma3](https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf) tokenizer, which has excellent performance for SEA languages, ensuring optimal model performance.

- **Developed by:** AI Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** AI Products Pillar, AI Singapore
- **Model type:** Encoder
- **Context length:** 8k
- **Languages:** Burmese, Chinese, English, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Sundanese, Tamil, Thai, and Vietnamese
- **License:** [MIT](https://tlo.mit.edu/understand-ip/exploring-mit-open-source-license-comprehensive-guide)

### Model Sources

- **Repository:** The weights for this model and its various training stages are being released to support transparency, research, and diverse downstream applications. **[Link to HF Repo](https://huggingface.co/collections/aisingapore/sea-lion-modernbert-and-embedding)**

## Uses

This model card details one of the variants available within this ModernBERT-based collection.

| Model Variant | Model Repository | Suggesting Applications & Use Cases |
| --- | --- | --- |
| **Fine-tuned Embedding Models** | - [aisingapore/SEA-LION-E5-Embedding-600M](https://huggingface.co/aisingapore/SEA-LION-E5-Embedding-600M) <br> - [aisingapore/SEA-LION-ModernBERT-Embedding-300M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-Embedding-300M) <br> - [aisingapore/SEA-LION-ModernBERT-Embedding-600M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-Embedding-600M) | - Retrieval-Augmented Generation (RAG) <br> - Information retrieval, and search <br> - Similarity comparisons |
| **Pre-trained Encoder Models** | - [aisingapore/SEA-LION-ModernBERT-300M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-300M) <br> - [aisingapore/SEA-LION-ModernBERT-600M](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-600M) <br> | - Fill mask <br>- Text classification <br> - Fine-tuning for downstream tasks (e.g., sentiment analysis, classification). |
| **Pre-trained Model Checkpoints** | - [aisingapore/SEA-LION-ModernBERT-300M-checkpoints](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-300M-checkpoints) <br> - [aisingapore/SEA-LION-ModernBERT-600M-checkpoints](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-600M-checkpoints) <br> | - Continued Pre-Training (CPT) <br> - Fine-tuning for downstream tasks (e.g., sentiment analysis, classification). |

The checkpoints repository contains available of model variants.

| Model Variant | Suggesting Applications & Use Cases |
| --- | --- |
| stage1-pre-training/SEA-LION-PT-300M.pt | Composer checkpoint from the **Pre-Training Stage** suitable for continued pre-training (CPT). |
| stage1-pre-training/SEA-LION-PT-300M | Folder for the HuggingFace checkpoints from the **Pre-Training Stage**, suitable for continued pre-training or fine tuning. |
| stage2-mid-training/SEA-LION-MT-300M-w-decay.pt | Composer checkpoint from the **Mid-Training stage** with learning rate annealing suitable for fine tuning with learning rate warmup. |
| stage2-mid-training/SEA-LION-MT-300M-wo-decay.pt | Composer checkpoint from the **Mid-Training stage** without learning rate annealing suitable for continued pre-training (CPT) and fine tuning without learning rate warmup. |
| stage2-mid-training/SEA-LION-MT-300M-wo-decay | Folder for the HuggingFace checkpoints from the **Mid-Training stage** without learning rate annealing. suitable for continued pre-training (CPT) and fine tuning without learning rate warmup. |

Note: For stage2-mid-train*ing checkpoints with learning rate annealing, please refer to* [*aisingapore/SEA-LION-ModernBERT-300M*](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-300M) and [*aisingapore/SEA-LION-ModernBERT-600M*](https://huggingface.co/aisingapore/SEA-LION-ModernBERT-600M)

*Note: If you are deploying our models for your specific use case, we would love to hear from you! Please feel free to* [*contact us*](mailto:sealion@aisingapore.org) *to share your experience or explore potential collaborations.*

### Bias, Risks, and Limitations

The model was not tested for robustness against adversarial usage. It is important for users to be aware that our model exhibits certain limitations that warrant consideration. Users should also exercise caution in continue-implementing and validating the model's responses due to the potential inconsistencies.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

## How to Get Started with the Model

Use the code below to download the model locally.

```
pip install -U transformers>=4.48.0
```

```
#########################
## Download checkpoints locally for continued pre-training or fine tuning
#########################
from huggingface_hub import snapshot_download

# Download the stage-1-pre-training Huggingface checkpoint
snapshot_download(
  "aisingapore/SEA-LION-ModernBERT-300M-checkpoints",
  repo_type="model",
  allow_patterns=["stage1-pre-training/SEA-LION-PT-300M/*"],
  local_dir="checkpoints"
)

# Download the stage-1-pre-training Composer checkpoint
snapshot_download(
  "aisingapore/SEA-LION-ModernBERT-300M-checkpoints",
  repo_type="model",
  allow_patterns=["stage1-pre-training/SEA-LION-PT-300M.pt"],
  local_dir="checkpoints"
)
```

```
import torch
from transformers import pipeline

pipeline = pipeline(
    task="fill-mask",
    model="checkpoints/stage1-pre-training/SEA-LION-PT-300M", # loading from local folder
    dtype=torch.float16,
    device=0
)
pipeline("Plants create  through a process known as photosynthesis.")
```
*Note: To get started with Continued Pre-Training of the Composer checkpoints, we recommend refering to this [guide](https://huggingface.co/blog/thomas-sounack/bioclinical-modernbert-tutorial).*

---

## Training Details

The models are pre-trained from scratch through a two-phase pipeline, beginning with an extensive initial stage on 2 trillion tokens, followed by a mid-training phase on an additional 1 trillion tokens. Both phases incorporated a diverse dataset covering programming code and 13 languages: Burmese, Chinese, English, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Sundanese, Tamil, Thai, and Vietnamese.

### Training Data

The pre-trained checkpoints were pre-trained from scratch on a number of trillion tokens corpus with the following linguistic and thematic distribution:

| Data Source | Percentage |
| --- | --- |
| code | 10% |
| EN - English | 35% |
| ID - Indonesian | 8% |
| JV - Javanese | 0.5% |
| KM - Khmer | 1.5% |
| LO - Lao | 0.5% |
| MS - Malay | 4.75% |
| MY - Burmese | 1.75% |
| SU - Sundanese | 0.5% |
| TA - Tamil | 4.5% |
| TH - Thai | 8% |
| TL - Filipino | 2.5% |
| VI - Vietnamese | 8.5% |
| ZH - Chinese | 14% |

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model is evaluated across three primary benchmark suites to provide a comprehensive assessment of embedding quality across Southeast Asian, Chinese, and English contexts:

- [**SEA-BED (Southeast Asia Embedding Benchmark)**](<https://arxiv.org/pdf/2508.12243>): The primary testing suite, consisting of 169 datasets across 10 Southeast Asian languages (Burmese, Filipino, Indonesian, Khmer, Malay, Lao, Tamil, Tetum, Thai, and Vietnamese). Notably, 71% of these datasets are native-authored or human-curated to preserve regional linguistic properties.
- **CMTEB (Chinese Massive Text Embedding Benchmark)**: A specialised subset of MTEB focused on Chinese language tasks, used to evaluate performance in one of the region's most prominent scripts.
- **MTEB (Massive Text Embedding Benchmark)**: The industry-standard global benchmark used to gauge general-purpose English embedding performance across a wide array of tasks.


## Results

For details on Performance comparison of embedding models on SEA-BED, please refer to the [SEA-HELM](https://leaderboard.sea-lion.ai/embedding/SEA).

## Environmental Impact

Carbon emission was estimated using the fact sheet from TRG [Datacenters](https://www.trgdatacenters.com/resource/h200-power-consumption/).

- **Hardware Type:** Nvidia H200 140GB GPUs
- **Hours used:** 1,825 GPU hours
- **Cloud Provider:** SMC H200
- **Compute Region:** Singapore
- **Carbon Emitted:** appx. 513.27 kg CO2 e

## Technical Specifications

### Model Architecture and Objective

SEA-LION-ModernBERT-300M is an encoder model using the ModernBERT architecture.

| Parameter | SEA-LION-ModernBERT |
| --- | --- |
| Layers | 22  |
| d_model | 768  |
| head_dim | 12 |
| Vocabulary | 262144 |
| Sequence Length | 8k |

## More Information

This is the repository for the commercial fine-tuned model. The model has *not* been aligned for safety. Developers and users should perform their own safety fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.

For more info, please contact us at [sealion@aisingapore.org](mailto:sealion@aisingapore.org)
