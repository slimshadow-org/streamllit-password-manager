import streamlit as st
from pages.auth import check_authentication
from pages.password_list import show_password_list
from pages.add_password import show_add_password
from pages.generate_password import show_password_generator

st.set_page_config(page_title="Secure Password Manager", page_icon="🔒")

def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        check_authentication()
    else:
        st.title("🔒 Secure Password Manager")
        
        tab1, tab2, tab3 = st.tabs(["Passwords", "Add New", "Generator"])
        
        with tab1:
            show_password_list()
            
        with tab2:
            show_add_password()
            
        with tab3:
            show_password_generator()

if __name__ == "__main__":
    main()