import streamlit as st
import json
import hashlib
import os

# Load and save user data
def load_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)  # Create an empty JSON file
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

st.title("📝 Sign Up Page")

new_username = st.text_input("Choose a Username")
new_password = st.text_input("Create a Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if new_password != confirm_password:
        st.error("Passwords do not match")
    else:
        users = load_users()

        if new_username in users:
            st.error("Username already exists!")
        else:
            # Hash and save the new user
            users[new_username] = hash_password(new_password)
            save_users(users)
            st.success(f"Account created for {new_username}!")

st.sidebar.page_link("../main.py", label="🏠 Home")
st.sidebar.page_link("1_Login.py", label="🔑 Login")
