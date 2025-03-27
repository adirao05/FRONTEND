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

# Button to submit
if st.button("Submit"):
    st.success("✅ Information Submitted Successfully!")
    
    # Display the entered information
    st.write("### 📄 Summary")
    st.write(f"**Yearly Income:** ${yearly_income:,.2f}")
    st.write(f"**Total Debt:** ${total_debt:,.2f}")
    st.write(f"**Credit Score:** {credit_score}")

    # You can further process this data as needed (e.g., save to a database or use it in calculations)

# 🔓 Logout button
if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.success("✅ Logged out successfully!")
    st.experimental_rerun()
