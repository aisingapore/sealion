**South East Asian Languages in One Network**

_Built for Southeast Asia, by Southeast Asia_

South East Asian Languages in One Network (SEA-LION) is a family of open-source Large Language Models (LLMs) that better understands Southeast Asia’s (SEA) diverse contexts, languages, and cultures.

It is an open-source project anchored by the Products Pillar of AI Singapore. Our work in SEA-LION aims to create LLMs that cater to under-represented population groups and low resource languages in the SEA region. You can [read more about our motivations for SEA-LION here](/overview/why_sea-lion.md).

This site provides information and resources on SEA-LION, including how to access the models, hosting, and how-to guides.

## Key Features of SEA-LION

| Model Collection | Size | Context Length | Training Strategy          | Available in            |
|------------------|------|----------------|----------------------------|-------------------------|
| **[SEA-LION v3.5](/models/sea-lion-v3.5/sea-lion-v3.5.md)** | 8B   | 128K           | CPT¹ of Llama 3.1 8B | Reasoning, GGUF    |
|                  | 70B  | 128K           | CPT of Llama 3.1 70B | Reasoning, GGUF    |
| **[SEA-LION v3](/models/sea-lion-v3/sea-lion-v3.md)**  | 9B   | 8192           | CPT of Gemma2            | Base, Instruct, GGUF    |
|                  | 8B   | 128K           | CPT of Llama 3.1 8B       | Base, Instruct, GGUF    |
|                  | 70B  | 128K           | CPT of Llama 3.1 70B      | Base, Instruct, GGUF    |
| **[SEA-LION v2](/models/sea-lion-v2/sea-lion-v2.md)**  | 8B   | 8192           | CPT of Llama3             | Base, Instruct, GGUF    |
| **[SEA-LION v1](/models/sea-lion-v1/sea-lion-v1.md)**  | 3B   | 2048           | Pre-training from scratch  | Base                    |
|                  | 7B   | 2048           | Pre-training from scratch  | Instruct                |

¹ Continued Pre-Training


## Performance and Benchmarks

SEA-LION has seen:

* In v1, ability to outperform most models based on SEA-HELM (SouthEast Asian Holistic Evaluation of Language Models) when it was released
* In v2, outperformance for SEA tasks, while retaining credible performance on standard (English) benchmarks
* In v2.1, key improvements in conversational abilities across SEA languages, while providing more helpful and contextually appropriate responses to user prompts
* In v3, outperforms similar sized open source models, and even some larger models in both general and SEA capabilities

We use a holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering) but also [meticulously handcrafted linguistic and cultural diagnostic tests tailored to Southeast Asia](https://arxiv.org/abs/2309.06085v2).

Visit our [Leaderboard](https://leaderboard.sea-lion.ai/) for more detailed breakdown on:

1. How SEA-LION compares to other available models along different metrics
2. What SEA-HELM is and the four key capabilities it is evaluated on: English performance, Proficiency in SEA chat, Instruction-following and Linguistic tasks
3. What each of these globally recognized metrics mean under SEA-HELM

## Licensing

**Transparent and Open Source**

We have benefited greatly from the open-source community and believe that efforts to better represent our region will similarly be well served by open-source efforts.

All SEA-LION releases will therefore embrace an open-source ethos under the MIT license as much as possible; however, the exact licensing terms may vary depending on the underlying base model’s restrictions or requirements. For instance, if the model leverages Meta’s Llama3 codebase, it may be bound by the [Llama3 License](https://huggingface.co/meta-llama/Meta-Llama-3-8B/blob/main/LICENSE), which places certain restrictions on commercial use. Similarly, the Gemma-based variants may carry different terms. Users should always refer to the Hugging Face model card of each specific SEA-LION model for the most accurate, up-to-date license information.

SEA-LION will also be open and transparent in the following areas throughout this guide:

1. Pre-Training data
2. Model training code
3. Fine-Tuning data
4. Evaluation benchmarks

## Community

We welcome contributions to SEA-LION! Check out the [contributing guide](overview/contributing.md) to get started.

Some ways to contribute:

* Report bugs and issues
* Enhance the documentation
* Add more model evaluation tasks and metrics
* Train versions of the model in more SEA languages

Check out our [collaborations guide](overview/collaboration.md) also, for possible ways to further enhance and expand the capabilities of SEA-LION together.

## To Cite SEA-LION

If you use SEA-LION in your work, please cite it as:

```bibtex
@misc{sea_lion_2024,
  title={SEA-LION (Southeast Asian Languages In One Network): A Family of Large Language Models for Southeast Asia},
  author={AI Singapore},
  year={2024},
  howpublished={\url{https://github.com/aisingapore/sealion}}
}
```

If you are using SEA-LION v3 for your work, please cite it as:

```bibtex
@misc{2504.05747,
      title={SEA-LION: Southeast Asian Languages in One Network},
      author={Raymond Ng and Thanh Ngan Nguyen and Yuli Huang and Ngee Chia Tai and Wai Yi Leong and Wei Qi Leong and Xianbin Yong and Jian Gang Ngui and Yosephine Susanto and Nicholas Cheng and Hamsawardhini Rengarajan and Peerat Limkonchotiwat and Adithya Venkatadri Hulagadri and Kok Wai Teng and Yeo Yeow Tong and Bryan Siow and Wei Yi Teo and Wayne Lau and Choon Meng Tan and Brandon Ong and Zhi Hao Ong and Jann Railey Montalan and Adwin Chan and Sajeban Antonyrex and Ren Lee and Esther Choa and David Ong Tat-Wee and Bing Jie Darius Liu and William Chandra Tjhi and Erik Cambria and Leslie Teo},
      year={2025},
      eprint={2504.05747},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.05747},
}
```

## Acknowledgements

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. Any opinion, finding, conclusion or recommendation expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore, or the National University of Singapore.

We also grateful for the support of the Infocomm Media Development Authority (IMDA) of Singapore.

SEA-LION would not be possible without a growing list of Singapore, regional, and international collaborators. Please see our website for more details.

## Contact

If you have questions, comments, or issues, please open a GitHub issue or contact us via this [SEA-LION Inquiry Form](https://forms.gle/sLCUVb95wmGf43hi6).
