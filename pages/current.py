import streamlit as st

from current_account import CurrentAccount

current = CurrentAccount
st.title("Current..")

with st.form("Current Account Form"):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox("Deposit or withdrawal", ("Deposit", "withdrawal"))
    submit = st.form_submit_button("Submit")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Thank you for banking with us! ✨</p>", unsafe_allow_html=True)


