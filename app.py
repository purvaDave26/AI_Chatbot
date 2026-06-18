import streamlit as st
from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("SARVAM_API_KEY")

client=SarvamAI(api_subscription_key=api_key)


st.title("AI Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])


user_input=st.chat_input("type your message here....")

if user_input:
    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role":"user",
        "content":user_input})
    
    response=client.chat.completions(model="sarvam-30b",messages=st.session_state.messages)

    ai_reply=response.choices[0].message.content

    st.chat_message("assistant").write(ai_reply)

    st.session_state.messages.append({
        "role":"assistant",
        "content":ai_reply
    })


   