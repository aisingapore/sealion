# Deployment using vLLM on Linux Server 

The following guide explains the procedures for deploying a SEA-LION model on a Linux server.

## Prerequisites
- OS: Linux
- Python: 3.9-3.12
- vLLM version: 0.10.1.1
- uv 0.7.x installed
- CUDA drivers version 12 installed

## Environment Setup
To get started, you will need to create an environment and install vLLM. The steps below outline how to install and use **uv** as the package manager, and then proceeding to install vLLM.

1. Navigate to the desired base directory. In this guide, the base folder is assumed to be `/home/sealion-user`.
```bash
cd /home/sealion-user
```

2. Create a new working directory and enter it
```bash
mkdir sealion_test && cd sealion_test
```

3. Initialize uv
```bash
uv init
```

4. Add the vllm dependency
```bash
uv add vllm
```

5. Clone vllm github repository and rename the top-level directory to `vllm_code`. The renaming is necessary to prevent Python from importing modules from the vllm repository directory instead of the packages installed in the environment.
```bash
git clone https://github.com/vllm-project/vllm.git && mv vllm vllm_code
```

## Model Deployment using vLLM
The steps below outline how to host a vLLM service using GPUs.

1. Navigate to working directory and activate environment:
```bash
cd /home/sealion-user/sealion_test && source/.venv/bin/activate
```

2. Set relevant values of environment variables. It is necessary to set VLLM_CACHE_ROOT to prevent errors arising from insufficient disk space as a result of using the default vLLM cache directory:
```bash
export CUDA_VISIBLE_DEVICES=0
export VLLM_CACHE_ROOT=/home/sealion-user/sealion_test/
```

3. Start the server with the desired model. The `aisingapore/Gemma-SEA-LION-v4-27B-IT` model is used in this example.
```bash
python -m vllm.entrypoints.openai.api_server --model aisingapore/Gemma-SEA-LION-v4-27B-IT
```

Alternatively, the server can be started with the below command:
```bash
vllm serve aisingapore/Gemma-SEA-LION-v4-27B-IT
```

4. Create a python script `main.py` similar to the following:
```bash
import requests

response = requests.post(
    "http://localhost:8000/v1/completions",
    headers={"Content-Type": "application/json"},
    json={
        "model": "aisingapore/Gemma-SEA-LION-v4-27B-IT",
        "prompt": "Prove or give a counter-example of the Birch and Swinnerton-Dyer conjecture.",
        "max_tokens": 3200,
        "temperature": 0.7,
    }
)
print(response.json())
```

5. Run the python script. The following assumes it is called `main.py`.
```bash
python main.py
```
You can also query the model with input prompts using curl method: 
```bash
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "aisingapore/Gemma-SEA-LION-v4-27B-IT",
        "prompt": "Prove or give a counter-example of the Birch and Swinnerton-Dyer conjecture.",
        "max_tokens": 3200,
        "temperature": 0.7
    }'
```
The output obtained should be similar to the following:

```bash
{'id': 'cmpl-7f41c8ff4bc9428e91505548b508747a', 'object': 'text_completion', 'created': 1755826519, 'model': 'aisingapore/Gemma-SEA-LION-v4-27B-IT', 'choices': [{'index': 0, 'text': '\n\nThe Birch and Swinnerton-Dyer (BSD) conjecture is one of the most important unsolved problems in mathematics. It relates the arithmetic of an elliptic curve to the analytic behavior of its L-function.\n\n**Statement of the Conjecture:**\n\nLet E be an elliptic curve defined over the rational numbers. Let L(E, s) be the L-function of E, which is a complex function defined for Re(s) > 1 by an Euler product.  The L-function can be analytically continued to the entire complex plane.\n\nThe conjecture states that:\n\n1. **The L-function L(E, s) has a pole at s = 1 if and only if E(Q) is finite.**  In other words, the L-function has a simple pole at s=1 if and only if the elliptic curve has finitely many rational points. If E(Q) is infinite, the L-function is analytic at s=1.\n\n2. **If the L-function has a pole at s = 1, the order of the pole is equal to the rank of the Mordell-Weil group E(Q).**  The rank of E(Q) is the dimension of the Mordell-Weil group, which measures the number of independent points of infinite order on the elliptic curve.\n\n3. **A precise formula relating the leading coefficient of the Taylor series of L(E, s) at s = 1 to several arithmetic invariants of E.** Specifically, if r is the rank of E(Q), then\n\n   lim_{s → 1} (s - 1)^r L(E, s) =  Ω_E * R_E *  ∏_{p | N} c_p *  |Sha(E)| / |E(Q)_{tor}|^2\n\n   where:\n    * Ω_E is the real period of E.\n    * R_E is the regulator of E.\n    * N is the conductor of E.\n    * c_p are the Tamagawa numbers at the primes p dividing N.\n    * Sha(E) is the Tate-Shafarevich group of E, which measures the failure of the Hasse principle.\n    * E(Q)_{tor} is the torsion subgroup of E(Q).\n\n**Status of the Conjecture:**\n\n* **Unproven:** The BSD conjecture remains unproven in general. It is considered one of the seven Millennium Prize Problems, with a $1 million reward for a correct proof.\n* **Partial Results:** Significant progress has been made:\n    * **Kolyvagin (1988):** Proved that if E has rank 0, then L(E, s) has a simple pole at s = 1.\n    * **Gross-Zagier (1986):** Proved the first half of BSD for elliptic curves with complex multiplication (CM curves). This result established the connection between the arithmetic invariants and the analytic behavior for a specific class of elliptic curves.\n    * **Rank 1 Curves:** Significant progress has been made towards proving BSD for rank 1 curves.\n    * **Taylor-Wiles-Katz:** Established modularity theorems, which are crucial for understanding the L-functions of elliptic curves.\n\n**Counter-Example?**\n\nThere are **no known counter-examples** to the BSD conjecture.  All the evidence so far supports its validity. However, the conjecture is incredibly difficult to prove, and the complexity of the terms involved makes it a formidable challenge.\n\n**Why can\'t I "prove or give a counter-example"?**\n\nThe difficulty lies in the following:\n\n* **Calculating L(E, s):** Computing the L-function to a high enough degree of accuracy to determine its behavior at s=1 is extremely challenging, even for relatively simple elliptic curves.\n* **Determining the Rank:** Finding the rank of an elliptic curve is also a difficult problem.\n* **Tate-Shafarevich Group:** The Tate-Shafarevich group Sha(E) is notoriously hard to compute. It is conjectured to be finite for all elliptic curves, but this remains unproven.\n* **Complex Analytic Continuation:** Understanding the analytic continuation of the L-function is also a complex problem.\n\n**In conclusion:**\n\nThe Birch and Swinnerton-Dyer conjecture is a profound statement about the deep connection between arithmetic and analysis.  Despite decades of research, it remains unproven.  There are no known counter-examples, and considerable evidence supports its truth.  A proof (or disproof) would be a major breakthrough in number theory.  Therefore, I cannot provide a proof or a counter-example. The best I can do is state the conjecture and summarize its current status.\n', 'logprobs': None, 'finish_reason': 'stop', 'stop_reason': 106, 'prompt_logprobs': None}], 'service_tier': None, 'system_fingerprint': None, 'usage': {'prompt_tokens': 20, 'total_tokens': 1020, 'completion_tokens': 1000, 'prompt_tokens_details': None}, 'kv_transfer_params': None}
```

