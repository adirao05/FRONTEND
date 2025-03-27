import streamlit as st

# ✅ Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ You must log in to access this page.")
    st.stop()  # Stop further execution if not logged in

# 🎯 Display the page content only for logged-in users
st.title("💰 Financial Information Form")

# Input fields
yearly_income = st.number_input("🏦 Yearly Income ($)", min_value=0.0, max_value=1_000_000.0, step=1000.0, format="%.2f")
total_debt = st.number_input("💳 Total Debt ($)", min_value=0.0, max_value=1_000_000.0, step=500.0, format="%.2f")
credit_score = st.number_input("📊 Credit Score", min_value=300, max_value=850, step=1)

# ✅ Add unique keys to the buttons
if st.button("Submit", key="submit_btn"):
    st.success("✅ Information Submitted Successfully!")
    
    # Display the entered information
    st.write("### 📄 Summary")
    st.write(f"**Yearly Income:** ${yearly_income:,.2f}")
    st.write(f"**Total Debt:** ${total_debt:,.2f}")
    st.write(f"**Credit Score:** {credit_score}")

# 🔓 Logout button with unique key
if st.button("Logout", key="logout_btn"):
    st.session_state["logged_in"] = False
    st.success("✅ Logged out successfully!")
    st.rerun()

import streamlit as st

# ✅ Ensure authentication is checked at the beginning
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("⚠️ Please log in first.")
    st.switch_page("pages/login.py")  # Redirect back to login page

# ✅ If logged in, display the content
st.title("📊 Debt Model")
st.write("You are now viewing the Debt Model page.")
