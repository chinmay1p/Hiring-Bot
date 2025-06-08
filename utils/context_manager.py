import streamlit as st

def update_context(role, content):
    st.session_state.context.append({"role": role, "content": content})

def get_context():
    return st.session_state.context
