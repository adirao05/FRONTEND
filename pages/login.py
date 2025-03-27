
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

# ✅ Function to authenticate user
def authenticate_user(username, password):
    """Check user credentials from SQLite database"""
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

# Only show login form if not authenticated
if not st.session_state.authenticated:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.success("✅ Login successful!")

            # ✅ Redirect to transaction page
            st.rerun()  # 🔥 Updated rerun function
        else:
            st.error("❌ Invalid username or password")
else:
    st.success("✅ You are already logged in!")

    # ✅ Button to navigate to transaction page
    if st.button("Go to Transaction"):
        st.switch_page("pages/transaction.py")

# ✅ Logout button
if st.session_state.authenticated:
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.warning("⚠️ You have been logged out.")
        st.rerun()  # 🔥 Updated rerun function


if st.button("Login"):
    if authenticate_user(username, password):
        st.session_state["logged_in"] = True
        st.success("✅ Login successful!")
        st.switch_page("pages/financial_info.py")  # Redirect to the restricted page
    else:
        st.error("❌ Invalid username or password")

