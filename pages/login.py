import streamlit as st
import sqlite3
import hashlib

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    conn.close()

    if result and result[0] == hash_password(password):
        return True
    return False

st.title("🔑 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if authenticate_user(username, password):
        st.success(f"Welcome back, {username}!")
    else:
        st.error("Invalid username or password")
