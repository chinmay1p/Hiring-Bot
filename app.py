import streamlit as st
from utils.prompts import prompt
from utils.llm_interface import llm_response
from utils.context_manager import update_context, get_context
from utils.data_storage import save_data
import re

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")
st.title("-- TalentScout Hiring Assistant --")

def init():
    if "context" not in st.session_state:
        st.session_state.context = []
    if "done" not in st.session_state:
        st.session_state.done = False
init()

st.write("Hello! I'm your Hiring Assistant. I'm here to help you get started with your job application.")

if not st.session_state.done:
    user_input = st.chat_input("You: ")
    if user_input:
        update_context("user", user_input)
        if any(word in user_input.lower() for word in ["exit", "quit", "bye"]):
            st.write("TalentScout: Thank you for your time! We'll get back to you soon.")
            save_data(get_context())
            st.session_state.done = True
        else:
            response=prompt(get_context())
            # response = llm_response(prompts)
            update_context("assistant",response)
            st.write(f"TalentScout:{response}")
else:
    st.write("Session ended. Refresh the page to start over.")
