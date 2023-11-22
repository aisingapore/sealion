# Please use transformers==4.34.1
from transformers import AutoModelForCausalLM, AutoTokenizer

generation_kwargs = {
    "do_sample": False,  # set to true if temperature is not 0
    "temperature": None,
    "max_new_tokens": 256,
    "top_k": 50,
    "top_p": 0.7,
    "repetition_penalty": 1.2,
}

tokenizer = AutoTokenizer.from_pretrained(
    "aisingapore/sealion7b-instruct-nc", trust_remote_code=True
)
generation_kwargs["eos_token_id"] = tokenizer.eos_token_id
model = AutoModelForCausalLM.from_pretrained(
    "aisingapore/sealion7b-instruct-nc", trust_remote_code=True
)

prompt_template = "### USER:\n{human_prompt}\n\n### RESPONSE:\n"
prompt = """Apa sentimen dari kalimat berikut ini?
Kalimat: Buku ini sangat membosankan.
Jawaban: """
full_prompt = prompt_template.format(human_prompt=prompt)

tokens = tokenizer(full_prompt, return_tensors="pt")

# Remove unneeded kwargs
if generation_kwargs["do_sample"] == False:
    generation_kwargs.pop("temperature")
    generation_kwargs.pop("top_k")
    generation_kwargs.pop("top_p")

output = model.generate(
    tokens["input_ids"],
    **generation_kwargs,
)
print(tokenizer.decode(output[0], skip_special_tokens=True))
