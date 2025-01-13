import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

## Replace with your actual OpenAI API key
openai_api_key = "api-key"



## Streamlit UI
st.set_page_config(page_title="Conversational Chatbot")
st.header("Hey, Let's Chat")

# Instantiate the ChatOpenAI with the API key
chat = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a Question and Answering  AI assistant")
    ]

## Function to load OpenAI model and get response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    response = get_chatmodel_response(input)
    st.subheader("The Response is")
    st.write(response)
