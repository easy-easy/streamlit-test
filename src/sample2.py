import streamlit as st
import time

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1)
