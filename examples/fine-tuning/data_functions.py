import logging

from datasets import concatenate_datasets, load_dataset

logger = logging.getLogger(__name__)

PROMPT_TEMPLATE = {
    "sealion": """### USER:
{prompt}

### RESPONSE:
{response}<|endoftext|>""",
    "sealion_w_system": """### SYSTEM:
{system}
    
### USER:
{prompt}

### RESPONSE:
{response}<|endoftext|>""",
}


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


def _prompt_format_helper(
    instruction_col_name, response_col_name, template, system=None
):
    def _formatter(example):
        if system is not None:
            text = template.format(
                prompt=example[instruction_col_name],
                response=example[response_col_name],
                system=system,
            )
        else:
            text = template.format(
                prompt=example[instruction_col_name],
                response=example[response_col_name],
            )
        example["text"] = text

        return example

    return _formatter


def _counter(tokenizer, col):
    def _helper(example):
        try:
            example["count"] = len(tokenizer.encode(example[col]))
        except:
            print(example["Response"], example["Prompt"])
        return example

    return _helper


def _count_tokens(dataset, tokenizer, cols, num_proc=8):
    columns = dataset.column_names
    count_dict = {"length": len(dataset)}

    for col in cols:
        count_dataset = dataset.map(
            _counter(tokenizer, col),
            remove_columns=columns,
            num_proc=num_proc,
        )
        count_dict[f"{col}_token_count"] = sum(count_dataset["count"])
    return count_dict


def load_hf_dataset(conf, dataset, split_train_test=True, tokenizer=None):
    dataset = load_dataset(
        conf.datasets[dataset]["name"],
        split=conf.split,
        token=True,
        num_proc=conf.num_proc if not conf.streaming else None,
        streaming=conf.streaming,
    )

    # count number of tokens in training data
    if tokenizer is not None:
        count = _count_tokens(
            dataset, tokenizer, ["prompt", "response"], num_proc=conf.num_proc
        )
    else:
        count = {}

    format_prompt = _prompt_format_helper(
        instruction_col_name="prompt",
        response_col_name="response",
        template=PROMPT_TEMPLATE[conf.prompt_format],
        system=conf.system_prompt,
    )
    dataset = dataset.map(format_prompt, num_proc=conf.num_proc)
    dataset = dataset.filter(
        lambda example: len(tokenizer.encode(example["text"])) <= conf.seq_length,
        num_proc=conf.num_proc,
    )
    if split_train_test:
        train_dataset, val_dataset = split_dataset(conf, dataset)
        return train_dataset, val_dataset, count
    else:
        return dataset, count


dataset_dictionary = {
    "hf": load_hf_dataset,
}


def create_datasets(tokenizer, conf):
    train_data_list = []
    valid_data_list = []
    count_dict = {}

    for dataset in conf.datasets:
        load_function = dataset_dictionary[conf.datasets[dataset]["type"]]
        train_data, valid_data, count = load_function(
            conf, dataset, tokenizer=tokenizer
        )
        count_dict[dataset] = count

        for _ in range(conf.datasets[dataset]["duplicate"]):
            train_data_list.append(train_data)
            valid_data_list.append(valid_data)

    train_data = concatenate_datasets(train_data_list)
    valid_data = concatenate_datasets(valid_data_list)

    if conf.streaming:
        logger.info("Loading the dataset in streaming mode")
        train_data = train_data.shuffle(buffer_size=conf.shuffle_buffer, seed=conf.seed)
    else:
        train_data = train_data.shuffle(seed=conf.seed)
        logger.info(
            f"Size of the train set: {len(train_data)}. Size of the validation set: {len(valid_data)}"
        )

    return train_data, valid_data, count_dict
