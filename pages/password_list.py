import streamlit as st
import pyperclip
from storage.password_store import PasswordStore

def show_password_list():
    st.header("Stored Passwords")
    
    store = PasswordStore(st.session_state.username)
    search = st.text_input("🔍 Search passwords", key="search")
    
    entries = store.search_entries(search) if search else store.entries
    
    for entry in entries:
        with st.expander(f"{entry.service} - {entry.username}"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.text_input("Password", 
                             value=entry.password, 
                             type="password",
                             disabled=True,
                             key=f"pass_{entry.id}")
                
                if entry.notes:
                    st.text_area("Notes", 
                                value=entry.notes,
                                disabled=True,
                                key=f"notes_{entry.id}")
            
            with col2:
                if st.button("📋", key=f"copy_{entry.id}"):
                    pyperclip.copy(entry.password)
                    st.toast("Password copied!")
                    
                if st.button("🗑️", key=f"delete_{entry.id}"):
                    if store.delete_entry(entry.id):
                        st.rerun()
                        
            # Edit form
            with st.form(key=f"edit_form_{entry.id}"):
                new_username = st.text_input("New Username", 
                                           value=entry.username,
                                           key=f"edit_user_{entry.id}")
                new_password = st.text_input("New Password",
                                           value=entry.password,
                                           key=f"edit_pass_{entry.id}")
                new_notes = st.text_area("New Notes",
                                       value=entry.notes,
                                       key=f"edit_notes_{entry.id}")
                
                if st.form_submit_button("Update"):
                    store.update_entry(entry.id,
                                     username=new_username,
                                     password=new_password,
                                     notes=new_notes)
                    st.rerun()