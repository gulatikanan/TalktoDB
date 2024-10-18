# # pages/4_User_Profile.py
# import streamlit as st
# import sqlite3

# def get_user_queries(username):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute("SELECT query, timestamp FROM user_queries WHERE username=? ORDER BY timestamp DESC", (username,))
#     queries = c.fetchall()
#     conn.close()
#     return queries

# st.title("User Profile")

# if not st.session_state['user']:
#     st.warning("Please log in to view your profile.")
# else:
#     st.write(f"Welcome, {st.session_state['user']}!")

#     # Display user information
#     st.subheader("User Information")
#     st.write(f"Username: {st.session_state['user']}")
    
#     # Display past queries
#     st.subheader("Past Queries")
#     queries = get_user_queries(st.session_state['user'])
#     if queries:
#         for query, timestamp in queries:
#             st.text(f"Query: {query}")
#             st.text(f"Timestamp: {timestamp}")
#             st.markdown("---")
#     else:
#         st.write("No past queries found.")

#     # Add more profile features here (e.g., change password, update email, etc.)



# pages/4_User_Profile.py
import streamlit as st
import sqlite3

def create_user_queries_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_queries
                 (username TEXT, query TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def get_user_queries(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT query, timestamp FROM user_queries WHERE username=? ORDER BY timestamp DESC", (username,))
    queries = c.fetchall()
    conn.close()
    return queries

# Ensure the user_queries table exists
create_user_queries_table()

st.title("User Profile")

if 'user' not in st.session_state or not st.session_state['user']:
    st.warning("Please log in to view your profile.")
else:
    st.write(f"Welcome, {st.session_state['user']}!")

    # Display user information
    st.subheader("User Information")
    st.write(f"Username: {st.session_state['user']}")
    
    # Display past queries
    st.subheader("Past Queries")
    queries = get_user_queries(st.session_state['user'])
    if queries:
        for query, timestamp in queries:
            st.text(f"Query: {query}")
            st.text(f"Timestamp: {timestamp}")
            st.markdown("---")
    else:
        st.write("No past queries found.")

    # Add more profile features here (e.g., change password, update email, etc.)