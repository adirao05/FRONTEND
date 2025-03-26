import streamlit as st
import os

st.set_page_config(page_title="View Files", page_icon="📁")

# Ensure the user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("You are not logged in.")
    st.stop()

username = st.session_state["username"]

# List uploaded PDFs
st.title("📁 Your Uploaded Files")

upload_folder = "uploads"
user_files = [f for f in os.listdir(upload_folder) if f.startswith(username)]

if user_files:
    for file in user_files:
        file_path = os.path.join(upload_folder, file)
        with open(file_path, "rb") as f:
            st.download_button(label=f"Download {file}", data=f, file_name=file, mime="application/pdf")
else:
    st.info("No uploaded files yet.")
