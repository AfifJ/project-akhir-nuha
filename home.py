import streamlit as st

def app():
    st.title(f'Selamat datang di digital book store kami, {st.session_state.email}')