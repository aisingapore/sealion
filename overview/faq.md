# FAQ

Common questions we receive at the SEA-LION inbox, grouped by topic. If your question is not covered here, write to us at [sealion@aisingapore.org](mailto:sealion@aisingapore.org) or use the Collaborate form on [sea-lion.ai](https://sea-lion.ai/).

## Getting started

### What is SEA-LION?

SEA-LION (Southeast Asian Languages In One Network) is a family of open-source large language models built for Southeast Asia's languages and cultural contexts. The models are developed by AI Singapore.

### How do I try SEA-LION?

You have a few options:

-   Test the models directly in our [Playground](https://sea-lion.ai/).
    
-   Chat with SEA-LION on our [Telegram bot](https://t.me/sealion_ai_bot).
    
-   Download the models from [Hugging Face](https://huggingface.co/aisingapore).
    
-   Inference the models through major cloud platforms (see "Running SEA-LION in production" below).
    

### Is SEA-LION free to use? Can I use it commercially?

Yes. SEA-LION is open-source and free to use, including for commercial purposes. You can download and self-host the models from Hugging Face, or access them through cloud platform partners.

## API access and rate limits

### How do I get an API key?

You can generate an API key through the SEA-LION Playground. Documentation is available at [docs.sea-lion.ai](https://docs.sea-lion.ai/).

### What are the API rate limits?

Our free APIs are intended for proof-of-concept (POC) development and are rate-limited (10 requests per minute). They are not designed for production workloads.

### Can I get a rate limit increase?

We are not able to raise the limits on the free POC tier. If you need higher throughput or production-grade reliability, inference SEA-LION through one of our cloud platform partners, where you can scale usage according to your needs.

### My API key expired, or I am hitting timeouts. What should I do?

The free API is rate-limited and meant for POC testing, so heavy or sustained use may hit limits. For continued or production use, move to a cloud platform partner. If you believe you are seeing an actual outage rather than a rate limit, write to us with the details.

### How do I run SEA-LION in production?

For production, inference SEA-LION through major cloud platforms rather than the free POC API. The models are available on hyperscalers including AWS (Bedrock) and Google Cloud (Vertex AI), among others. See our [inferencing guide](https://docs.sea-lion.ai/guides/inferencing) for the current list and setup steps.

### Which model and hardware should I use?

If you are running on limited GPU resources, use the quantised versions of the models. The model card on Hugging Face lists the available variants and their requirements.

## Languages and capabilities

### Which languages does SEA-LION support?

SEA-LION is trained on and supports the national languages of Southeast Asia. This includes (among others) Indonesian, Thai, Vietnamese, Malay, Tamil, Khmer, Burmese, Lao and Filipino. For the authoritative and most current list, see the model documentation.

### Does SEA-LION support \[Khmer / Tamil / Lao / Burmese\]?

Yes. These are among the Southeast Asian languages SEA-LION is trained on. We are continually working with local and international partners to strengthen performance across all supported languages.

### Does SEA-LION support Tetum?

We are actively improving Tetum capability, working together with local and international partners. It is an area of ongoing development.

### Does SEA-LION support dialects such as Cantonese or Hokkien?

No. We evaluate and support the national languages of Southeast Asia. This does not include dialects such as Cantonese, Hokkien, Teochew, Hakka or other Singaporean dialects.

### What about Singlish, or speech-to-text and text-to-speech?

SEA-LION currently supports text and image (vision) inputs, and does not yet have a voice or audio model, though we do have plans to release text-to-speech (TTS).

### Does SEA-LION have a voice or audio model?

Not yet. SEA-LION today supports text and vision, and does not currently have a voice or audio model. We do have plans to release text-to-speech (TTS). Follow our website and AI Singapore's social channels to hear when it is released.

### What is the difference between SEA-LION and MERaLiON?

SEA-LION and MERaLiON are complementary models that address different needs and work in tandem to strengthen Singapore's national AI foundation. SEA-LION, built by AI Singapore, is an open-source, SEA-relevant large language model. It is multilingual, multicultural and multimodal (handling text and vision), and is built for general tasks such as instruction following, tool use and reasoning. MERaLiON is a speech-to-text model that prioritises empathetic learning and understanding, starting with Singlish and Singapore's multicultural context and extending to regional languages. It also supports speech-related tasks such as emotion recognition and spoken dialogue summarisation. MERaLiON is developed by A\*STAR's Institute for Infocomm Research (I²R).

The two leverage shared data, compute and research to build complementary text and speech models.

## Benchmarks and evaluation

### Where can I see how SEA-LION performs?

Our benchmark evaluations are published on the [SEA-LION Leaderboard](https://leaderboard.sea-lion.ai/).

### I am running SEA-HELM and seeing inconsistencies. What should I check?

Make sure you are using the latest version of the SEA-HELM evaluation code base, which is updated as we add languages and metrics. We recommend running with the default SEA-HELM configuration.

## Partnerships and collaboration

### How can I partner or collaborate with SEA-LION?

We welcome collaboration across the public sector, private sector, academia and the non-profit space. The best first step is to submit the Collaborate form on [sea-lion.ai](https://sea-lion.ai/) or email us. To help us route your request quickly, please include a short overview of your organisation, your use case or proposed collaboration, and the languages or capabilities you are interested in.

### I would like to contribute language data or annotation. Is that useful?

We are always glad to hear from people who can help strengthen SEA-LION's coverage and quality. Share details of the data or capability you can offer, and we will let you know if it aligns with our current priorities. We do review fit case by case, so not every offer will match an active need at a given time.

### Can AI Singapore/SEA-LION fund my project or research?

AI Singapore/SEA-LION is a non-profit initiative funded by Singapore's National Research Foundation (NRF). We are not able to provide grants or funding for external projects. You are very welcome to use the open-source models freely for your work.

### We are a cloud or hosting provider interested in hosting SEA-LION. Who do we talk to?

Reach out via the Collaborate form or email. Note that SEA-LION is already available on several major platforms, so do let us know what you have in mind and we can explore fit.

## Programmes

### What is the Pinnacle AI Industry Programme (PAIP) and how do I apply?

PAIP is a company-sponsored programme that helps organisations build applied AI capability within their teams. Because it is tailored to each organisation, we usually start with a short call to understand your team, your goals and the number of participants before sharing detailed materials. If you are interested, email us with your organisation and a brief description of your needs.

## Media and speaking

### I am a journalist with a media or interview request.

Please email us with details of your outlet, the focus of the story and your timeline. Media requests are handled together with AI Singapore's Marketing Communications team, and we will follow up to confirm.

### I would like to invite SEA-LION to speak at an event.

We are glad to receive speaking and panel invitations. Email us with the event details, format, date and audience, and we will assess fit and timing.

## Security

### How do I report a security vulnerability?

If you have identified a potential security issue, please email us at [sealion@aisingapore.org](mailto:sealion@aisingapore.org) with the details so we can route it to the right team.

## Staying in touch

### How do I keep up with new releases and events?

Follow AI Singapore on LinkedIn and our other social channels, and keep an eye on the SEA-LION website. That is where we announce new model releases, events and opportunities.