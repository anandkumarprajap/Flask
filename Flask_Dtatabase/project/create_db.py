import sqlite3

conn = sqlite3.connect('site.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
""")

conn.commit()
conn.close()