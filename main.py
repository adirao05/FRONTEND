import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar
st.sidebar.title("Finance Dashboard")
st.sidebar.metric("Balance", "$2,000")
st.sidebar.write("📊 Menu")
st.sidebar.button("Dashboard")
st.sidebar.button("Transaction History")
st.sidebar.button("Investments")
st.sidebar.button("Settings")

# Main Dashboard
st.title("Financial Dashboard")

# Transaction History
st.header("📜 Transaction History")
transactions = pd.DataFrame({
    "Date": ["2025-03-01", "2025-03-15", "2025-03-20"],
    "Description": ["Rent", "Food Delivery", "Gas"],
    "Amount": [-1200, -35, -50]
})
st.table(transactions)

# Spending Pattern Chart
st.header("💡 Spending Pattern")
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Spending': [400, 300, 500, 450],
    'Income': [600, 700, 800, 750]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.bar(df['Month'], df['Spending'], label='Spending', color='orange')
ax.bar(df['Month'], df['Income'], label='Income', color='green', alpha=0.7)
ax.legend()
st.pyplot(fig)

# Financial Goal
st.header("🎯 Financial Goal Progress")
st.progress(0.7)

# Investment Strategy
st.header("📈 Investment Strategy")
st.write("✅ Stocks: 50% | ✅ Bonds: 30% | ✅ Crypto: 20%")

# Debt Repayment
st.header("💳 Debt Repayment")
st.write("Credit Card: $500 remaining")
st.write("Mortgage: $150,000 remaining")

# Credit Score Improvement
st.header("📊 Credit Score Improvement")
track_improvement = st.toggle("Track Credit Score Improvement")
