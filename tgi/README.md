# Text Generation Inference (TGI)

## Build TGI 1.3.2 image with customised `MPTForCausalLM` class to support Sealion

Original `MPTForCausalLM` class can be found at
https://github.com/huggingface/text-generation-inference/blob/2a13f1a04682f43e48aea1f2378d1e32ee726256/server/text_generation_server/models/custom_modeling/mpt_modeling.py

```bash
cd sealion/tgi

docker image build -t sealion-tgi-image .
```

## Deploy Sealion model (e.g. sealion7b-instruct-nc) with TGI 1.3.2

Number of shards (`num-shard`) must be 1 at the moment.

```bash
model=aisingapore/sealion7b-instruct-nc
volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run

docker run -d --gpus '"device=0"' --shm-size 1g -p 8080:80 \
-v $volume:/data \
--name sealion_tgi_container \
sealion-tgi-image \
--model-id $model \
--trust-remote-code \
--dtype bfloat16 \
--num-shard 1
```

## Test Inference

Request

```bash
curl 127.0.0.1:8080/generate \
    -X POST \
    -d '{"inputs":"### USER:\nApa sentimen dari kalimat berikut ini?\nKalimat: Buku ini sangat membosankan.\nJawaban: \n\n### RESPONSE:\n","parameters":{"max_new_tokens":256,"repetition_penalty":1.2,"eos_token_id":1,"do_sample":false}}' \
    -H 'Content-Type: application/json' 
```

Result

```bash
{"generated_text":"Negatif"}
```

Cleanup
```bash
docker container rm -f sealion_tgi_container
```

## Performance Analysis using TGI benchmarking tool

Hardware: 1 instance of GCP VM
|Machine type| 	GPUs| 	GPU memory| 	Available vCPUs| 	Available memory|
|------------|------|-------------|--------------------|--------------------|
|a2-highgpu-8g| 	8 GPUs| 	320 GB|  	96 vCPUs| 	680 GB|


Copy `PreTrainedTokenizerFast` tokenizer files to model cache directory
```bash
sudo cp ../tokenizer/sealion_fasttokenizer/* $volume/models--aisingapore--sealion7b-instruct-nc/snapshots/9869033e74f2ae74499e96a6267bd42bd6aac511/
```

Deploy Sealion model (e.g. sealion7b-instruct-nc) with TGI 1.2.

Note: There is an error from `text-generation-benchmark` tool when used with `--top-n-tokens` flag with TGI 1.3. So TGI 1.2 is used instead.

```bash
docker run -d --gpus '"device=0"' --shm-size 1g \
-v $volume:/data \
-v $PWD/custom_modeling/mpt_modeling.py:/opt/conda/lib/python3.10/site-packages/text_generation_server/models/custom_modeling/mpt_modeling.py \
--name sealion_tgi_container \
ghcr.io/huggingface/text-generation-inference:1.2 \
--model-id $model \
--trust-remote-code \
--dtype bfloat16 \
--num-shard 1
```

Run benchmarking tool (`text-generation-benchmark`)

```bash
docker exec -it sealion_tgi_container \
text-generation-benchmark \
--tokenizer-name /data/models--aisingapore--sealion7b-instruct-nc/snapshots/9869033e74f2ae74499e96a6267bd42bd6aac511 \
--repetition-penalty=1.2 \
--top-n-tokens=256
```

