# Triton Inference Server

## Build Triton Inference Server 23.12 image with customised `MPTForCausalLM` class to support Sealion

```bash
cd sealion/vllm

docker build -f triton_inference_server/Dockerfile -t sealion-vllm-triton-server-image .
```

## Deploy Sealion model (e.g. sealion7b) with Triton Inference Server 23.12

Number of tensor parallel replicas (`tensor-parallel-size`) in `model_repository/sealion7b/1/model.json` can only be 1 (default) at the moment.

```bash
cd triton_inference_server

sudo docker run -u triton-server -d --gpus '"device=0"' --net=host --shm-size=1G --ulimit memlock=-1 --ulimit stack=67108864 \
-v ${PWD}/model_repository:/opt/tritonserver/model_repository \
-v ~/.cache:/home/triton-server/.cache \
--name sealion_vllm_triton_server_container \
sealion-vllm-triton-server-image \
tritonserver --model-repository=model_repository
```

## Test Inference

Requests
```bash
curl -X POST localhost:8000/v2/models/sealion7b/generate \
-d '{"text_input": "Hello, my name is John and I am a", "parameters": {"sampling_parameters": "{\"temperature\": 0, \"repetition_penalty\": 1.2, \"max_tokens\": 64}"}}'

curl -X POST localhost:8000/v2/models/sealion7b/generate \
-d '{"text_input": "Singapore is", "parameters": {"sampling_parameters": "{\"temperature\": 0, \"repetition_penalty\": 1.2, \"max_tokens\": 64}"}}'
```

Results
```bash
{"model_name":"sealion7b","model_version":"1","text_output":"Hello, my name is John and I am a 20 year old student at the University of California in Santa Barbara.\nI have been playing guitar for about three years now but only started to take it seriously around two months ago when i bought an electric guitar from Guitar Center (a gift). My main influences are: Jimi Hendrix, Eric Clapton, Stevie Ray Vaughan"}

{"model_name":"sealion7b","model_version":"1","text_output":"Singapore is a great place to visit.\nThe country has many beautiful places and attractions that you can enjoy with your family or friends, such as the Gardens by The Bay in Marina Bay Sands which are one of my favorite spots when I was there last year! It’s also home to some amazing food like this delicious chicken rice"}
```

Cleanup
```bash
docker container rm -f sealion_vllm_triton_server_container
```