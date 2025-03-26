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
        @keyframes bgTransition {
            0% { background: #0f2027; }
            50% { background: #203a43; }
            100% { background: #2c5364; }
        }
        body {
            background: linear-gradient(to right, #0f2027, #203a43);
            animation: bgTransition 5s ease-in-out infinite alternate;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 60px 20px;
        }
        .title {
            font-size: 60px;
            font-weight: bold;
            color: #FFD700;
            animation: slideIn 2s ease-in-out;
        }
        .subheader {
            font-size: 28px;
            color: #FFA500;
            animation: fadeIn 3s ease-in-out;
            margin-bottom: 20px;
        }
        .content {
            font-size: 20px;
            max-width: 900px;
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: left;
            animation: fadeIn 3s ease-in-out;
        }
        .cta-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .cta-button a {
            background: #FFD700;
            color: #000;
            padding: 12px 30px;
            font-size: 20px;
            font-weight: bold;
            text-decoration: none;
            border-radius: 5px;
            transition: 0.3s;
        }
        .cta-button a:hover {
            background: #FFA500;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='container'>
        <div class='title'>Welcome to AI-Powered Fintech</div>
        <div class='subheader'>Revolutionizing Financial Wellness Through AI</div>
        <div class='content'>
            <p>Our AI-powered financial wellness platform is designed to provide users with personalized financial insights,
            budgeting recommendations, investment strategies, and debt management solutions. By leveraging advanced 
            machine learning algorithms, we analyze financial patterns and help users make informed decisions for a 
            secure and prosperous future.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
*Key Features:*

                               - 📊 *Smart Budgeting*: AI-driven recommendations based on income, expenses, and spending habits.
                    - 💹 *Investment Strategies*: Tailored investment suggestions aligned with your financial goals.
                    - 📉 *Debt Management*: Optimize repayments and manage financial obligations effectively.
                    - 🌍 *Cross-Platform Accessibility*: Use our platform on any device, anywhere, anytime.
                    - 🔒 *Banking API Integration*: Securely connect with financial institutions for seamless transactions.
""")

st.markdown("""
    <div class='cta-button'>
        <a href='/signup' target='_self'>Get Started</a>
    </div>
""", unsafe_allow_html=True)



