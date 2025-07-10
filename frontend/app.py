# frontend/app.py

import streamlit as st

st.set_page_config(page_title="DeFi Credit Agent", layout="centered")

st.title("DeFi Credit Agent")
st.markdown("Fill in your financial info to check loan eligibility")

# Input fields
income = st.number_input("Monthly Income (INR)", min_value=0)
expenses = st.number_input("Monthly Expenses (INR)", min_value=0)
transactions = st.number_input("Mobile Txn Volume (INR)", min_value=0)

# Submit button
if st.button("Check Credit"):
    st.info("Prediction will appear here after backend integration.")
