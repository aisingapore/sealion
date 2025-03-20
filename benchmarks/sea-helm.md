# SEA-HELM: SouthEast Asian Holistic Evaluation of Language Models

SEA-HELM (SouthEast Asian Holistic Evaluation of Language Models) is a comprehensive benchmark suite designed to evaluate the linguistic and cultural competencies of Large Language Models (LLMs) in Southeast Asian (SEA) languages.

Formerly known as BHASA, SEA-HELM has been expanded and integrated with HELM to provide a more rigorous and authentic evaluation. It addresses the critical need for multilingual and multicultural benchmarks in the rapidly evolving field of LLMs.

SEA-HELM serves as a valuable resource for developers looking to create and assess LLMs for linguistic accuracy and cultural sensitivity in the Southeast Asian context. It currently covers Filipino, Indonesian, Javanese, Sundanese, Tamil, Thai, and Vietnamese.

## Motivations

Several key factors motivated our development of SEA-HELM:

### Lack of Comprehensive SEA Language Benchmarks
Existing LLM benchmarks are capable of evaluating specific capabilities of LLMs in English and some mid- to low-resource languages, including those in the Southeast Asian (SEA) region. However, there has not been a comprehensive and authentic evaluation suite developed specifically for SEA languages, a problem exacerbated by the lack of both training and testing data on the internet. 

### Need for Multilingual and Multicultural Evaluations
There's an increasing need for benchmarks that assess not only linguistic capabilities but also cultural representation and sensitivity. Evaluations of linguistic and cultural representation are essential for gauging the efficacy and fairness of language models.

SEA-HELM deliberately incorporates community participation by involving native speakers to ensure linguistic accuracy and cultural authenticity. For example, the evaluation suite includes a cultural evaluation dataset for Filipino developed in collaboration with community members from the Philippines.
 

## Core Pillars of SEA-HELM

SEA-HELM is organized into five core evaluation pillars, designed to comprehensively assess various competencies of LLMs.

Each evaluation task under SEA-HELM uses prompts in the target language to ensure that the LLM can interpret native instructions correctly. The datasets used are either originally written in the native language or carefully translated by native speakers to avoid translation errors. This ensures that the evaluation is authentic and relevant to the linguistic nuances of each language.

### 1. NLP Classics

This pillar focuses on evaluating the fundamental natural language processing abilities of LLMs in Southeast Asian languages, such as language understanding, generation, and reasoning.

#### Natural Language Understanding (NLU)

NLU tasks assesses the model's ability to comprehend text. The tasks included in this competency are question answering and sentiment analysis.

- **Question Answering (QA)** evaluates the model's ability to understand a question and extract the answer from a given text. SEA-HELM uses datasets like TyDi QA for Indonesian, XQuAD for Vietnamese and Thai, and IndicQA for Tamil. The models are prompted to answer questions by extracting the answer from a provided paragraph.

- **Sentiment Analysis:** determines sentiment expressed in a text. SEA-HELM uses datasets like NusaX for Indonesian, UIT-VSFC for Vietnamese, Wisesight Sentiment for Thai, and IndicSentiment for Tamil. The models are prompted to determine the sentiment of a given sentence and respond with a single word: Positive, Negative, or Neutral.

#### Natural Language Generation (NLG)
NLG tasks evaluates a model's ability to generate human-like text. The tasks included in this competency are machine translation and abstractive summarization.

- **Machine Translation** assesses the model's ability to translate text from one language to another. SEA-HELM evaluates translation between English and target SEA languages. The models are prompted to translate a given text into a specified language.

- **Abstractive Summarization** requires the model to read a document, identify the key points, and summarize them into a coherent and fluent text. SEA-HELM uses the XLSum dataset for all four target languages. The models are prompted to summarize an article in one or two sentences in the specified language

#### Natural Language Reasoning (NLR)
NLR tasks assesses the model's ability to reason and draw inferences from text. The tasks included in this competency are causal reasoning and Natural Language Inference (NLI).

NLI tasks involve determining whether a given premise entails or contradicts a hypothesis. SEA-HELM uses datasets like IndoNLI for Indonesian, XNLI for Vietnamese and Thai, and IndicXNLI for Tamil.


