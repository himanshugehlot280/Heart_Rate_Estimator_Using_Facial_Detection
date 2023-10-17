import streamlit as st
import sys
import Papp
from streamlit_option_menu import option_menu
st.set_page_config(
        page_title="BPM estimator",
)


with st.sidebar:
    app = option_menu(
        menu_title='BPM Estimator',
        options=['Home','Account','Trending','Your Posts','about'],
        icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
        menu_icon = "cast", default_index = 1)


