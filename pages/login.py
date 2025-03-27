
'''import streamlit as st
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
   '''     
import streamlit as st
import sqlite3
import hashlib

# ✅ Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ✅ Authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result and result[0] == hash_password(password):
        return True
    return False

# ✅ Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.title("🔑 Login Page")

# ✅ Show login form if not authenticated
if not st.session_state.authenticated:
    # ✅ Add unique keys for text_input fields
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.success("✅ Login successful!")

    if st.button("Go to Transaction"):
        st.switch_page("transaction.py")

# ✅ Logout button
if st.session_state.authenticated:
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.warning("⚠️ You have been logged out.")
        st.rerun()
