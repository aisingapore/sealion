# Prompting and Usage Guide

Quick references:

1. [Prompt Format](https://github.com/aisingapore/sealion/blob/main/docs/promptguide.md#prompt-format)
2. [Single Question Answering](https://github.com/aisingapore/sealion/blob/main/docs/promptguide.md#single-question-answering)
3. Multiple Question Answering
4. Contextual Question Answering
5. Translation
6. Creative Writing
7. Reasoning
8. Indonesian
9. Multilingual
10. Repetition Penalty

## Prompt Format

To ensure optimal performance from SEA-LION-7B-Instruct, prompts should be formatted in the following way. For instance, given the input "Describe Singapore in a few words", your prompt should look like this:

```
### USER:
Describe Singapore in a few words.

### RESPONSE:

```

__NOTE: the newline characters ie. “””### USER:\n{input}\n\n### RESPONSE:\n”””_

Additionally, SEA-LION-7B-Instruct has not been tuned to explicitly support system prompts, though we have noticed changes in behaviour when they are incorporated regardless.

## Guidelines

In our experiments with SEA-LION-7B-Instruct, beyond the above instruction format, we have found that crafting your instructions carefully can significantly enhance the model's performance and the quality of its response. Below are some strategies and guidelines to consider when formulating your instructions. Remember, these are illustrative and not exhaustive, and they are not meant to be rigid rules but rather suggestions to optimise your interaction with the model. 

### Single Question Answering

Asking precise questions can lead to more accurate answers. For example, including specific details like the year can greatly improve the quality of the response.

For instance, without specifying a time frame, you might receive a generic answer that doesn't directly address your query:

```
### USER:
Who is the president of the United States?

### RESPONSE:
The president of the United States is the leader of the United States and is elected by the Electoral College for a term of four years.
```

However, when you include a specific time frame, such as a year, the response is more direct and useful:

```
### USER:
Who is the president of the United States in 2022?

### RESPONSE:
Joe Biden
```

Specifying the desired format of your answer can significantly change the response you receive. For example, if you're seeking a specific type of answer, it's beneficial to mention this requirement in your question.

Consider the difference when a question is asked without specifying the answer format:

```
### USER:
Is Singapore a good place to live?

### RESPONSE:
Singapore is a great place to live. It is a safe and clean city with a high standard of living. The people are friendly and the food is delicious. There are many things to do in Singapore, from visiting the many museums and parks to shopping at the many malls and markets.
```

Compared to when a direct yes/no answer is requested:

```
### USER:
Is Singapore a good place to live? Answer with either yes or no only.

### RESPONSE:
Yes
```

### Multiple Question Answering

To effectively handle a prompt containing several questions as opposed to just one, we have found that organising them in a numerical list as follows generally works well:

```
### USER:
Answer the following questions.
1. How are rainbows formed?
2. What are some tourist attractions in Singapore?
3. What is the capital of Indonesia?
4. List 3 ASEAN countries.

### RESPONSE:
1. Rainbows are formed when sunlight reflects off droplets of water in the air.
2. Some tourist attractions in Singapore include the Singapore Zoo, Gardens by the Bay, and the Singapore Flyer.
3. Jakarta is the capital of Indonesia.
4. The 3 ASEAN countries are Indonesia, Singapore, and Thailand.
```

### Contextual Question Answering

For contextual question answering, we found that including a section instructing the model to answer based on the article and properly demarcating the start of the article or context was helpful in inducing a higher quality response from the model.

```
### USER:
Based on the following article, answer the questions below.
Article: On Wednesday, Singapore's government announced its intention to have driverless buses operating on public roads from 2022. Driverless buses are to be first launched in three towns on less crowded roads made to be suitable for the purpose. The autonomous buses are to run during off-peak times, complementing human-driven bus services.

Questions:
1. When is Singapore intending to operate driverless buses?
2. When will these buses run?
3. Will these buses replace human drivers?

### RESPONSE:
1. The government announced its intention to have driverless buses operating on public roads from 2022.
2. The autonomous buses are to run during off-peak times, complementing human-driven bus services.
3. The autonomous buses are not intended to replace human drivers.
```

### Translation

We find translation texts phrased in the following manner to be relatively successful:

```
### USER:
Translate the following text to Indonesian.
Indonesia lies along the equator, and its climate tends to be relatively even year-round.

### RESPONSE:
Indonesia terletak di garis khatulistiwa, dan iklimnya cenderung stabil sepanjang tahun.
```

### Creative Writing

In creative writing tasks, to enhance the diversity of the output and avoid repetitiveness, adjusting the repetition penalty could be helpful to alleviate some of the repetition. 

For instance, with a repetition penalty set at the default value of 1, the generated response tends to be more repetitive as shown below:

```
### USER:
Write a birthday song.

### RESPONSE:
Happy birthday to you
Happy birthday to you
Happy birthday to you
Happy birthday to you!
```

Adjusting the repetition penalty slightly to 1.05 yields a more interesting and higher quality response:

```
### USER:
Write a birthday song.

### RESPONSE:
Happy Birthday to you!
You're one year old today,
So let's celebrate!
You've been through so much,
And you've come so far.
You're a smart and strong girl,
With a bright future ahead.
You're a friend to everyone,
And you're always there for me.
I love you so much,
And I hope that you have the best day ever!
```

### Reasoning

In tasks requiring analytical insights, such as sentiment analysis, having the model provide a rationale for the answer might be desired. In these cases, we found that it is better to explicitly specify that the model should provide a reason.

For example, given this sentiment analysis task, without being instructed to include a reason, it replies as instructed to with either positive or negative.

```
### USER:
Is the sentiment of the following sentence positive or negative?
Sentence: I am having a great day because it is my birthday.

### RESPONSE:
Positive
```

However, when explicitly instructed to include a reason, the model not only identifies the sentiment but also delves deeper into the rationale behind its answer, offering a more detailed response.

```
### USER:
Is the sentiment of the following sentence positive or negative? Provide a reason for the sentiment.
Sentence: I am having a great day because it is my birthday.

### RESPONSE:
Positive
The sentiment of the sentence is positive because it is stated that it is the birthday of the person and it is a good day to celebrate.
```

### Indonesian

SEA-LION-7B-Instruct is also capable of handling prompts in native Indonesian. Similar to English, when crafting your prompt in Indonesian, keeping the above guidelines in mind is strongly advised. 

Here is an example of the model’s capabilities in answering multiple questions given a context in Indonesian.
```
### USER:
Berdasarkan artikel berikut, jawablah pertanyaan-pertanyaan di bawah ini.
Artikel: Kedua film tersebut sama-sama dibintangi Reza Rahadian, sehingga menjadikannya artis kedua yang membintangi dua film yang ditayangkan pada hari yang sama setelah Tatjana Saphira lewat Hit & Run dan Ghost Writer pada tahun yang sama.

Pertanyaan:
1. Siapakah nama artis yang membintangi dua film yang ditayangkan pada hari yang sama selain Reza Rahadian?
2. Film apa yang ditayangkan pada hari yang sama dengan Hit & Run?
3. Apa salah satu film yang dibintangi oleh Tatjana Saphira?

### RESPONSE:
1. Nama artis yang membintangi dua film yang ditayangkan pada hari yang sama selain Reza Rahadian adalah Tatjana Saphira.
2. Film yang ditayangkan pada hari yang sama dengan Hit & Run adalah Ghost Writer.
3. Film yang dibintangi oleh Tatjana Saphira adalah Ghost Writer.
```

_Translated Prompt: “Based on the following article, answer the questions below. Article: Both films star Reza Rahadian, making him the second artist to star in two films released on the same day after Tatjana Saphira through Hit & Run and Ghost Writer in the same year. Questions: 1. Who is the name of the artist who starred in two films that were shown on the same day besides Reza Rahadian? 2. What film was shown on the same day as Hit & Run? 3. What is one of the films starring Tatjana Saphira?”_

_Translated Response: “1. The name of the artist who starred in two films that were shown on the same day besides Reza Rahadian is Tatjana Saphira. 2. The film that was shown on the same day as Hit & Run is Ghost Writer. 3. The film starring Tatjana Saphira is Ghost Writer._

### Multilingual

We have found that the model is also capable of handling multilingual contexts despite not having been trained explicitly for them. For example, we can prompt the model in one language and ask for it to respond in a different language. To increase the chances of the model being able to perform the task, we recommend that the prompt be clear about the expected response language. Below are two examples that demonstrate this.

The first example involves prompting SEA-LION-7B-Instruct in English and asking it to do multiple question answering while providing the response in Thai. Here, the model is able to answer both questions correctly in the expected language.

```
### USER:
Answer the following questions strictly in Thai.
1. Who is the president of the United States now?
2. What is the capital of Japan?

### RESPONSE:
1. นายโจ ไบเดน เป็นประธานาธิบดีของสหรัฐอเมริกา
2. กรุงโตเกียว เป็นเมืองหลวงของญี่ปุ่น
```

_Translated Response: “1. Mr. Joe Biden is the president of the United States of America. 2. The city of Tokyo is the capital of Japan.”_

This second example stands out from the first because it includes several languages in the prompt. SEA-LION-7B-Instruct comprehends the Vietnamese instruction asking it to translate the given Indonesian sentence into English, and successfully executes the task, responding with an accurate translation.

```
### USER:
Hãy dịch văn bản dưới đây sang Tiếng Anh: "Nama saya Sarah dan saya sudah tinggal di Singapura selama 21 tahun."

### RESPONSE:
My name is Sarah and I have lived in Singapore for 21 years.
```
*Translated Prompt: "Translate the following text into English: 'My name is Sarah and I have lived in Singapore for 21 years.'”

### Repetition Penalty

In structuring prompts for the model, the inclusion of a repetition penalty parameter alongside the prompt can play a crucial role in avoiding repetitive responses. It is generally recommended to maintain the default setting, which imposes no penalty, unless repetitive answers are noted or a concise response is necessary. Through preliminary investigations, we also observed a decline in the model's effectiveness in certain tasks, such as contextual question answering, correlating with an increase in the repetition penalty.
