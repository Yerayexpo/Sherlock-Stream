import streamlit as st
import streamlit.components.v1 as components
import subprocess
import sys


st.set_page_config(page_title='Sherlock 🔎', page_icon = 'https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png')
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.title('Sherlock Username Search')

st.image('https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/134b5b0f-9577-4f34-994a-d0243c9d1a3a/Leonardo_Diffusion_XL_A_chaotic_and_cluttered_office_filled_wi_1.jpg')

username = st.text_input('Username', value='', help='Enter the username you want to track')
col1, col2, col3 = st.columns([1, 2, 4])
with col1:
    if st.button('Submit'):
        st.text('Searching for \''+username+'\'... (this might take a minute)')
        python_executable = sys.executable
        try:
            s = subprocess.check_output([python_executable, "sherlock", username])
            st.text(s.decode("utf-8"))
        except subprocess.CalledProcessError as e:
            st.error(f"Error occurred: {e}")
with col3:
    st.markdown("Repository of the project: [Yerayexpo/Sherlock-Stream](https://github.com/Yerayexpo/Sherlock-Stream)")
