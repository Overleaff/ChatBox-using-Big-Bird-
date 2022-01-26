import streamlit as st 
import numpy as np 

from transformers import BigBirdForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
import torch
#streamlit run hello.py -- command to run

st.title('Covid 19 Big Bird Model')

st.write("""
# Have questions about COVID-19?
WE HAVE ANSWERS.
""")
st.sidebar.title("NLP Bot")
st.title("""
NLP Bot  
NLP Bot is an NLP conversational chatterbot. Initialize the bot by clicking the "Initialize bot" button. 
""")

#get text
def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text 


model_id = "vasudevgupta/bigbird-roberta-natural-questions"
model = BigBirdForQuestionAnswering.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
with open("text.txt") as fileobject:
    context = fileobject.read().rstrip()
    context = context.replace("\n", " ")

# respone
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

    return "i do not understand..."

# initialize
ind = 1
if st.sidebar.button('Initialize bot'):
 
    st.title("Your bot is ready to talk to you")
    ind = ind +1


user_input = get_text()
if user_input:
 st.text_area("Bot:", value=get_response(user_input), height=200, max_chars=None, key=None)


