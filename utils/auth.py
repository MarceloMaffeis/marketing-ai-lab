import streamlit as st

def check_authentication():
    """
    Garante acesso 100% aberto e público a todas as ferramentas
    sem necessidade de login ou senha.
    """
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = True
    return True

