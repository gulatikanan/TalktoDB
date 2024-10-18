# # pages/3_NLP_to_SQL.py
# import streamlit as st
# import pandas as pd
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# import sqlite3
# # Load environment variables
# load_dotenv()

# # Configure Google Gemini API key
# api_key = os.getenv("GOOGLE_API_KEY")
# if api_key:
#     genai.configure(api_key=api_key)
# else:
#     st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

# # Function to get the SQL response from Google Gemini
# def get_gemini_response(question, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         response = model.generate_content([prompt[0], question])
#         return response.text
#     except Exception as e:
#         st.error(f"Error generating SQL query: {str(e)}")
#         return None

# # Function to read SQL query from the connected database
# def read_sql_query(sql, connection):
#     try:
#         cur = connection.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         column_names = [description[0] for description in cur.description]
#         return rows, column_names
#     except Exception as e:
#         st.error(f"Error executing SQL query: {str(e)}")
#         return None, None

# st.title("Natural Language to SQL")

# if 'user' not in st.session_state or not st.session_state['user']:
#     st.warning("Please log in to use this feature.")
# elif 'db_connection' not in st.session_state or not st.session_state['db_connection']:
#     st.warning("Please connect to a database first on the Database Connection page.")
# else:
#     st.write(f"Logged in as: {st.session_state['user']}")

#     # Define your prompt for Google Gemini
#     prompt = ["""
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
#     For example:
#     1. How many records are present? => SELECT COUNT(*) FROM STUDENT;
#     2. List all students studying Data Science => SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
#     """]

#     question = st.text_input("Enter your question:")
#     if st.button("Generate SQL"):
#         if question:
#             # Get SQL query from Gemini API
#             response = get_gemini_response(question, prompt)
#             if response:
#                 cleaned_response = response.strip()

#                 st.subheader("Generated SQL Query:")
#                 st.code(cleaned_response, language="sql")

#                 # Execute the SQL query button
#                 if st.button("Execute Query"):
#                     # Execute the SQL query on the connected database
#                     data, column_names = read_sql_query(cleaned_response, st.session_state['db_connection'])
#                     if data and column_names:
#                         st.subheader("Query Results:")
#                         df = pd.DataFrame(data, columns=column_names)
#                         st.table(df)
#                     elif data is None and column_names is None:
#                         st.warning("Error occurred while executing the query.")
#                     else:
#                         st.info("Query executed successfully, but no data was returned.")
#         else:
#             st.error("Please enter a valid question.")

# # Add query to user's history
# def add_query_to_history(username, query):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO user_queries (username, query) VALUES (?, ?)", (username, query))
#     conn.commit()
#     conn.close()

# # If a query was executed, add it to the user's history
# if 'last_executed_query' in st.session_state:
#     add_query_to_history(st.session_state['user'], st.session_state['last_executed_query'])
#     del st.session_state['last_executed_query']




# ----------------------------------------------------------------------
# pages/3_NLP_to_SQL.py
# import streamlit as st
# import pandas as pd
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# import sqlite3

# # Load environment variables
# load_dotenv()

# # Configure Google Gemini API key
# api_key = os.getenv("GOOGLE_API_KEY")
# if api_key:
#     genai.configure(api_key=api_key)
# else:
#     st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

# # Function to get the SQL response from Google Gemini
# def get_gemini_response(question, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         response = model.generate_content([prompt[0], question])
#         return response.text
#     except Exception as e:
#         st.error(f"Error generating SQL query: {str(e)}")
#         return None

# # Function to read SQL query from the connected database
# def read_sql_query(sql, connection):
#     try:
#         cur = connection.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         column_names = [description[0] for description in cur.description]
#         return rows, column_names
#     except Exception as e:
#         st.error(f"Error executing SQL query: {str(e)}")
#         return None, None

# # Function to save query to user history
# def save_query_to_history(username, query):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS user_queries
#                  (username TEXT, query TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
#     c.execute("INSERT INTO user_queries (username, query) VALUES (?, ?)", (username, query))
#     conn.commit()
#     conn.close()

# st.title("Natural Language to SQL")

