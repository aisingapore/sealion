from datasets import load_dataset
from helper_functions import *

from trl.trainer import ConstantLengthDataset
from omegaconf import OmegaConf


def split_dataset(args, dataset):
    if args.streaming:
        print("Loading the dataset in streaming mode")
        valid_data = dataset.take(args.size_valid_set)
        train_data = dataset.skip(args.size_valid_set)
    else:
        dataset = dataset.train_test_split(test_size=0.005, seed=None)
        train_data = dataset["train"]
        valid_data = dataset["test"]
    return train_data, valid_data


prompt_format_without_system = """### USER:
{instruction}

### RESPONSE:
{response}"""


def load_dolly(args, split_train_test=True):
    dataset = load_dataset(
            "Abzu/dolly_hhrlhf",
            split=args.split,
            use_auth_token=True,
            num_proc=8 if not args.streaming else None,
            streaming = args.streaming
            )
    dataset=dataset.map(prepare_dolly_text)

    if split_train_test:
        return split_dataset(args, dataset)
    else:
        return dataset


def prepare_dolly_text(example):
    text = prompt_format_without_system.format(
        instruction=example["prompt"], response=example["response"]
    )
    example["text"] = text
    return example


def create_datasets(tokenizer, conf):
    train_data_list = []
    valid_data_list = []

    train_data, valid_data = load_dolly(conf)

    if conf.streaming:
        print("Loading the dataset in streaming mode")
        train_data = train_data.shuffle(buffer_size=conf.shuffle_buffer, seed=None)
    else:
        train_data = train_data.shuffle(seed=None)
        print(
            f"Size of the train set: {len(train_data)}. Size of the validation set: {len(valid_data)}"
        )

    chars_per_token = chars_token_ratio(train_data, tokenizer)
    print(f"The character to token ratio of the dataset is: {chars_per_token:.2f}")

    train_dataset = ConstantLengthDataset(
        tokenizer,
        train_data,
        dataset_text_field="text",
        infinite=True,
        seq_length=conf.seq_length,
        chars_per_token=chars_per_token,
    )
    valid_dataset = ConstantLengthDataset(
        tokenizer,
        valid_data,
        dataset_text_field="text",
        infinite=False,
        seq_length=conf.seq_length,
        chars_per_token=chars_per_token,
    )
    return train_dataset, valid_dataset
