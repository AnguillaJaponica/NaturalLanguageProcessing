import json
import sqlite3

conn = None

def connect():
    global conn
    conn = sqlite3.connect('./sample.db')

def close():
    conn.close()

def create_table():
    conn.execute('DROP TABLE IF EXISTS docs')
    conn.execute('''CREATE TABLE docs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        meta_info BLOB,
        sentence BLOB,
        chunk BLOB,
        token BLOB
    )''')