from openai import OpenAI

client = OpenAI(
    api_key="sk-i1hM1VTIdZmo8EPm3rofZQ",
    base_url="https://api.sea-lion.ai/v1" 
)

completion = client.chat.completions.create(
    model="aisingapore/Llama-SEA-LION-v3-70B-IT",
    messages=[
        {
            "role": "user",
            "content": "what is the capital of malaysia?"
        }
    ],
    extra_body={
        "cache": {
            "no-cache": True
        }
    },
    
)

print(completion.choices[0].message.content)

