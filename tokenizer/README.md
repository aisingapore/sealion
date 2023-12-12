# SEA-LION Tokenizer

## Fast Tokenizer

This folder contains the fast tokenizer for the SEA-LION tokenizer. This fast tokenizer is converted using the [sentencepiece_extractor.py](https://github.com/huggingface/tokenizers/blob/main/bindings/python/scripts/sentencepiece_extractor.py) script from HuggingFace's `tokenizers` package.  

## Caveat

Please note that due to the conversion process, it is not possible to replicate the exact SentencePiece model accurately. More details in this [Github issue](https://github.com/huggingface/tokenizers/issues/225#issuecomment-612140650).

Please note that the original SentencePiece model does not normalize the input text whereas the converted fast tokenizer applies normalization.  

## Normalization Differences Example

```python
text = '尽管该顾客又两次回到摊位，但最终不再来了。 中央社7月25日走访该店时，塑料袋已放回原处。'

# Converted Fast Tokenizer
['▁尽管', '该', '顾客', '又', '两次', '回到', '摊位', ',', '但最终', '不再', '来了', '。', '▁', '中央社', '7', '月', '2', '5', '日', '走访', '该店', '时', ',', '塑料袋', '已', '放', '回', '原', '处', '。']
[90424, 250428, 19132, 250571, 25218, 17435, 124279, 249832, 100096, 14049, 14608, 249868, 249813, 74216, 249884, 250069, 249846, 249872, 250030, 30115, 227861, 249971, 249832, 104737, 250225, 250356, 250370, 250307, 250327, 249868]

# From original SPM
['▁尽管', '该', '顾客', '又', '两次', '回到', '摊位', '，', '但最终', '不再', '来了', '。', '▁', '中央社', '7', '月', '2', '5', '日', '走访', '该店', '时', '，', '塑料袋', '已', '放', '回', '原', '处', '。']
[90424, 250428, 19132, 250571, 25218, 17435, 124279, 251933, 100096, 14049, 14608, 249868, 249813, 74216, 249884, 250069, 249846, 249872, 250030, 30115, 227861, 249971, 251933, 104737, 250225, 250356, 250370, 250307, 250327, 249868]

# Difference
['，', ',']
```

```python
text = '“Aku bilang pada paman… kamu (tidak di sini) untuk membelikanku bee hoon. Anda hanya ingin datang untuk mengambil kantong plastik gratis saya,” kata Ms Sally.'

# Converted Fast Tokenizer
['▁"', 'Aku', '▁bilang', '▁pada', '▁p', 'aman', '...', '▁kamu', '▁(', 'tidak', '▁di', '▁sini', ')', '▁untuk', '▁membel', 'ik', 'anku', '▁bee', '▁ho', 'on', '.', '▁Anda', '▁hanya', '▁ingin', '▁datang', '▁untuk', '▁mengambil', '▁kantong', '▁plastik', '▁gratis', '▁saya', ',"', '▁kata', '▁Ms', '▁Sally', '.']
[654, 205241, 29753, 4255, 321, 6278, 753, 8611, 432, 138410, 874, 26327, 249860, 1737, 87797, 490, 153399, 35541, 1060, 307, 249835, 2395, 7754, 10573, 28281, 1737, 27597, 144192, 83793, 15279, 8854, 1328, 20487, 11656, 32455, 249835]

# From original SPM
['▁"', 'Aku', '▁bilang', '▁pada', '▁p', 'aman', '…', '▁kamu', '▁(', 'tidak', '▁di', '▁sini', ')', '▁untuk', '▁membel', 'ik', 'anku', '▁bee', '▁ho', 'on', '.', '▁Anda', '▁hanya', '▁ingin', '▁datang', '▁untuk', '▁mengambil', '▁kantong', '▁plastik', '▁gratis', '▁saya', ',"', '▁kata', '▁Ms', '▁Sally', '.']
[654, 205241, 29753, 4255, 321, 6278, 250021, 8611, 432, 138410, 874, 26327, 249860, 1737, 87797, 490, 153399, 35541, 1060, 307, 249835, 2395, 7754, 10573, 28281, 1737, 27597, 144192, 83793, 15279, 8854, 1328, 20487, 11656, 32455, 249835]

# Difference
['...', '…']
```

# Segmentation Differences

```python
text = 'ກ່ຽວ​ກັບ​ບໍລິສັດ​ໜຶ່ງ​ທີ່​ຖືກ​ກວດ​ສອບ​ຫຼາຍ​ທີ່​ສຸດ​ໃນ​ໂລກ.'

# Converted Fast Tokenizer
['▁ກ', '່ຽວ', '\u200b', 'ກັບ', '\u200b', 'ບໍລິສັດ', '\u200b', 'ຫນ', 'ຶ່ງ', '\u200b', 'ທີ່', '\u200b', 'ຖືກ', '\u200b', 'ກວດ', '\u200b', 'ສ', 'ອບ', '\u200b', 'ຫຼາຍ', '\u200b', 'ທີ່', '\u200b', 'ສຸດ', '\u200b', 'ໃນ', '\u200b', 'ໂລກ', '.']
[43871, 83646, 250136, 54417, 250136, 179219, 250136, 169061, 94497, 250136, 24181, 250136, 108444, 250136, 210553, 250136, 251464, 62742, 250136, 94751, 250136, 24181, 250136, 112369, 250136, 28099, 250136, 163526, 249835]

# From original SPM
['▁ກ', '່ຽວ', '\u200b', 'ກັບ', '\u200b', 'ບໍລິສັດ', '\u200b', 'ໜຶ່ງ', '\u200b', 'ທີ່', '\u200b', 'ຖືກ', '\u200b', 'ກວດ', '\u200b', 'ສ', 'ອບ', '\u200b', 'ຫຼາຍ', '\u200b', 'ທີ່', '\u200b', 'ສຸດ', '\u200b', 'ໃນ', '\u200b', 'ໂລກ', '.']
[43871, 83646, 250136, 54417, 250136, 179219, 250136, 227757, 250136, 24181, 250136, 108444, 250136, 210553, 250136, 251464, 62742, 250136, 94751, 250136, 24181, 250136, 112369, 250136, 28099, 250136, 163526, 249835]

# Difference
['ຫນ', 'ໜຶ່ງ', 'ຶ່ງ']
```

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