Result
```
| Parameter          | Value                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------|
| Model              | /data/models--aisingapore--sealion7b-instruct-nc/snapshots/9869033e74f2ae74499e96a6267bd42bd6aac511 |
| Sequence Length    | 10                                                                                                  |
| Decode Length      | 8                                                                                                   |
| Top N Tokens       | Some(256)                                                                                           |
| N Runs             | 10                                                                                                  |
| Warmups            | 1                                                                                                   |
| Temperature        | None                                                                                                |
| Top K              | None                                                                                                |
| Top P              | None                                                                                                |
| Typical P          | None                                                                                                |
| Repetition Penalty | Some(1.2)                                                                                           |
| Watermark          | false                                                                                               |
| Do Sample          | false                                                                                               |


| Step           | Batch Size | Average   | Lowest    | Highest   | p50       | p90       | p99       |
|----------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Prefill        | 1          | 36.38 ms  | 35.92 ms  | 36.92 ms  | 36.38 ms  | 36.92 ms  | 36.92 ms  |
|                | 2          | 40.76 ms  | 40.30 ms  | 41.63 ms  | 40.80 ms  | 41.63 ms  | 41.63 ms  |
|                | 4          | 47.21 ms  | 46.95 ms  | 47.71 ms  | 47.17 ms  | 47.71 ms  | 47.71 ms  |
|                | 8          | 61.56 ms  | 60.51 ms  | 62.92 ms  | 61.36 ms  | 62.92 ms  | 62.92 ms  |
|                | 16         | 89.59 ms  | 88.15 ms  | 90.67 ms  | 89.68 ms  | 90.67 ms  | 90.67 ms  |
|                | 32         | 152.34 ms | 151.31 ms | 153.90 ms | 152.37 ms | 153.90 ms | 153.90 ms |
| Decode (token) | 1          | 31.94 ms  | 31.75 ms  | 32.30 ms  | 31.95 ms  | 31.75 ms  | 31.75 ms  |
|                | 2          | 35.58 ms  | 35.42 ms  | 35.77 ms  | 35.63 ms  | 35.73 ms  | 35.73 ms  |
|                | 4          | 41.90 ms  | 41.58 ms  | 42.33 ms  | 41.91 ms  | 41.58 ms  | 41.58 ms  |
|                | 8          | 55.43 ms  | 54.58 ms  | 55.99 ms  | 55.39 ms  | 55.94 ms  | 55.94 ms  |
|                | 16         | 81.11 ms  | 80.37 ms  | 82.78 ms  | 80.97 ms  | 81.51 ms  | 81.51 ms  |
|                | 32         | 133.92 ms | 133.01 ms | 134.57 ms | 133.99 ms | 134.57 ms | 134.57 ms |
| Decode (total) | 1          | 223.60 ms | 222.26 ms | 226.11 ms | 223.62 ms | 222.26 ms | 222.26 ms |
|                | 2          | 249.08 ms | 247.96 ms | 250.39 ms | 249.43 ms | 250.09 ms | 250.09 ms |
|                | 4          | 293.32 ms | 291.09 ms | 296.32 ms | 293.39 ms | 291.09 ms | 291.09 ms |
|                | 8          | 388.00 ms | 382.08 ms | 391.92 ms | 387.76 ms | 391.57 ms | 391.57 ms |
|                | 16         | 567.77 ms | 562.57 ms | 579.48 ms | 566.79 ms | 570.55 ms | 570.55 ms |
|                | 32         | 937.43 ms | 931.11 ms | 942.02 ms | 937.96 ms | 942.02 ms | 942.02 ms |


| Step    | Batch Size | Average            | Lowest             | Highest            |
|---------|------------|--------------------|--------------------|--------------------|
| Prefill | 1          | 27.49 tokens/secs  | 27.09 tokens/secs  | 27.84 tokens/secs  |
|         | 2          | 49.07 tokens/secs  | 48.04 tokens/secs  | 49.63 tokens/secs  |
|         | 4          | 84.73 tokens/secs  | 83.84 tokens/secs  | 85.20 tokens/secs  |
|         | 8          | 129.96 tokens/secs | 127.15 tokens/secs | 132.22 tokens/secs |
|         | 16         | 178.61 tokens/secs | 176.47 tokens/secs | 181.50 tokens/secs |
|         | 32         | 210.06 tokens/secs | 207.93 tokens/secs | 211.48 tokens/secs |
| Decode  | 1          | 31.31 tokens/secs  | 30.96 tokens/secs  | 31.50 tokens/secs  |
|         | 2          | 56.21 tokens/secs  | 55.91 tokens/secs  | 56.46 tokens/secs  |
|         | 4          | 95.46 tokens/secs  | 94.49 tokens/secs  | 96.19 tokens/secs  |
|         | 8          | 144.34 tokens/secs | 142.89 tokens/secs | 146.57 tokens/secs |
|         | 16         | 197.28 tokens/secs | 193.28 tokens/secs | 199.09 tokens/secs |
|         | 32         | 238.95 tokens/secs | 237.79 tokens/secs | 240.57 tokens/secs |

```

Cleanup
```bash
docker container rm -f sealion_tgi_container
```
