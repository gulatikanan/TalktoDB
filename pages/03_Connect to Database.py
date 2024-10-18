# pages/2_Database_Connection.py
import streamlit as st
import sqlite3
import pymysql
import psycopg2

def connect_to_db(db_type, host, port, user, password, db_name):
    if db_type == 'SQLite':
        connection = sqlite3.connect(db_name)
    elif db_type == 'MySQL':
        connection = pymysql.connect(host=host, user=user, password=password, database=db_name, port=int(port))
    elif db_type == 'PostgreSQL':
        connection = psycopg2.connect(host=host, user=user, password=password, database=db_name, port=int(port))
    return connection

st.title("Database Connection")

if 'user' not in st.session_state or not st.session_state['user']:
    st.warning("Please log in to connect to a database.")
else:
    st.write(f"Logged in as: {st.session_state['user']}")

    # User input for database connection
    db_type = st.selectbox("Select Database Type", options=["SQLite", "MySQL", "PostgreSQL"])
    host = st.text_input("Host", value="localhost" if db_type != "SQLite" else "")
    port = st.text_input("Port", value="5432" if db_type == "PostgreSQL" else "3306" if db_type == "MySQL" else "")
    user = st.text_input("Username", value="root" if db_type == "MySQL" else "postgres" if db_type == "PostgreSQL" else "")
    password = st.text_input("Password", type="password")
    db_name = st.text_input("Database Name", value="student.db" if db_type == "SQLite" else "")

    # Connect button
    if st.button("Connect"):
        try:
            connection = connect_to_db(db_type, host, port, user, password, db_name)
            st.session_state['db_connection'] = connection
            st.success("Database connected successfully!")
        except Exception as e:
            st.error(f"Failed to connect to the database: {str(e)}")

    # Disconnect button
    if st.button("Disconnect"):
        if 'db_connection' in st.session_state and st.session_state['db_connection']:
            st.session_state['db_connection'].close()
            st.session_state['db_connection'] = None
            st.success("Disconnected from the database.")
        else:
            st.warning("No active database connection.")
