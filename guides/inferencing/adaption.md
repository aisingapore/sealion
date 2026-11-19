# Adaption Inference — Quickstart Guide

The following SEA-LION models are now available on Adaption's inference service.

Please follow these steps to sign up with Adaption, create an API key, and call a model.

| **Model ID**            | **Base model**              |
|-------------------------|-----------------------------|
| nemotron-SEA-LION-v4.8-120b-a12b | [Nemotron SEA-LION v4.8 120B](/models/sea-lion-v4.8/nemotron-sea-lion-v4.8.md) |
| qwen397b-flashnext      | Qwen 397B FlashNext         |


## 1. Sign up

1. Go to [adaptionlabs.ai/app/auth](https://adaptionlabs.ai/app/auth) and create an account.
2. Verify your email address.


## 2. Create an API key

1. Open [**Settings → API keys**](https://adaptionlabs.ai/app/settings?tab=api_keys).
2. Create a key and copy it. You will not be able to view it again.
3. Export it as `ADAPTION_API_KEY`:

```bash
export ADAPTION_API_KEY="pt_live_..."
```


## 3. Call a model

Install the Python SDK (version 0.16.0 or later):

```bash
pip install adaption
```

Call `responses.create` with one of the model IDs above:

```python
from adaption import Adaption

 client = Adaption()  # reads ADAPTION_API_KEY

 response = client.responses.create(
     model="nemotron-SEA-LION-v4.8-120b-a12b",
     instructions="You are a helpful assistant.",
     input="Where is Lau Pa Sat? Tell me in a single sentence.",
 )

 print(response.output_text)
```