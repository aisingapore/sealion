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
<td><p>→ <a href="https://huggingface.co/aisingapore/Gemma2-9b-WangchanLIONv2-instruct">Gemma2 9B WangchanLIONv2 (Thai)</a>: The Gemma2 9B WangchanLIONv2 Instruct model is a collaborative effort between VISTEC and AI Singapore. It has been fine-tuned with approximately 3,760,000 Thai instruction-completion pairs derived from human-annotated instructions, FLAN-style automatic data construction, and synthetic samples. This multilingual model supports both Thai and English languages.</p><p></p><p>→ <a href="https://huggingface.co/GoToCompany/gemma2-9b-cpt-sahabatai-v1-instruct">Gemma2 9B CPT Sahabat-AI (Indonesian)</a>: The Gemma2 9B CPT Sahabat-AI v1 Instruct model, co-developed by GoTo Group and AI Singapore, has been fine-tuned with approximately 448,000 Indonesian instruction-completion pairs, along with 96,000 in Javanese, 98,000 in Sundanese, and an additional 129,000 in English. This multilingual model supports Indonesian, Javanese, Sundanese, and English.</p>
</td>
</tr>
</tbody></table>

## Impact and Future Directions

By leveraging SEA-LION’s architecture, these localized models provide AI solutions that align more closely with native language requirements. As SEA-LION continues to evolve, more localized versions are expected to emerge, further expanding the reach and effectiveness of AI in Southeast Asian languages.
