import streamlit as st
from tweaker import st_tweaker

# Function to load and apply CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load and apply the CSS file at the start of your app
load_css('src/style.css')

st_tweaker.title("Happy Monthsary, Love!",
                id = 'title')

video_file = open("assets/1203.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st_tweaker.caption("Andrei Palma",
                id='signature')