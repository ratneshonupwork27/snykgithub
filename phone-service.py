import sqlite3

# VULNERABLE: Direct concatenation of user input into a SQL statement
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

user_id = input("Enter User ID: ")
query = "SELECT * FROM users WHERE id = " + user_id
cursor.execute(query)  # Vulnerable to SQL injection if input is `1 OR 1=1`
