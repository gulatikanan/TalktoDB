# pages/1_Login_Register.py
import streamlit as st
import hashlib
import sqlite3

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create users table
def create_users_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new user
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    conn.close()

# Function to verify user
def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash_password(password)))
    result = c.fetchone()
    conn.close()
    return result is not None

# Create users table
create_users_table()

st.title("Login / Register")

# Login Form
st.header("Login")
login_username = st.text_input("Username", key="login_username")
login_password = st.text_input("Password", type="password", key="login_password")
if st.button("Login"):
    if verify_user(login_username, login_password):
        st.session_state['user'] = login_username
        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password")

# Registration Form
st.header("Register")
reg_username = st.text_input("Username", key="reg_username")
reg_password = st.text_input("Password", type="password", key="reg_password")
if st.button("Register"):
    if reg_username and reg_password:
        try:
            add_user(reg_username, reg_password)
            st.success("Registered successfully! You can now log in.")
        except sqlite3.IntegrityError:
            st.error("Username already exists. Please choose a different one.")
    else:
        st.error("Please enter both username and password")
