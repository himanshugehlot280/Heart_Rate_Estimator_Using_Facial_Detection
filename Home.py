import streamlit as st
from streamlit_option_menu import option_menu
import average
import estimator
import demo

def home():
    st.title("Online Heart Rate Estimator")
    selected = st.sidebar.selectbox(
        "Main Menu",
        options=["Home", "Online Heart Rate", "20s CheckUp", "About Us"],
        index=0,  # Set index 0 for 'Home'
        format_func=lambda x: f"{x}",  # Use a lambda function to format the options
    )
    if selected == "Home":
        st.write(f"You have Selected {selected}")
        st.write("### Description")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write(
            "When your heart beats you face changes colour ever-so-slightly because of blood flowing through. Though "
            "this change isn't visible to the naked eye, it can be extracted by a computer program. ")
        st.write(
            "Our application first detects faces and isolates the forehead. it then performs a fast fourier transform. "
            "The amount of colour change occurring at 50bpm is on the left ranging to the amount of colour changes "
            "happening at 200bpm on the right. The rate of colour change which appears most significant is assumed to be "
            "the heart beat. ")
        st.write("As you can see, the programs requires you to be very still and is annoyingly lighting dependant but "
                 "otherwise works.")
        # Define custom HTML and CSS for the colored box
        custom_style = """
        <style>
            .colored-box {
                background-color: #3498db; /* Specify the background color you want */
                border-radius: 10px; /* Adjust the border radius as needed */
                padding: 20px; /* Adjust the padding as needed */
                margin: 10px 0; /* Adjust the margin as needed */
            }
        </style>
        """
        # Apply the custom style to the app
        st.markdown(custom_style, unsafe_allow_html=True)
        # Create the colored box using a <div> element
        st.markdown('<div class="colored-box">PRE-REQUISITE </div>', unsafe_allow_html=True)
        st.markdown("""
        - Stable Camera. Minimum 14 pixel required 
        - Proper Lighting Condition. Note: Fluctuation of light cause change in Heart Rate 
        """)
        # Add content below the box
        st.write("")
        image_path_1 = "images/second.jpg"
        st.image(image_path_1, caption="Image", use_column_width=True)
        st.write("### Heart Explained")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write(
            "The functions of the heart are to pump blood and oxygen around the body and deliver waste products carbon "
            "dioxide back to the lungs to be removed.")
        st.write("The heart consists of four chambers, each separated by valves which direct the flow of blood.")
        st.write("Conditions affecting the heart include coronary heart disease, angina, heart attack, heart failure, "
                 "heart valve diseases, abnormal heart rhythms including atrial fibrillation, heart inflammation, congenital "
                 "heart disease (present from birth) and rheumatic heart disease.")
        image_path_2 = "images/third.jpg"
        st.image(image_path_2, caption="Image", use_column_width=True)
        st.write("### Heart Rate")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        - The heart rate is one of the ‘vital signs,’ or the important indicators of health in the human body.
        - The heart rate is the number of times the heart beats in the space of a minute.
        - The speed of the heartbeat varies as a result of physical activity, threats to safety, and emotional responses.
        """)
        st.write("#### Healthy Heart Rate for Mens and Women's")
        image_path_3 = "images/fifth.png"
        st.image(image_path_3, caption="Image", use_column_width=True)
    if selected == "Online Heart Rate":
        st.write(f"You have Selected {selected}")
        estimator.main()
    if selected == "20s CheckUp":
        st.write(f"You have Selected {selected}")
        st.title("Coming Soon...........")
        st.title("Future Enhancement")
    if selected == "About Us":
        st.write(f"You have Selected {selected}")
        demo.main()


if __name__ == "__main__":
    home()
