# SEA-LION Tokenizer

## Fast Tokenizer

This folder contains the fast tokenizer for the SEA-LION tokenizer. This fast tokenizer is converted using the [sentencepiece_extractor.py](https://github.com/huggingface/tokenizers/blob/main/bindings/python/scripts/sentencepiece_extractor.py) script from HuggingFace's `tokenizers` package.  

## Caveat

Please note that due to the conversion process, it is not possible to replicate the exact SentencePiece model accurately. More details in this [Github issue](https://github.com/huggingface/tokenizers/issues/225#issuecomment-612140650).

Please note that the original SentencePiece model does not normalize the input text whereas the converted fast tokenizer applies normalization.

## Usage

```python
from transformers import AutoTokenizer, PreTrainedTokenizerFast

tokenizer_folder = "sealion_fasttokenizer"
fast_tokenizer = AutoTokenizer.from_pretrained(tokenizer_folder)

# Check tokenizer type
isinstance(fast_tokenizer, PreTrainedTokenizerFast)
# True

# Encode
fast_tokenizer("Sea Lion is awsome")
# {'input_ids': [9975, 19723, 371, 6032], 'token_type_ids': [0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1]}

# Decode
fast_tokenizer([9975, 19723, 371, 6032])
# Sea Lion is awesome
```