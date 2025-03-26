import streamlit as st
import sqlite3
import bcrypt

st.title("Login")

# User input
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# SQLite connection
conn = sqlite3.connect('db/users.db')
cursor = conn.cursor()

if st.button("Login"):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        stored_password = user[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            st.success(f"Welcome, {username}!")
            # Store login status in session state
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.experimental_rerun()  # Redirect to main page
        else:
            st.error("Invalid password.")
    else:
        st.error("Username not found!")

conn.close()