# if 'user' not in st.session_state or not st.session_state['user']:
#     st.warning("Please log in to use this feature.")
# elif 'db_connection' not in st.session_state or not st.session_state['db_connection']:
#     st.warning("Please connect to a database first on the Database Connection page.")
# else:
#     st.write(f"Logged in as: {st.session_state['user']}")

#     # Define your prompt for Google Gemini
#     prompt = ["""
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
#     For example:
#     1. How many records are present? => SELECT COUNT(*) FROM STUDENT;
#     2. List all students studying Data Science => SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
#     """]

#     question = st.text_input("Enter your question:")
#     if st.button("Generate SQL"):
#         if question:
#             # Get SQL query from Gemini API
#             response = get_gemini_response(question, prompt)
#             if response:
#                 cleaned_response = response.strip()

#                 st.subheader("Generated SQL Query:")
#                 st.code(cleaned_response, language="sql")

#                 # Execute the SQL query button
#                 if st.button("Execute Query"):
#                     # Execute the SQL query on the connected database
#                     data, column_names = read_sql_query(cleaned_response, st.session_state['db_connection'])
#                     if data and column_names:
#                         st.subheader("Query Results:")
#                         df = pd.DataFrame(data, columns=column_names)
#                         st.table(df)
                        
#                         # Save the query to user history
#                         save_query_to_history(st.session_state['user'], cleaned_response)
#                         st.success("Query executed and saved to history.")
#                     elif data is None and column_names is None:
#                         st.warning("Error occurred while executing the query.")
#                     else:
#                         st.info("Query executed successfully, but no data was returned.")
                        
#                         # Save the query to user history even if no data was returned
#                         save_query_to_history(st.session_state['user'], cleaned_response)
#                         st.success("Query saved to history.")
#         else:
#             st.error("Please enter a valid question.")

# # Add a section to display recent queries
# st.subheader("Recent Queries")
# conn = sqlite3.connect('users.db')
# c = conn.cursor()
# c.execute("SELECT query, timestamp FROM user_queries WHERE username=? ORDER BY timestamp DESC LIMIT 5", (st.session_state['user'],))
# recent_queries = c.fetchall()
# conn.close()

# if recent_queries:
#     for query, timestamp in recent_queries:
#         st.text(f"Query: {query}")
#         st.text(f"Timestamp: {timestamp}")
#         st.markdown("---")
# else:
#     st.write("No recent queries found.")


# #############################################################################



import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv
import sqlite3
import re

# # Load environment variables
# load_dotenv()

# # Configure Google Gemini API key
# api_key = os.getenv("GOOGLE_API_KEY")
# if api_key:
#     genai.configure(api_key=api_key)
# else:
#     st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

# # Function to get the SQL response from Google Gemini
# def get_gemini_response(question, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         response = model.generate_content([prompt[0], question])
#         return response.text
#     except Exception as e:
#         st.error(f"Error generating SQL query: {str(e)}")
#         return None

# # Function to clean the generated SQL by removing markdown formatting (e.g., backticks)
# def clean_sql_query(query):
#     cleaned_query = re.sub(r'```sql|```', '', query).strip()
#     return cleaned_query

# # Function to read SQL query from the connected database
# def read_sql_query(sql, connection):
#     try:
#         cur = connection.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         column_names = [description[0] for description in cur.description]
#         return rows, column_names
#     except Exception as e:
#         st.error(f"Error executing SQL query: {str(e)}")
#         return None, None

# # Function to save query to user history
# def save_query_to_history(username, query):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS user_queries
#                  (username TEXT, query TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
#     c.execute("INSERT INTO user_queries (username, query) VALUES (?, ?)", (username, query))
#     conn.commit()
#     conn.close()

# st.title("Natural Language to SQL")

# if 'user' not in st.session_state or not st.session_state['user']:
#     st.warning("Please log in to use this feature.")
# elif 'db_connection' not in st.session_state or not st.session_state['db_connection']:
#     st.warning("Please connect to a database first on the Database Connection page.")
# else:
#     st.write(f"Logged in as: {st.session_state['user']}")

