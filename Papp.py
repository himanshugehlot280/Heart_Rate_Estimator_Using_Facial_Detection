# import streamlit as st
# import firebase_admin
# from firebase_admin import firestore
# from streamlit_option_menu import option_menu
# from firebase_admin import credentials
# from firebase_admin import auth
# import estimator
# import re
# import Home
#
# if not firebase_admin._apps:
#     cred = credentials.Certificate('logindetails-bf6d4-f6727cbcbf84.json')
#     default_app = firebase_admin.initialize_app(cred)
#
#
# st.title(' Welcome to BPM estimator ')
# choice = st.selectbox('Login/Signup', ['Login','Signup'])
#
# def f():
#     try:
#         user = auth.get_user_by_email(email)
#         #st.session_state.username = user.uid
#         #st.session_state.useremail = user.email
#         st.success('Login Successfully')
#         st.balloons()
#         Home.home()
#         #st.session_state.signedout = True
#         #st.session_state.signout = True
#     except:
#         st.warning('Login Failed')
#
#
# if choice == 'Login':
#     email = st.text_input('Enter your Email')
#     password = st.text_input('Enter your Password')
#     st.button('Login',on_click=f)
# else:
#     email = st.text_input('Enter your Email',key='email_input')
#     password = st.text_input('Enter your Password', type='password',key='password_input')
#     username = st.text_input('Enter Unique username',key='username_input')
#     if st.button('Create my Account'):
#         if email and password and username:
#             if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#                 st.error('Invalid email address')
#             else:
#                 user = auth.create_user(email = email, password = password ,uid=username)
#                 st.success('Account Created Successfully')
#                 st.markdown('Please Login using Email and Password')
#             st.balloons()
#
