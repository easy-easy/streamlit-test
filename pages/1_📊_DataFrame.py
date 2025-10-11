"""DataFrame Demo Page.

This page demonstrates DataFrame and chart visualization capabilities.
The actual implementation is in lib.dataframe_demo module.
"""

import streamlit as st

from lib.dataframe_demo import render_dataframe_demo

# Page configuration
st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

# Page header
st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write("""This demo shows how to use `st.dataframe` and `st.altair_chart` to display data.""")

# Render the main demo content
render_dataframe_demo()
