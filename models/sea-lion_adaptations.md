# SEA-LION Foundation Family

The SEA-LION models have served as a foundation for developing localized AI solutions tailored to specific linguistic and cultural needs. Over multiple iterations, other regions have built upon SEA-LION’s architecture to create specialized versions that enhance language understanding for their respective regions. These models leverage SEA-LION’s robust multilingual capabilities while being fine-tuned with localized datasets, ensuring better performance in regional contexts.

## SEA-LION Model Tree
<table>
<thead><tr><th width="144" valign="top">Base</th><th>Localized Model</th></tr></thead>
<tbody>
<tr>
<td width="144" valign="top">SEA-LION v1</td>
<td>→ <a href="https://huggingface.co/airesearch/WangchanLion7B">WangchanLion 7B (Thai)</a>: WangchanLion 7B is a multilingual instruction-following model developed by PyThaiNLP and the VISTEC-depa AI Research Institute of Thailand. Fine-tuned on SEA-LION-v1-7B, it incorporates approximately 500,000 samples from open-source, commercially permissible datasets, with a focus on Thai and English languages.</td>
</tr>
<tr>
<td valign="top">SEA-LION v2</td>
<td>→ <a href="https://huggingface.co/GoToCompany/llama3-8b-cpt-sahabatai-v1-instruct">Llama3 8B CPT Sahabat-AI v1 Instruct (Indonesian)</a>:</b> Llama3 8B CPT Sahabat-AI v1 Instruct model, co-developed by GoTo Group and AI Singapore, is an Indonesian-focused adaptation fine-tuned with 448,000 Indonesian instruction-completion pairs, along with 96,000 Javanese and 98,000 Sundanese pairs. It supports Indonesian, Javanese, Sundanese, and English, making it a significant advancement in AI for the Indonesian linguistic landscape.</td>
</tr>
<tr>
<td valign="top">SEA-LION v3</td>
<td><p>→ <a href="https://huggingface.co/aisingapore/Gemma2-9b-WangchanLIONv2-instruct">Gemma2 9B WangchanLIONv2 (Thai)</a>: The Gemma2 9B WangchanLIONv2 Instruct model is a collaborative effort between VISTEC and AI Singapore. It has been fine-tuned with approximately 3,760,000 Thai instruction-completion pairs derived from human-annotated instructions, FLAN-style automatic data construction, and synthetic samples. This multilingual model supports both Thai and English languages.</p>
<p></p><p>→ <a href="https://huggingface.co/GoToCompany/gemma2-9b-cpt-sahabatai-v1-instruct">Gemma2 9B CPT Sahabat-AI (Indonesian)</a>: The Gemma2 9B CPT Sahabat-AI v1 Instruct model, co-developed by GoTo Group and AI Singapore, has been fine-tuned with approximately 448,000 Indonesian instruction-completion pairs, along with 96,000 in Javanese, 98,000 in Sundanese, and an additional 129,000 in English. This multilingual model supports Indonesian, Javanese, Sundanese, and English.</p>
</td>
</tr>
<tr>
<td valign="top">SEA-LION v4</td>
<td><p>→ <a href="https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-VL">Gemma 3 27B/4B SEA-LION v4 (Multimodal)</a>: The first multimodal release in the SEA-LION family, based on the Gemma 3 architecture. Co-developed with Google, these models support a 128K context window. It underwent post-training on ~10M samples across 11 SEA languages and features vision-text capabilities for document understanding and visual Q&A. This model supports text and image understanding with a commercially permissive license. It is designed to handle Southeast Asian cultural nuances and visual contexts.</p>
<p></p><p>→ <a href="https://huggingface.co/aisingapore/Qwen-SEA-LION-v4-4B-VL"> Qwen-SEA-LION-v4-4B/8B-IT</a>: The lightweight flagship multimodal model built on the Qwen3-VL framework, optimized for regional linguistic and cultural nuances.</p>
<p></p><p>→ <a href="">Apertus 8B SEA-LION v4</a>: A fully open regional adaptation based on the Swiss AI "Apertus" architecture, focusing on highly efficient, transparent, and community-driven multilingual support. Features 15T token pre-training across 1,000+ languages with a focus on deep multilingual depth and transparency.
</p>
</td>
</tr>
<tr>
  <td valign="top">SEA-Guard</td>
  <td>A specialized collection of safety-focused LLMs built on the SEA-LION family released on 4 Feb 2026. 
    <p>→ <a href="https://huggingface.co/aisingapore/Qwen-SEA-Guard-4B-040226">Qwen-SEA-Guard-4B/8B (Image-to-Text)</a>: The 4B variant is a lightweight visual guardrail optimized for edge applications, while the 8B offers balanced visual moderation with stronger reasoning capabilities.</p>
    <p></p>
    <p>→ <a href="https://huggingface.co/aisingapore/Llama-SEA-Guard-8B-040226">Llama-SEA-Guard-8B (Text Generation)</a>: A text-only safety specialist optimized for chat moderation and policy enforcement, ensuring safe interactions in dialogue systems.</p>
    <p></p>
    <p>→ <a href="https://huggingface.co/aisingapore/Gemma-SEA-Guard-12B-040226">Gemma-SEA-Guard-12B (Multimodal)</a>: The high-capacity safety flagship capable of interpreting complex relationships between visual and textual data for deep content analysis.</p>
  </td>
</tr>
</tbody></table>

## Impact and Future Directions

By leveraging SEA-LION’s architecture, these localized models provide AI solutions that align more closely with native language requirements. As SEA-LION continues to evolve, more localized versions are expected to emerge, further expanding the reach and effectiveness of AI in Southeast Asian languages.
