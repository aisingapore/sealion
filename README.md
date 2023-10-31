# SEA-LION (Southeast Asian Languages in One Network) - A Family of Southeast Asian Language Models

SEA-LION is a family of open source language models developed by AI Singapore to better understand and represent the diverse contexts, languages, and cultures of Southeast Asia. 

## Key Features

- 3 to 7 billion parameters (larger models coming in 2024)
- Trained on 980B tokens of text data from 11 languages spoken across Southeast Asia (SEA)
- Specialized vocabulary and tokenization for optimal performance on SEA languages
- Excels on regional tasks and datasets
- Open source under the MIT License for community contribution and adoption

## Getting Started

The SEA-LION model files are available in the `models` directory. See the examples in the `examples` folder for how to load and use the model for inference.

To use SEA-LION:

```python
import sea_lion

model = sea_lion.load_model("sea_lion_3B")

output = model.generate(prompt="Singapore is a", max_length=30)
```

## Model Details

SEA-LION is based on the MPT architecture with 32 layers and comes in two sizes:

- [sea-lion-3B](https://huggingface.co/aisingapore/sealion3b) : 3 billion parameters 
- [sea-lion-7B](https://huggingface.co/aisingapore/sealion7b) : 7 billion parameters

It was trained on a diverse dataset of 980B tokens spanning 11 SEA languages:

- English
- Chinese  
- Indonesian
- Malay
- Thai
- Vietnamese
- Filipino
- Tamil
- Burmese
- Khmer
- Lao

The model uses a vocabulary of 256,000 tokens and a context length of 2048 tokens. It employs a custom SEA byte-pair encoding (BPE) tokenizer to handle the unique linguistic properties of SEA languages.

## Performance

SEA-LION does as well or outperforms on regional tasks and datasets:

[ _Metrics coming soon_ ]

SEA-LION does average when it comes to general LLM tasks (as measured by Hugging Face''s LLM Leaderboard)

[ _Metrics coming soon_ ]

For full details on the datasets, metrics, and results, please see the model cards:
* [sea-lion-3B](https://huggingface.co/aisingapore/sealion3b)
* [sea-lion-7B](https://huggingface.co/aisingapore/sealion7b)

## Contributing

We welcome contributions to SEA-LION! Check out the [contributing guide](CONTRIBUTING.md) to get started.

Some ways to contribute:

- Report bugs and issues
- Enhance the documentation
- Add more model evaluation tasks and metrics
- Train versions of the model in more SEA languages

## License

SEA-LION is licensed under the [MIT License](LICENSE).

## Citation

If you use SEA-LION in your work, please cite it as:

```
@misc{sea_lion_2022,
  title={SEA-LION: Large Language Model for Southeast Asia},
  author={AI Singapore},
  year={2023},
  howpublished={\url{https://github.com/aisg/sea-lion}}
}
```

## Contact

For questions, comments, or issues, please open a GitHub issue or contact us at seallm@aisingapore.org.
