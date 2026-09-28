import os

print(os.path.abspath("room_expense.db"))


import sqlite3
connection = sqlite3.connect("room_expense.db")
cursor = connection.cursor()
"""Send this SQL command to the SQLite database."""

cursor.execute("""  
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    item TEXT NOT NULL,
    price INTEGER NOT NULL CHECK(price > 0),
    date TEXT NOT NULL
    )
""")

connection.commit()

def execute_query(query,values):
    cursor.execute(query, values)
    connection.commit()
    return cursor.rowcount

def fetch_query(query,values = ()):
    cursor.execute(query,values)
    return cursor.fetchall()