
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
        st.success("Login successful")
        st.markdown("""<div class='cta-button'><a href='/transaction' target='_self'>Transaction</a></div> """, unsafe_allow_html=True)

if "Login successful" not in st.session_state:
    st.session_state["Login successful"] = False

# Check if the user is already logged in
if st.session_state["Login successful"]:
    st.success("You are already logged in!")
    st.switch_page("pages/dashboard.py")  # Automatically redirect to dashboard
else:
    st.title("🔑 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state["Login successful"] = True  # Store login state
            st.session_state["username"] = username
            st.success("Login successful! Redirecting...")
            st.switch_page("pages/dashboard.py")  # Redirect to dashboard
        else:
            st.error("Invalid username or password")


        
