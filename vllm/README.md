# vLLM

## Clone and checkout vLLM git repo version 0.2.6

```bash
cd sealion/vllm

git clone https://github.com/vllm-project/vllm.git
cd vllm
git checkout v0.2.6

cd ..
```

## Build vLLM 0.2.6 from source with customised `MPTForCausalLM` class to support Sealion

Original `MPTForCausalLM` class can be found at https://github.com/vllm-project/vllm/blob/v0.2.6/vllm/model_executor/models/mpt.py

```bash
cp models/mpt.py vllm/vllm/model_executor/models/mpt.py
```

vLLM recommends using the NVIDIA PyTorch Docker image if there is trouble building vLLM from your host.

```bash
# Use `--ipc=host` to make sure the shared memory is large enough.

docker run --gpus '"device=0"' -it --ipc=host \
-v $PWD/vllm:/workspace/vllm \
-v ~/.cache:/root/.cache \
nvcr.io/nvidia/pytorch:23.10-py3
```

You will now arrive at the container shell.

Upgrade pip
```bash
python -m pip install --upgrade pip
```

Upgrade `torchdata`, `torchtext` and `torchvision` python modules
```bash
pip install --upgrade torchdata torchtext torchvision
```

Build vLLM
```bash
cd vllm
pip install -e .
```

## Test Inference

Start Python shell
```bash
python
```

Create LLM
```python
import math
from vllm import SamplingParams, LLM

d_model = 4096

def scale_logits(token_ids, logits):
    logits = logits * (1 / math.sqrt(d_model))
    return logits

# Create an LLM.
llm = LLM(
    model="aisingapore/sealion7b",
    trust_remote_code=True,
)
```

Use LLM to generate text from prompts.
```python
# Sample prompts.
prompts = [
    "Hello, my name is John and I am a",
    "Singapore is",
]
# Create a sampling params object.
sampling_params = SamplingParams(
    temperature=0,
    repetition_penalty=1.2,
    logits_processors=[scale_logits],
    max_tokens=64,
)

# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

Result
```bash
Prompt: 'Hello, my name is John and I am a', Generated text: ' 20 year old student at the University of California in Santa Barbara.\nI have been playing guitar for about three years now but only started to take it seriously around two months ago when i bought an electric guitar from Guitar Center (a gift). My main influences are: Jimi Hendrix, Eric Clapton, Stevie Ray Vaughan'

Prompt: 'Singapore is', Generated text: ' a great place to visit.\nThe country has many beautiful places and attractions that you can enjoy with your family or friends, such as the Gardens by The Bay in Marina Bay Sands which are located on top of an artificial island near downtown area; Sentosa Island where there’s Universal Studios theme park for kids who love adventure'
```

Exit Python shell
```bash
quit()
```

Exit and stop container
```bash
exit
```