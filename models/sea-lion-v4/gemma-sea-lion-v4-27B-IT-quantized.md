---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
Gemma-SEA-LION-v4-27B-IT (IT Model) Last updated: 2025-08-23
---

# Model Card for Gemma-SEA-LION-v4-27B-IT-GGUF, -NVFP4 and -FP8-Dynamic

<!-- Provide a quick summary of what the model is/does. -->

Last updated: 2025-08-23

**SEA-LION** is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned 
for the Southeast Asia (SEA) region.

As of 25 Aug 2025, Gemma-SEA-LION-v4-27B-IT excels at Southeast Asian (SEA) tasks when compared to other open models
 with fewer than 200 billion parameters and demonstrates performance comparable to that of larger and top closed models. 
 Gemma-SEA-LION-v4-27B-IT was quantized to create Gemma-SEA-LION-v4-27B-IT-GGUF, -NVFP4 and -FP8-Dynamic. 
 The quantized models has little degradation (<x%) in performance compared to Gemma-SEA-LION-v4-27B-IT 
 (for detailed rankings, please refer to the [leaderboard](https://leaderboard.sea-lion.ai/)), and 
 this version can run on a laptop with Ollama with 16GB of memory. 

Gemma-SEA-LION-v4-27B-IT-GGUF, -NVFP4 and -FP8-Dynamic inherit Gemma 3’s: 

- Large 128K context length 

- Image and text understanding capabilities, including document comprehension, visual Q&A, and image-grounded reasoning

- Advanced function calling and structured outputs to allow for seamless integration into larger systems



### Model Description

<!-- Provide a longer summary of what this model is. -->

SEA-LION stands for *Southeast Asian Languages In One Network*. 

Quantization was performed on Gemma-SEA-LION-v4-27B-IT to produce optimized variants that reduce memory requirements 
while maintaining model quality. These quantized models support inference on a range of consumer-grade GPUs 
and are compatible with various inference engines.


For tokenization, the model employs the default tokenizer used in Gemma 3 27B Instruct. 


- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s):**  Bahasa Indonesia, Burmese, Chinese, English, Khmer, Lao, Malay, Tagalog, Tamil, Thai and Vietnamese
- **License:** [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- **Quantized from model:** Gemma-SEA-LION-v4-27B-IT

This repo contains GGUF format models files for aisingapore/Gemma-SEA-LION-v4-27B-IT

Model Weights included in this repository:
- [Gemma-SEA-LION-v4-27B-IT-Q4_K_M](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT-GGUF) 
- [Gemma-SEA-LION-v4-27B-IT-Q8_0](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT-GGUF) 
- [Gemma-SEA-LION-v4-27B-IT-NVFP4](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT-NVFP4) 
- [Gemma-SEA-LION-v4-27B-IT-FP8-Dynamic](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT-FP8-Dynamic)

> Take note that some GGUFs are split into parts. Most tools such as llama.cpp and those built on it do support split GGUFs, 
> pointing the platform to the first split will be sufficient for it to function. In the event where a merge is necessary, 
> it can be done using llama.cpp's gguf-split: ./gguf-split --merge ./path/to/first-split ./path/to/output-gguf More details: 
> gguf-split guide & [README](https://github.com/ggerganov/llama.cpp/tree/master/examples/gguf-split)


## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Performance Test Results

| Quantized Variant | Model Size (GB) | Memory Footprint (GB) | VRAM Required (GB) | Time to First Token (s) | Tokens per Second |
|-------------------|-----------------|-----------------------|--------------------|------------------------|-------------------|
| Q8_0              | 28.7            | 3                     | 47                 | 3.179                  | 37                |
| Q4_K_M            | 16.5            | 2.7                   | 35.5               | 2.645                  | 59.9              |
| NVFP4             | 20.9            |                       |                    | 0.034                  | 81.9              |
| FP8 Dynamic       | 29.3            |                       |                    | 0.489                  | 66.1              |

Additional Remarks: 

- Concurrency Requests: 1

- GGUF served using llama.cpp with the following settings:

- Offload all layers to GPU, Context Length 128K

- Reported results are the median (p50) values, calculated across 10 requests.




### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model has not been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

*The model was not tested for robustness against adversarial prompting.* It is important for users to be aware that our model exhibits certain limitations that warrant consideration. 
Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, 
introducing fictional elements that are not grounded in the provided context. 
Users should also exercise caution in interpreting and validating the model's responses 
due to the potential inconsistencies.

**Limitations**

In terms of vision capability, Gemma-SEA-LION-v4-27B-IT has been trained and fine-tuned exclusively on the text back-end.
As a result, its vision capabilities are expected to be comparable to those of Gemma 3 IT 27B, 
and may not exhibit significant improvements or differences in this area. [🤗 google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it )



## More Information

This is the repository for the commercial instruction-tuned model. 
The model has not been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable 
for any claims, damages, or other liabilities arising from the use of the released weights and codes.

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. 
Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore.

For more info, please contact us at sealion@aisingapore.org


## Team

Antonyrex Sajeban, Chan Hok Teng Adwin, Cheng Zi Yi Nicholas, Choa Hsueh Mei Esther, Heng Jonathan, Huang Yuli, Hulagadri Adithya Venkatadri, 
Jann Railey Estrada Montalan, Kang Siow Wei  Bryan, Lau Wayne, Lee Chwan Ren, Leong Wai Yi, Leong Wei Qi, 
Limkonchotiwat Peerat, Muhammad Ridzuan Bin Mokhtar, Nagarajan Karthik, Ng Boon Cheong  Raymond, Ngee Chia Tai, 
Ngui Jian Gang, Nguyen Thanh Ngan, Ong Jin Jie Brandon, Ong Tat-Wee David, Ong Zhi Hao, Pereira Mark, 
Rengarajan Hamsawardhini, Susanto Yosephine, Sutaveephamochanon Anocha, Tan Choon Meng, Tan Chor Phin Evelyn, 
Tan Siao Wei Jessica, Teng Kok Wai Walter, Teo Eng Sipp Leslie, Tjhi William, Yeo Yeow Tong, Yong Xianbin, 
Liew Rachel, Liu Bing Jie Darius, Teo Wei Yi, Lin Zhou (NCS), Roshan Gopalakrishnan (NCS), Cuahtemoc Anda (NCS), 
Sri Devi Wijaya (NCS), Partha Nandi (NCS)


## Contact

sealion@aisingapore.org