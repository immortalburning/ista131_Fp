import streamlit as st
import requests
from streamlit_lottie import st_lottie


class Introduction:
    def __init__(self):
        pass

    def app(self):
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_anim1 = load_lottieurl("https://lottie.host/ef0d69e7-85c3-41d5-9def-d76e9d129876/f6hH1U5edi.json")

        # Create two columns
        text, spacer, video = st.columns([2,0.5,1])

        # Left column for text content
        with text:
            st.title('Introduction to the project')
            st.write("---")
            st.write("""
                     This project is aimed at expanding our understanding in dataframe analysis.
                     For this module, our group of three have created different visualizations through the use of
                     libraries that have been explored during ISTA 131 course, such as:

                     - Pandas
                     - Matplotlib
                     - Numpy

                     As well as auxiliary required libraries:

                     - Streamlit
                     """
                     )
            st.write("---")
            st.subheader("Used environment")
            st.write("""
                     In order to offer the easier perception of our visualizations, we've
                     decided to use the streamlit framework, which allowed us to organize
                     our work through the use of several pages, one for every member of
                     our team. 
                     """)
            st.write("---")
            st.subheader("Repository information")
            st.write("""
                        If you wish to review the structure of the content as well as
                        check the sequence of our git actions, you can visit our github
                        repository at: 
                        """)
            st.write("[Github link >](https://github.com/ligushka789/ista131_Fp)")

        # Right column for video and animation
        with video:
            video_file = open('video/video.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

        st_lottie(lottie_anim1, height=300, key="coding")

        # Add styling
        st.markdown(
            """
            <style>
            h1 {
                color: #4CAF50;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
