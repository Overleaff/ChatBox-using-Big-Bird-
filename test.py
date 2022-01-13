from transformers import pipeline
'''
from transformers import  AutoModelForQuestionAnswering, AutoTokenizer
#model_id = "deepset/bert-base-cased-squad2"

model_id =model = AutoModelForQuestionAnswering.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
'''
''' '''
from transformers import BigBirdForQuestionAnswering,AutoTokenizer
model_id = "vasudevgupta/bigbird-roberta-natural-questions"
#model_id = "google/bigbird-pegasus-large-arxiv"
model = BigBirdForQuestionAnswering.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

'''
from transformers import PegasusTokenizer, BigBirdPegasusForQuestionAnswering
tokenizer = PegasusTokenizer.from_pretrained('google/bigbird-pegasus-large-arxiv')
model = BigBirdPegasusForQuestionAnswering.from_pretrained('google/bigbird-pegasus-large-arxiv')
'''


with open("text.txt") as fileobject:
    context = fileobject.read().rstrip()
    context = context.replace("\n", " ")

while(1):
    question = input('Enter your question: ')
    tokenizer.encode(question, truncation=True, padding=True)

    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

    # Passing the Question and Context into the QA pipeline
    output = nlp(question = question, context = context)

    score = str(output)[9:16]  # lay 5 so sau so 0
    if (float(score) > 0.05):
        print(output)