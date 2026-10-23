# SEA-HELM Audio

SEA-HELM Audio is a Southeast Asian (SEA) multilingual evaluation framework that extends the [text-based SEA-HELM benchmark](./sea-helm.md). It is designed to assess performance degradation in cascaded automatic speech recognition and large language model (ASR–LLM) pipelines. 

**SEA-HELM Audio** serves as a valuable resource for developers looking to deploy and evaluate voice agents, providing empirical baselines for how linguistic accuracy and instruction-following hold up when transitioning from text to spoken interactions. It currently covers *English, Indonesian, Malay, Tamil, and Chinese*.

## Motivations

### Limitations of Text-Only Benchmarks for Voice Agents
While Large Language Models (LLMs) continue to achieve high benchmark scores on written text, deploying these models within real-world voice pipelines introduces acoustic transcription errors, phonetic ambiguities, and domain-specific degradation. Existing spoken language benchmarks do not adequately capture Southeast Asian linguistic nuances. There was a critical need to systematically measure the impact of speech input on downstream LLM task performance across SEA languages.

### Quantifying the "Speech Gap"
To evaluate how voice interfaces bottleneck LLM reasoning, SEA-HELM Audio establishes a controlled framework to quantify the **Speech Gap** (Δ = Score_text − Score_speech). This absolute difference represents the "modality penalty," quantifying precisely how much task performance degrades due to transcription errors or missing acoustic signals.

## Core Pillars of SEA-HELM Audio

### 1. Spoken Prompt Construction
Because the original SEA-HELM contains only written prompts, SEA-HELM Audio natively creates spoken input. Each prompt is read aloud by a Text-to-Speech (TTS) synthesizer that plays the role of the user. To ensure authenticity, only the content a user would actually say is synthesized, and written conventions (like multiple-choice markers) are adapted so they read naturally aloud in each specific language.

### 2. Dual-Path Evaluation Flow
To isolate the exact cost of the speech front-end, each SEA-HELM prompt is evaluated in two parallel ways:
* **The Speech Path:** The text prompt is converted to speech via TTS, transcribed back to text by an ASR system, and the resulting transcript is answered by the LLM. 
* **The Text Path:** The LLM answers the original, ground-truth text prompt directly. 

> Because both paths share the same LLM and rule-based verifier, any difference in performance isolates the failure of the acoustic pipeline.

### 3. ASR and LLM Pipeline Assessment
The framework accommodates diverse pipeline architectures, evaluating both open-weight multilingual baselines (e.g., Qwen3-ASR, MERaLiON3-ASR) and commercial API services (e.g., ElevenLabs). It measures transcription quality (Word Error Rate and Character Error Rate) to separate *how much* the ASR changed the prompt from how much those changes actually derailed the downstream LLM task.

### 4. Deterministic Scoring and Active Subsets
All responses are scored with rule-based verifiers taken from SEA-HELM, keeping evaluations deterministic and identical across paths. Initial benchmarking focuses on highly verifiable subsets like **SEA-HELM IFEval** (instruction following) and **Global-MMLU-Lite** (multiple-choice reasoning).

## SEA-HELM Audio Leaderboard

The leaderboard allows users to compare different ASR-LLM configurations, highlighting the performance penalty of the speech modality. Initial empirical results have exposed severe degradation across the board. For example, while models achieve exceptionally high scores on text-only instruction following, end-to-end speech accuracy drops significantly. 

Notably, the benchmark reveals a profound "Tamil Bottleneck," where the modality penalty exceeds 40 percentage points regardless of whether open-weight or commercial ASR systems are used, pointing to a severe acoustic data scarcity in regional speech modeling.

## SEA-HELM Audio Datasets and Resources

SEA-HELM Audio forms part of the broader ATLAS-Eval ecosystem. Our methodology, evaluation frameworks, and related research papers (including the formal *SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance* preprint) are publicly accessible.

## Limitations and Future Work

While SEA-HELM Audio establishes a solid baseline using synthesized speech to measure the "floor" of performance degradation, [real-world spoken interactions](https://voice-agent.sea-lion.ai/playground/) involve natural accents, background noise, and conversational code-switching. Future iterations of SEA-HELM Audio aim to incorporate naturalistic, crowdsourced audio corpora to provide an even more robust and comprehensive evaluation of Southeast Asian voice AI.

## Resources

For more details and information on SEA-HELM Audio, you can refer to the following materials and platforms:

1. **SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance** [Technical Report](https://arxiv.org/abs/2610.19869)
2. **SEA-HELM Audio Benchmark Dataset** Available on Hugging Face: [`aisingapore/seahelm-audio`](https://huggingface.co/datasets/aisingapore/seahelm-audio)
3. **SEA-HELM Audio Evaluation Repository** Available on GitHub: [`aisingapore/seahelm-audio`](https://github.com/aisingapore/seahelm-audio)
4. **SEA Audio Leaderboard & Voice-Agent Playground** Interactive evaluation platform at [`voice-agent.sea-lion.ai`](https://voice-agent.sea-lion.ai/leaderboard/)