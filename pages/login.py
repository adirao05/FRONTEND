import streamlit as st
import json
import hashlib

# Load user data
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

st.title("🔑 Login Page")

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    users = load_users()
    
    if username in users and users[username] == hash_password(password):
        st.success(f"Welcome back, {username}!")
    else:
        st.error("Invalid username or password")

if st.button("Back to Home"):
    st.switch_page("../main.py")
