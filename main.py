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

# Streamlit UI Enhancements
st.set_page_config(page_title="AI-Powered Fintech", layout="wide")
st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideIn {
            from { transform: translateY(-20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #FF5733;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        .subheader {
            font-size: 25px;
            color: #33FF57;
            text-align: center;
            animation: slideIn 2s ease-in-out;
        }
        .content {
            font-size: 18px;
            color: #FFFFFF;
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 10px;
            text-align: justify;
            animation: fadeIn 3s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Welcome to AI-Powered Fintech</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Revolutionizing Financial Wellness Through AI</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='content'>
        Our AI-powered financial wellness platform is designed to provide users with personalized financial insights,
        budgeting recommendations, investment strategies, and debt management solutions. By leveraging advanced 
        machine learning algorithms, we analyze financial patterns and help users make informed decisions for a 
        secure and prosperous future.
        
        <br><br>
        <strong>Key Features:</strong>
        <ul>
            <li>Smart Budgeting: AI-driven recommendations based on income, expenses, and spending habits.</li>
            <li>Investment Strategies: Tailored investment suggestions aligned with your financial goals.</li>
            <li>Debt Management: Optimize repayments and manage financial obligations effectively.</li>
            <li>Cross-Platform Accessibility: Use our platform on any device, anywhere, anytime.</li>
            <li>Banking API Integration: Securely connect with financial institutions for seamless transactions.</li>
        </ul>
        
        <br>
        Join us in transforming financial management with cutting-edge technology and data-driven insights.
    </div>
""", unsafe_allow_html=True)