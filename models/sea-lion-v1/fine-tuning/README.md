# SEA-LION QLoRA Fine-Tuning Guide
The following is a fine-tuning example using the SEA-LION-v1-7B model and the `Abzu/dolly_hhrlhf` dataset.

## Tested setup
This guide was tested on a machine containing 8× A100(40GB) GPUs.

## Running the fine tuning code
### Installing python packages
The required environment can be created by running the following codes
``` bash
conda create -n sealion_sft python==3.10.12
pip install -r requirements.txt

# Install flash attention
pip install flash-attn==2.5.3
```

### Setting up the accelerate library
As the accelerate library is used, please ensure that the accelerate configuration has been setup. This can be done by running:
``` bash
accelerate config
```

### Modifying the training parameters
The training parameters such as the learning rate, batch size and LoRA parameters can be modified in the `train_config.yaml` file.

### Training the model
Once the accelerate configuration and the training configuration yaml file is setup, the training can be started by running:
``` bash
accelerate launch qlora_fine_tuning.py --config_path="train_config.yaml"
```

## Training notes
### Gradient checkpointing
If the model is able to fit in GPU memory without gradient checkpointing, it is recommended to set `gradient_checkpointing: False` in the `train_config.yaml` file as this would result in a speed up in the training time. However, for larger models 

### Prompt format
In our limited testing, we identified that the following prompt format works best for our use case. However, this is still an active area of experimentation and may change in the future.
```
### USER:\n{prompt}\n\n### RESPONSE:\n{response}
```