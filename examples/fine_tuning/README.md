# Running the supervised fine tuning code
The supervised fine tuning code uses the accelerate library to launch the training:
``` python
accelerate launch supervised_fine_tuning.py --config_path="train_config.yaml"
```