#     # Define your prompt for Google Gemini
#     prompt = ["""
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
#     For example:
#     1. How many records are present? => SELECT COUNT(*) FROM STUDENT;
#     2. List all students studying Data Science => SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
#     """]

#     question = st.text_input("Enter your question:")
#     if st.button("Generate SQL"):
#         if question:
#             # Get SQL query from Gemini API
#             response = get_gemini_response(question, prompt)
#             if response:
#                 # Clean the generated SQL query
#                 cleaned_response = clean_sql_query(response)

#                 st.subheader("Generated SQL Query:")
#                 st.code(cleaned_response, language="sql")

#                 # Execute the SQL query button
#                 if st.button("Execute Query"):
#                     # Execute the SQL query on the connected database
#                     data, column_names = read_sql_query(cleaned_response, st.session_state['db_connection'])
#                     if data and column_names:
#                         st.subheader("Query Results:")
#                         df = pd.DataFrame(data, columns=column_names)
#                         st.table(df)
                        
#                         # Save the query to user history
#                         save_query_to_history(st.session_state['user'], cleaned_response)
#                         st.success("Query executed and saved to history.")
#                     elif data is None and column_names is None:
#                         st.warning("Error occurred while executing the query.")
#                     else:
#                         st.info("Query executed successfully, but no data was returned.")
                        
#                         # Save the query to user history even if no data was returned
#                         save_query_to_history(st.session_state['user'], cleaned_response)
#                         st.success("Query saved to history.")
#         else:
#             st.error("Please enter a valid question.")

# # Add a section to display recent queries
# st.subheader("Recent Queries")
# conn = sqlite3.connect('users.db')
# c = conn.cursor()
# c.execute("SELECT query, timestamp FROM user_queries WHERE username=? ORDER BY timestamp DESC LIMIT 5", (st.session_state['user'],))
# recent_queries = c.fetchall()
# conn.close()

# if recent_queries:
#     for query, timestamp in recent_queries:
#         st.text(f"Query: {query}")
#         st.text(f"Timestamp: {timestamp}")
#         st.markdown("---")
# else:
#     st.write("No recent queries found.")



###########################################

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import re

####################################################
####################################################

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to Load Google Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, question])  # Can also give Multiple Prompts
    return response.text

# Function to Retrieve query from the SQL database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.OperationalError as e:
        st.error(f"SQL Error: {e}")
        return []

# Define Your Prompt
prompt = """
You are an expert in converting English questions to SQL queries!
The SQL database is called STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.

For example: 
1. Question: How many entries of records are present?
   SQL: SELECT COUNT(*) FROM STUDENT;

2. Question: Tell me all the students studying in the Data Science class.
   SQL: SELECT * FROM STUDENT WHERE CLASS = "Data Science";

The SQL code should not include any 'BEGIN' or 'END' markers.
"""


# Function to clean the generated SQL by removing markdown formatting (e.g., backticks)
def clean_sql_query(query):
    # Remove backticks and language hints like ```sql
    cleaned_query = re.sub(r'```sql|```', '', query).strip()
    return cleaned_query


# Streamlit App UI
st.set_page_config(page_title="Retrieve Any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

# Input and Button
question = st.text_input("Enter your question:", key="input")
submit = st.button("Ask the question")

# If the submit button is clicked
if submit:
    # Fetch the SQL query response from Google Gemini API
    response = get_gemini_response(question, prompt)
    
    # Clean the generated SQL to remove markdown formatting
    cleaned_response = clean_sql_query(response)

    # Display the generated SQL for debugging purposes
    st.subheader("Generated SQL Query:")
    st.code(cleaned_response, language="sql")

    try:
        # Execute the cleaned SQL query on the 'student.db'
        data = read_sql_query(cleaned_response, "student.db")

        # If data is returned, format and display it
        if data:
            st.subheader("Query Results:")

            # Clean up and format the data
            cleaned_data = [list(row) for row in data]  # Convert tuples to lists

            # Display results as a table using Streamlit
            st.table(cleaned_data)

        else:
            st.write("No data returned.")
    except Exception as e:
        st.error(f"SQL Error: {str(e)}")
