# SEA-LION

SEA-LION is a collection of LLMs which has been pretrained and instruct-tuned for the South-East Asia (SEA) region.
The models range from 3 billion to 7 billion parameters.
SEA-LION stands for <i>South-East Asia Languages In One Network</i>.


## Model Details

### Model Description

The SEA-LION model is a significant leap forward in the field of natural language processing and understanding,
specifically trained to understand South-East Asia (SEA) regional context.

The SEA-LION model comes in two variants, one with 3 billion parameters and another with 7 billion parameters.
Both variants are built on the robust MPT architecture and utilize a vocabulary size of 256K.

The model employs our proprietary SEABPETokenizer for tokenization.
Our SEABPETokenizer is specially tailored for SEA languages, ensuring optimal model performance.

The training data for SEA-LION is encompasses 1 trillion tokens.

- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Model type:** Decoder
- **Language(s) (NLP):** English, Chinese, Indonesian, Malay, Thai, Vietnamese, Filipino, Tamil, Burmese, Khmer, Lao
- **License:** MIT License


## How to Get Started with the Model

Please see the `examples` folder for code samples.


## Training Details

### Training Data

SEA-LION was trained on 980B tokens of the following data:

| Data Source            | Tokens | Percentage |
|------------------------|-------:|:----------:|
| RefinedWeb - English   | 571.3B |     62.80% |
| mC4 - Chinese          |  91.2B |     10.03% |
| mC4 - Indonesian       |   3.6B |      0.40% |
| mC4 - Malay            |   0.7B |      0.08% |
| mC4 - Filipino         |   1.3B |      0.15% |
| mC4 - Burmese          |   1.2B |      0.13% |
| mC4 - Vietnamese       |  63.4B |      6.97% |
| mC4 - Thai             |  10.8B |      1.19% |
| mC4 - Lao              |   0.3B |      0.03% |
| mC4 - Khmer            |   0.9B |      0.11% |
| mC4 - Tamil            |   2.5B |      0.28% |
| Python                 |  20.9B |      2.30% |
| Javascript             |  55.6B |      6.11% |
| Shell                  |   1.3B |      0.14% |
| SQL                    |   6.4B |      0.70% |
| Markdown               |  26.6B |      2.91% |
| StackExchange          |  21.2B |      2.33% |
| ArXiv                  |  30.6B |      3.35% |

### Training Infrastructure

#### Hardware

| Training Details     | SEA-LION 3B  | SEA-LION 7B  |
|----------------------|:------------:|:------------:|
| AWS EC2 p4d.24xlarge | 30 instances | 32 instances |
| Nvidia A100 40GB GPU | 240          | 256          |
| Training Duration    | 14 days      | 22 days      |


#### Software

SEA-LION was trained using MosaicML Composer using PyTorch
FullyShardedDataParallelism (FSDP).



#### Training HyperParameters

| HyperParameter    | SEA-LION 3B        | SEA-LION 7B        |
|-------------------|:------------------:|:------------------:|
| Precision         | bfloat16           | bfloat16           |
| Optimizer         | decoupled_adamw    | decoupled_adamw    |
| Scheduler         | cosine_with_warmup | cosine_with_warmup |
| Learning Rate     | 1.6e-4             | 6e-5               |
| Global Batch Size | 1200               | 2048               |
| Micro Batch Size  | 5                  | 4                  |


## Evaluation

| Model       | Average |  ARC  | HellaSwag |  MMLU | TruthfulQA |
|-------------|:-------:|:-----:|:---------:|:-----:|:----------:|
| SEA-LION 3B |  40.35  | 36.26 |   64.60   | 24.07 |   36.47    |
| SEA-LION 7B |  42.60  | 39.93 |   68.51   | 26.87 |   35.09    |


## Technical Specifications

### Model Architecture and Objective

SEA-LION is a decoder model using the MPT architecture.

| Parameter       | SEA-LION 3B | SEA-LION 7B |
|-----------------|:-----------:|:-----------:|
| Layers          | 32          | 32          |
| d_model         | 2560        | 4096        |
| head_dim        | 20          | 32          |
| Vocabulary      | 256000      | 256000      |
| Sequence Length | 2048        | 2048        |



## The Team

Hamsawardhini Rengarajan<br>
Lam Zhiwen Clarence<br>
Leong Weiqi<br>
Li Yier<br>
Liu Darius<br>
Lovenia Holy<br>
Ng Raymond<br>
Ngui Jian Gang<br>
Ong Tat-Wee David<br>
Railey Montalan<br>
Tai Ngee Chia<br>
Tan Choon Meng<br>
Thanh Ngan Nguyen<br>
Teo Jin Howe<br>
Teo Wei Yi<br>
William Tjhi<br>
Yeo Yeow Tong<br>
Yong Xianbin<br>
Yosephine<br>
Leslie Teo<br>

## Model Card Contact

For more info, please contact us at seallm@aisingapore.org


