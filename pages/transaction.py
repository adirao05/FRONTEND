import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transaction History", page_icon="📜", layout="wide")

# Sample transaction data
transactions = pd.DataFrame({"Date": ["2025-03-01", "2025-03-10", "2025-03-15", "2025-03-20"],
    "Description": ["Rent", "Groceries", "Gas", "Subscription"],
    "Category": ["Housing", "Food", "Transport", "Entertainment"],
    "Amount": [-1200, -350, -50, -20]
})

st.title("📜 Transaction History")

st.table(transactions)

# Add a button to return to the main page
if st.button("Back to Dashboard"):
    st.switch_page("main.py")