### 2. LLM-Specifics
This pillar focuses on evaluating capabilities unique to LLMs, such as instruction following and chat capabilities.

- **Instruction following** assesses the ability of LLMs to follow human instructions and adhere to specified formats using **SEA-IFEval**, a benchmark we manually created collaboratively with native speakers.

- **Chat capability** evaluates the ability of LLMs to engage in human-like conversations using **SEA-MTBench**, another manually translated and localised version of the popular MT-Bench dataset.


### 3. SEA Linguistics
This pillar focuses on systematically diagnosing language proficiency and grammatical understanding of language models in Southeast Asian languages by utilizing LINDSEA (LINguistic Diagnostics for SouthEast Asian languages).

LINDSEA is a high-quality, manually-crafted linguistic dataset designed to provide a fine-grained evaluation of a model’s linguistic abilities, and is the first dataset of its kind created for SEA languages. 

### 4. SEA Culture
This pillar is designed to assess cultural representation and sensitivity in language models. This pillar recognizes the importance of evaluating LLMs on their understanding and appropriate handling of cultural nuances, social norms, and values specific to Southeast Asian cultures. 

SEA-HELM uses cultural diagnostics to probe for both cultural representation and sensitivity. The goal is to ensure that LLMs used in SEA contexts are not only linguistically accurate but also culturally aware and respectful.

SEA-HELM achieves authentic cultural representation through a strong participatory approach that includes native speaker communities. For example, SEA-HELM includes a cultural evaluation dataset for Filipino developed in collaboration with community members from the Philippines, which resulted in KALAHI. 

### 5. Safety

This pillar ensures that language models (LLMs) do not produce harmful or unsafe outputs, especially in the context of Southeast Asian (SEA) languages and cultures. It recognizes that multilingual inputs, particularly in lower-resource languages common in the SEA region, can increase the likelihood of LLMs generating unsafe responses. The pillar aims to protect users interacting with these models in SEA languages from issues like hate speech.

Currently, the Safety pillar focuses on toxicity detection as its primary task, with coverage for Indonesian, Thai, Vietnamese, and Filipino. This involves identifying toxic content such as hate speech and abusive language in text, which is crucial for content moderation. SEA-HELM uses datasets like MLHSD for Indonesian, Thai Toxicity Tweet for Thai, ViHSD for Vietnamese, and PH Elections Toxicity for Filipino.

While passing these evaluations is a necessary step, it is not a guarantee of complete safety in real-world scenarios, as it is impossible to cover every type of unsafe response. SEA-HELM plans to expand this pillar to include a broader range of safety-related tasks in the future.

## SEA-HELM Leaderboard

To provide transparency, comparative insights and understanding of models' multilingual and multicultural performance, SEA-HELM maintains a [public leaderboard](https://leaderboard.sea-lion.ai).

The [leaderboard](https://leaderboard.sea-lion.ai) offers multiple views, including overall scores, language-specific scores, and detailed task scores, allowing users to delve deeper into the evaluation results.


## SEA-HELM Datasets and Resources

Our SEA-HELM evaluation datasets are publicly available on [HuggingFace](https://huggingface.co/collections/aisingapore/sea-helm-evaluation-datasets-67593d0bb8c9f17f9f6b0fcb). 


## Limitations and Future Work

While SEA-HELM aims for holistic evaluations, it is not yet exhaustive in its coverage of languages and tasks. Areas for improvement include:

- Expanding SEA language coverage beyond the current seven languages (e.g., Burmese, Khmer, Lao).
- Exploring automatic LLM evaluations for better benchmarking.
- Enhancing the safety pillar to include more real-world risk factors.
- Adding more cultural and linguistic assessments

## Resources

For more details and information on SEA-HELM, you can refer to the following materials:
1. [BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models](https://arxiv.org/abs/2309.06085)
2. [SEA-HELM: Southeast Asian Holistic Evaluation of Language Models](https://arxiv.org/abs/2502.14301)
3. [Towards fair and comprehensive multilingual LLM benchmarking](https://cohere.com/blog/towards-fair-and-comprehensive-multilingual-and-multicultural-llm-benchmarking)


