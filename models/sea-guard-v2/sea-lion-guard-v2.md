## SEA-LION-Guard-v2 Model Overview

**SEA-LION-Guard-v2** is our next-generation suite of action governance and safety models tailored specifically for the Southeast Asian AI ecosystem. Moving beyond standard binary content filtering, the v2 suite introduces real-time **Action Governance**, **Bring Your Own Policy (BYOP)** enforcement, and deep **Multi-Turn Context Evaluation** across 8 core regional languages (Burmese, English, Filipino, Indonesian, Malay, Tamil, Thai, and Vietnamese).

### The Gemma-SEA-LION-Guard-v2 Collection

The v2 collection offers scalable parameters and context windows designed for diverse deployment requirements—from edge agent execution to enterprise cloud governance:

- **[Gemma-SEA-LION-Guard-31B/E4B/E2B-v2](./gemma-sea-lion-guard-v2.md)** (`https://huggingface.co/collections/aisingapore/sea-lion-guard-v2`) is a lightweight **31B, E4B and E2B parameter model** with **256K context window** for 31B and **128K context window** for E4B and E2B. Optimized for ultra-low latency, it acts as an efficient edge guardrail for real-time tool interception and rapid API checks.

### Key Enhancements in v2

Compared to legacy moderation models, Gemma-SEA-LION-Guard-v2 shifts from freeform string generation to type-safe, calibrated decision probabilities across three fields:

1. **`content_moderation`**: Categorical probability distribution across `"safe"`, `"sensitive"`, and `"unsafe"` tiers (summing to 1.0).
2. **`rule_applicability`**: Predicate relevance score ($0.0 - 1.0$) indicating whether a custom BYOP policy applies to the interaction.
3. **`rule_violation`**: Calibrated probability score ($0.0 - 1.0$) quantifying the likelihood of a policy breach to enable real-time tool call abortion before execution.

### Our Commitment to Safe Regional AI
     
Gemma-SEA-LION-Guard-v2 empowers developers, enterprises, and public sector organizations across Southeast Asia to deploy autonomous agents with confidence. By providing structured, calibrated decision outputs, these models ensure AI systems remain culturally aligned, policy-compliant, and secure against emerging agentic risks.

> **Note:** For integration examples using OpenAI-compatible Decisions APIs, local `vllm` deployment scripts, and benchmark results on **SEA-SafeguardBench**, please refer to the individual model documentation pages linked above.