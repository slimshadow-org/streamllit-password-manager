import streamlit as st
from utils.crypto import verify_password, hash_password
import json
import os

def check_authentication():
    st.title("🔒 Password Manager Login")
    
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Master Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                with open("users.json", "r") as f:
                    users = json.load(f)
                
                if username in users and verify_password(password, users[username]):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    with tab2:
        with st.form("signup_form"):
            new_username = st.text_input("Username")
            new_password = st.text_input("Master Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Sign Up")
            
            if submitted:
                if new_password != confirm_password:
                    st.error("Passwords don't match")
                    return
                
                with open("users.json", "r") as f:
                    users = json.load(f)
                
                if new_username in users:
                    st.error("Username already exists")
                    return
                
                users[new_username] = hash_password(new_password)
                
                with open("users.json", "w") as f:
                    json.dump(users, f)
                
                st.success("Account created! Please login.")