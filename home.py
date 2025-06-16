import streamlit as st
from streamlit.source_util import page_icon_and_name
from Account import Account
#from savings_account import SavingsAccount
#from current_account import CurrentAccount

st.set_page_config(page_title = "VinPress Official",layout= "centered",page_icon=":bank:",initial_sidebar_state="collapsed")


total_balance = 15234.56
total_transactions_this_month = 75
new_users_today = 100


user_profile_data = {
    "name": "Trevor Daniel",
    "email": "trevor@gmail.com",
    "phone_number": "+1 (555) 123-4567",
    "address": "123 Main St, Anytown, USA",
}

#Title
st.title(f"💰!Welcome back to VinPress Bank!, {user_profile_data['name']} 👋!")



#a seperator
st.markdown("---")

st.subheader("Your Financial Journey, Simplified. 🚀")
st.write("Where Security Meets Simplicity!")
st.write("Manage your money, track your spending, and achieve your financial goals with ease.")

st.markdown("---") # Separator
st.subheader("Your Personal Details 👤")

# custom div
st.markdown('<div class="profile-section">', unsafe_allow_html=True)

st.markdown(f"<p class='profile-detail'><strong>Name:</strong> {user_profile_data['name']}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='profile-detail'><strong>Email:</strong> {user_profile_data['email']}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='profile-detail'><strong>Phone:</strong> {user_profile_data['phone_number']}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='profile-detail'><strong>Address:</strong> {user_profile_data['address']}</p>", unsafe_allow_html=True)

# button
if st.button("Edit Profile Information"):
    st.info("Edit functionality coming soon! (This is where you'd typically navigate to an edit form.)")

st.markdown('</div>', unsafe_allow_html=True)



# --- Financial Overview Metrics ---
st.markdown("---") # Separator
st.subheader("Your Financial Snapshot 📊")
st.write("Here's a quick overview of your banking activity and profile.")


#For space
st.markdown("##")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Balance", value=f"${total_balance:,.2f}", delta="Access your funds instantly!")
    st.markdown("<p style='font-size: smaller; color: gray;'>Across all your accounts.</p>", unsafe_allow_html=True)


with col2:
    st.metric(label="Transactions This Month", value=str(total_transactions_this_month), delta="Stay on top of your spending!")
    st.markdown("<p style='font-size: smaller; color: gray;'>See your recent activity.</p>", unsafe_allow_html=True)


with col3:
    st.metric(label="New Members Today", value=str(new_users_today), delta="Join our growing community!", delta_color="normal")
    st.markdown("<p style='font-size: smaller; color: gray;'>Welcome aboard!</p>", unsafe_allow_html=True)


st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Thank you for banking with us! ✨</p>", unsafe_allow_html=True)
