import streamlit as st
import sqlite3

# Initialize database connection
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize DB
init_db()

import streamlit as st
import pandas as pd
import numpy as np
import time

# Function for AI-based financial advice
def generate_financial_advice(income, expenses, investment_goal, debt_level):
    savings = income - expenses
    advice = ""
    
    if savings > 0:
        advice += f"Great! You're saving {savings} per month. "
    else:
        advice += "You're spending more than you earn! Consider cutting unnecessary expenses. "
    
    if debt_level > 0:
        advice += "Focus on reducing your debt first before making major investments. "
    else:
        advice += "You have no debt! Consider diversifying your investments. "
    
    if investment_goal.lower() == "high growth":
        advice += "Look into high-return investments like stocks or ETFs."
    elif investment_goal.lower() == "low risk":
        advice += "Consider bonds, fixed deposits, or index funds for stability."
    else:
        advice += "A balanced portfolio with a mix of stocks and bonds could work well."
    
    return advice

# Streamlit UI Enhancements
st.set_page_config(page_title="AI-Powered Fintech", layout="wide")
st.markdown("""
    <style>
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #FF5733;
            text-align: center;
        }
        .subheader {
            font-size: 25px;
            color: #33FF57;
            text-align: center;
        }
        .stButton > button {
            background-color: #007BFF;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>AI-Powered Financial Wellness Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Personalized financial insights, budgeting, and investment strategies</div>", unsafe_allow_html=True)

# User Inputs with Animation
col1, col2 = st.columns(2)
with col1:
    income = st.number_input("💰 Monthly Income ($)", min_value=0, value=5000, step=100)
    expenses = st.number_input("💸 Monthly Expenses ($)", min_value=0, value=3000, step=100)
    investment_goal = st.selectbox("🎯 Investment Goal", ["High Growth", "Low Risk", "Balanced"])
with col2:
    debt_level = st.number_input("📉 Existing Debt Level ($)", min_value=0, value=0, step=100)
    age = st.slider("📅 Your Age", 18, 70, 30)
    risk_tolerance = st.select_slider("⚖ Risk Tolerance", ["Low", "Medium", "High"], value="Medium")

# Animated Button
if st.button("🚀 Get Financial Advice"):
    with st.spinner("Analyzing your financial status..."):
        time.sleep(2)
    advice = generate_financial_advice(income, expenses, investment_goal, debt_level)
    st.success(advice)