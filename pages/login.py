import streamlit as st
import bcrypt
import json
import os

# ---- Helper Functions ----
def load_users():
    """Load users from a JSON file"""
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

users = load_users()

# ---- Login Form ----
st.title("🔑 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users:
        stored_hashed_password = users[username]["password"]

        # ✅ Verify password
        if bcrypt.checkpw(password.encode("utf-8"), stored_hashed_password.encode("utf-8")):
            st.session_state["authentication_status"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}! 🎉")
        else:
            st.error("Incorrect password")
    else:
        st.error("User not found")

# ---- Navigation ----
if st.button("Go to Signup"):
    st.switch_page("signup.py")

if st.session_state.get("authentication_status"):
    st.write("✅ You are logged in.")
    if st.button("Logout"):
        st.session_state["authentication_status"] = None
        st.experimental_rerun()
