import streamlit as st
import firebase_admin
from firebase_admin import firestore
from streamlit_option_menu import option_menu
from firebase_admin import credentials
from firebase_admin import auth
from validators import email
import estimator
import re
import Home
import streamlit as st
st.markdown('<h1 style="color: red;">Heart Rate Estimator</h1>', unsafe_allow_html=True)
st.write("Welcome to the Heart Rate Estimator web app, where cutting-edge technology meets health monitoring in real time. Our innovative platform allows you to track and estimate your heart rate using the latest advancements with Real Time Data.")
# Display a GIF from a local file
local_gif_path = "images/ecg.gif"  # Replace this with the local path to your GIF
st.image(local_gif_path, use_column_width=True)

if not firebase_admin._apps:
    cred = credentials.Certificate('logindetails-bf6d4-f6727cbcbf84.json')
    default_app = firebase_admin.initialize_app(cred)


def f(email, password):
    try:
        user = auth.get_user_by_email(email)
        password = auth.get_user(password)
        st.success('Login Successfully')
        st.balloons()
        st.session_state.logged_in = True
        st.session_state.current_page = "Home"
    except:
        st.error(f"Authentication failed:")



def main():
    page = st.sidebar.selectbox("Select Page", ["Login", "Home", "SignUp"])


    if page == "Login":
        st.title("Login Page")
        # Your login logic goes here
        email = st.text_input('Enter your Email')
        password = st.text_input('Enter your Password')
        if st.button('Login'):
            f(email, password)

    elif page == "Home":
        # Check if the user is logged in
        if "logged_in" not in st.session_state or not st.session_state.logged_in:
            # If not logged in, redirect back to the Login page
            st.warning("Please log in to access the Home page.")
            st.session_state.current_page = "Login"
        else:
            Home.home()
        # --------------------------SIGN UP-----------------------------------------------------------------
    else:
        email = st.text_input('Enter your Email', key='email_input')
        password = st.text_input('Enter your Password', type='password', key='username_input')
        # username = st.text_input('Enter Unique username',key='username_input')
        if st.button('Create my Account'):
            if email and password:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error('Invalid email address')
                else:
                    user = auth.create_user(email=email, uid=password)
                    st.success('Account Created Successfully')
                    st.markdown('Please Login using Email and Password')
                    st.balloons()


if __name__ == "__main__":
    main()
