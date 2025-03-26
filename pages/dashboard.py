import streamlit as st
import pdfplumber
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Dashboard", page_icon="📊")

# Ensure user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("You are not logged in.")
    st.stop()

# Get the current user
username = st.session_state["username"]

# Create upload folder
upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)

# PDF uploader
st.title(f"📄 Welcome, {username}")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# PDF extraction
def extract_tables(pdf_path):
    all_data = []
    column_names = None

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_table = page.extract_table()
                if extracted_table:
                    if column_names is None:
                        column_names = extracted_table[0]
                        all_data.extend(extracted_table[1:])
                    else:
                        if extracted_table[0] == column_names:
                            all_data.extend(extracted_table[1:])
                        else:
                            all_data.extend(extracted_table)

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
    file_path = os.path.join(upload_folder, f"{username}_{uploaded_file.name}")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("PDF uploaded successfully!")

    # Extract tables
    with st.spinner("Extracting tables..."):
        df = extract_tables(file_path)

        if df is not None:
            st.session_state["extracted_df"] = df
            st.success("Tables extracted successfully! Go to the extracted data page.")
        else:
            st.warning("No tables found.")
