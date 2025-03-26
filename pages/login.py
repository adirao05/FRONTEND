import streamlit as st
import json
import hashlib
import os

# Load user data
def load_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)  # Create an empty JSON file
    with open("users.json", "r") as file:
        return json.load(file)

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

st.title("🔑 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    users = load_users()
    
    if username in users and users[username] == hash_password(password):
        st.success(f"Welcome back, {username}!")
    else:
        st.error("Invalid username or password")

st.sidebar.page_link("main.py", label="🏠 Home")
st.sidebar.page_link("pages/2_Sign_Up.py", label="📝 Sign Up")
