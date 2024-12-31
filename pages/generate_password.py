import streamlit as st
import pyperclip
from utils.password_generator import generate_password, check_password_strength

def show_password_generator():
    st.header("Password Generator")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        length = st.slider("Password Length", 8, 32, 16)
    
    password = generate_password(length)
    strength, feedback = check_password_strength(password)
    
    st.code(password, language=None)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.progress(strength / 5, text=f"Password Strength: {strength}/5")
        if feedback != "Strong password!":
            st.info(feedback)
    
    with col2:
        if st.button("📋 Copy"):
            pyperclip.copy(password)
            st.toast("Password copied!")
        
        if st.button("🔄 Generate New"):
            st.rerun()