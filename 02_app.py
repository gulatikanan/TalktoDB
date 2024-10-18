# app.py
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="NLP to SQL Query Assistant", page_icon="🔍")

st.title("Welcome to NLP to SQL Query Assistant")
st.write("This app helps you connect to a database and convert natural language to SQL queries.")

st.subheader("How to use this app:")
st.write("1. Register or log in to your account.")
st.write("2. Go to the 'Database Connection' page to set up your database connection.")
st.write("3. Navigate to the 'NLP to SQL' page to convert natural language to SQL queries and execute them.")
st.write("4. View your profile and past queries on the 'User Profile' page.")

st.sidebar.success("Select a page above.")

# Initialize session state
if 'user' not in st.session_state:
    st.session_state['user'] = None

if 'db_connection' not in st.session_state:
    st.session_state['db_connection'] = None

# Add login/logout button to sidebar
if st.session_state['user']:
    if st.sidebar.button("Logout"):
        st.session_state['user'] = None
        st.session_state['db_connection'] = None
        st.success("Logged out successfully!")
else:
    st.sidebar.write("Please log in or register to use the app.")