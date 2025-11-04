import streamlit as st

st.set_page_config(page_title="PSBFinance", layout="wide")

section = st.sidebar.radio("📂 Navigate", ["About Us", "General Knowledge"])

if section == "About Us":
    st.title("🧠 Welcome to PSBFinance")
    st.image("https://raw.githubusercontent.com/YOUR_USERNAME/psbfinance-v2/main/capilotimage.png", use_column_width=True)
    st.markdown("""
    ### Built by students for students.

    PSBFinance is a learning dashboard designed to make finance accessible, visual, and practical.
    """)

if section == "General Knowledge":
    st.header("📚 General Finance Knowledge")
    st.info("Hull's book summary will appear here once PyMuPDF is installed.")

