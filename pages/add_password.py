import streamlit as st
from storage.password_store import PasswordStore
from utils.password_generator import check_password_strength

def show_add_password():
    st.header("Add New Password")
    
    store = PasswordStore(st.session_state.username)
    
    with st.form("add_password_form"):
        service = st.text_input("Service/Website")
        username = st.text_input("Username/Email")
        password = st.text_input("Password", type="password")
        notes = st.text_area("Notes (optional)")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            submitted = st.form_submit_button("Save Password")
        
        if submitted:
            if not service or not username or not password:
                st.error("Please fill in all required fields")
                return
            
            strength, feedback = check_password_strength(password)
            st.progress(strength / 5, text=f"Password Strength: {strength}/5")
            
            if feedback != "Strong password!":
                st.warning(feedback)
            
            store.add_entry(service, username, password, notes)
            st.success("Password saved successfully!")
            st.rerun()