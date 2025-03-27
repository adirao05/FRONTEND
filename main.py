import streamlit as st
import sqlite3

#BACKGROUND COLOUR
st.set_page_config(page_title="AI-Powered Fintech",layout="wide")

st.markdown(
    """
    <style>
        /* Main page background */
        .main {
            background: linear-gradient(135deg, #FFA500, #32CD32);  
        }

        /* Sidebar background */
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #32CD32, #FFA500);  
        }
    </style>
    """,
    unsafe_allow_html=True
)



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



import streamlit as st
import pdfplumber
import os
import pandas as pd
from io import BytesIO


# Create upload folder
upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)

# Title
st.title("📄 PDF to DataFrame Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# PDF Extraction function
def extract_tables_from_pdf(pdf_path):
    """Extract tables from PDF and return as DataFrame"""
    all_data = []
    column_names = None
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_table()
                
                if tables:
                    if column_names is None:
                        column_names = tables[0]  # First row as headers
                        all_data.extend(tables[1:])  # Skip headers
                    else:
                        all_data.extend(tables[1:])
        
        if all_data and column_names:
            df = pd.DataFrame(all_data, columns=column_names)
            return df
        else:
            return None
    except Exception as e:
        st.error(f"Error extracting PDF: {str(e)}")
        return None

# Handle PDF upload
if uploaded_file:
    # Save PDF
    pdf_path = os.path.join(upload_folder, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("PDF uploaded successfully!")

    # Extract tables
    with st.spinner("Extracting tables..."):
        df = extract_tables_from_pdf(pdf_path)
        
        if df is not None:
            st.success("Tables extracted successfully!")

            # Display the DataFrame
            st.write("### Extracted Data:")
            st.dataframe(df)

            # Download as CSV
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", data=csv, file_name="extracted_data.csv", mime="text/csv")

            # Download as Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            output.seek(0)

            st.download_button(
                "Download Excel",
                data=output,
                file_name="extracted_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("No tables found in the PDF.")



