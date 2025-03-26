import streamlit as st
import sqlite3

# Initialize database connection
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize DB
init_db()

st.set_page_config(page_title="Auth App", layout="centered")

st.title("🏠 Welcome to the Authentication App")

st.write("Use the sidebar to navigate to the Login or Sign Up page.")
