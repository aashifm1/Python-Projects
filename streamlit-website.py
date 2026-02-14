
# Install streamlit --> pip install streamlit
import streamlit as st
import re

st.title("Registration Website")
st.write("Powered by Streamlit.")

# Registration form
with st.form("registration_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email", type="default")
    
    password = st.text_input("Enter your password", type="password") 
    # type=password gives usual password properties such as hide and show password icon.

    agree = st.checkbox("I agree to Terms and Conditions") # checkbox
    submitted = st.form_submit_button("Register") # submit button

# Email validation
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" # email format
    return re.match(pattern, email)

# Form submission
if submitted:
    # the form will be submitted only after all inputs are filled.
    if not name:
        st.error("Please enter your name.")
    elif not email or not is_valid_email(email):
        st.error("Please enter a valid email address.")
    elif not password or len(password) < 6:
        st.error("Password must be at least 6 characters.")
    elif not agree:
        st.error("You must agree to the Terms and Conditions.")
    else:
        st.success(f"🎉 {name} is registered successfully!")

# To run --> pythom -m streamlit run streamlit-website.py