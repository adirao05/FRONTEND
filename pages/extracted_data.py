import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Extracted Data", page_icon="📊")

if "extracted_df" not in st.session_state:
    st.warning("No extracted data. Upload a PDF first.")
    st.stop()

st.title("📊 Extracted PDF Data")

# Display DataFrame
df = st.session_state["extracted_df"]
st.dataframe(df)

# Download as CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download CSV",
    data=csv,
    file_name="extracted_data.csv",
    mime="text/csv"
)

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
