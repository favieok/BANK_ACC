import streamlit as st

from savings_account import SavingsAccount

savings = SavingsAccount(200000)
st.title("Savings..")


with st.form("Savings Account Form"):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox("Deposit or withdrawal",("Deposit","withdrawal"))
    submit = st.form_submit_button("")



if submit and operations == "withdrawal":
    with st.spinner("Processing..."):
        savings.withdraw(amount)
        print(savings.balance)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Thank you for banking with us! ✨</p>", unsafe_allow_html=True)
