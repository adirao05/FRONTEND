import streamlit as st
import pdfplumber
import os
import pandas as pd
from io import BytesIO

# Set page config
st.set_page_config(page_title="PDF to DataFrame", page_icon="📄")

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
