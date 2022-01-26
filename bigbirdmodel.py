#pip3 install transformers and protobuf
from transformers import BigBirdForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
import torch

bot_name = "Sam"
model_id = "vasudevgupta/bigbird-roberta-natural-questions"
model = BigBirdForQuestionAnswering.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

with open("text.txt") as fileobject:
    context = fileobject.read().rstrip()
    context = context.replace("\n", " ")

def get_response(msg):
    tokenizer.encode(msg, truncation=True, padding=True)

    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

    # Passing the Question and Context into the QA pipeline
    output = nlp(question=msg, context=context)
    score = str(output)[9:16] # lay 5 so sau so 0

    strOutput = str(output).split("'")
    result = strOutput[len(strOutput) - 2]

    if (float(score) > 0.1):
        return result

    return "Access https://www.who.int/ for more information"

if __name__ == "__main__":
    while (1):
        question = input('Enter your question: ')
        tokenizer.encode(question, truncation=True, padding=True)

        nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

        # Passing the Question and Context into the QA pipeline
        output = nlp(question=question, context=context)

        score = str(output)[9:16]  # lay 5 so sau so 0
        if (float(score) > 0.1):
            print(output)
        else: print('Access https://www.who.int/ for more information')