import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create table if it doesn't exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert records (using parameterized queries to avoid SQL injection)
students_data = [
    ('Kanan', 'Data Science', 'A', 90),
    ('Ainara', 'Data Science', 'B', 50),
    ('Jay', 'Data Science', 'A', 86),
    ('Anurag', 'DEVOPS', 'A', 100),
    ('Val', 'DEVOPS', 'A', 35)
]

cursor.executemany('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)''', students_data)

# Fetch and display inserted data
data = cursor.execute('''SELECT * FROM STUDENT''')
print("The inserted records are:")
for row in data:
    print(row)

# Commit and close the connection
connection.commit()
connection.close()
