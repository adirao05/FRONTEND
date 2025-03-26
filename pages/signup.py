import streamlit as st
import streamlit_authenticator as stauth
import json
import os

# ---- Helper functions ----
def save_users(users):
    """Save users to a JSON file"""
    with open("users.json", "w") as f:
        json.dump(users, f)

def load_users():
    """Load users from a JSON file"""
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

users = load_users()

# ---- Signup Form ----
st.title("📝 Signup")

new_username = st.text_input("Choose a username")
new_password = st.text_input("Create a password", type="password")
confirm_password = st.text_input("Confirm password", type="password")

if st.button("Sign Up"):
    if new_password == confirm_password:
        if new_username in users:
            st.error("Username already exists")
        else:
            # 🔥 Correct hashing method
            hashed_password = stauth.Hasher([new_password]).generate()[0]

            users[new_username] = {
                "password": hashed_password
            }
            save_users(users)
            st.success("Account created successfully! Go to the login page.")
    else:
        st.error("Passwords do not match")

# ---- Navigation ----
if st.button("Go to Login"):
    st.switch_page("login.py")
