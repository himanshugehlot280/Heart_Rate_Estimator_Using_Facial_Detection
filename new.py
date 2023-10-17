
import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

if not firebase_admin._apps:
    cred = credentials.Certificate('C:\PulseEstimator\logindetails-bf6d4-48c3ec4795b7.json')
    default_app = firebase_admin.initialize_app(cred)



st.title(' Welcome to BPM estimator ')
choice = st.selectbox('Login/Signup', ['Login','Signup'])


def f():
    try:
        user = auth.get_user_by_email(email)
        #print(user.uid)
    except:
        st.warning('Login Failed')

if choice == 'Login':
    email = st.text_input('Enter your Email')
    password = st.text_input('Enter your Password',type='password')
    st.button('Login')
else:
    email = st.text_input('Enter your Email')
    password = st.text_input('Enter your Password', type='password')
    username = st.text_input('Enter Unique username')
    if st.button('Create my Account'):
        user = auth.create_user(email = email, password = password,uid=username)
        st.success('Account Created Successfully')
        st.markdown('Please Login using Email and Password')
        st.balloons()

