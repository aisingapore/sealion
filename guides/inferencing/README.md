# Run SEA-LION Models for Inferenceing
This section covers the various environments where SEA-LION models can be hosted, ranging from fully managed cloud services to self-hosted high-performance infrastructure. SEA-LION models are freely available for [download](/models/download_models.md). The following guides provide technical how-tos for setting up SEA-LION inference using different approaches:

1. [Using our provided SEA-LION API](./api.md)
2. Running SEA-LION on a local machine (coming soon)
3. Deploying SEA-LION on the cloud
    - [Google Vertex AI](./vertex_ai.md): Integration for deploying SEA-LION endpoint within Google Cloud’s unified AI platform, Google Vertex AI.
    - [Amazon Bedrock Custom Model Import](./amazon_bedrock.md): Step-by-step guide for importing and using Llama-SEA-LION weights into a serverless on-demand environment with Amazon Bedrock.
    - [Bedrock Access Gateway](./bedrock_access_gateway.md): A specialized bridge for secure, standardized access to Bedrock-hosted instances for such OpenAI-compatible APIs with Llama-SEA-LION models and Bedrock Access Gateway.
    - [AWS SageMaker](./Gemma-SEA-LION-v4-27B-Instruct.ipynb): Instructions for hosting SEA-LION on dedicated EC2 instances using SageMaker endpoints showing a deployment of Gemma-SEA-LION models on AWS Sagemaker AI.
    - [vLLM on Linux](./vllm_linux.md): A guide for self-hosting on-premises or in private clouds using the high-throughput vLLM engine for maximum performance of SEA-LION on Linux server.

