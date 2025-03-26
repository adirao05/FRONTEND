import streamlit as st
import sqlite3
import bcrypt

st.title("Signup")

# User input
username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Connect to SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

if st.button("Signup"):
    if password == confirm_password:
        # Check if username exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        if cursor.fetchone():
            st.error("Username already exists!")
        else:
            # Hash the password
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed))
            conn.commit()
            st.success("Account created successfully! Go to the login page.")
    else:
        st.error("Passwords do not match!")

conn.close()
