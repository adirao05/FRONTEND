import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

st.set_page_config(page_title="Finance App", layout="wide")

# Check if user is logged in
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("Please login first.")
    st.stop()

st.title(f"Welcome {st.session_state['username']}!")

# Main App Content
st.write("This is your financial dashboard.")
if st.button("Logout"):
    st.session_state["authenticated"] = False
    st.experimental_rerun()

