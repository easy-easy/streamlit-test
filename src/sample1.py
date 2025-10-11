import pandas as pd
import streamlit as st

st.title("ファイル読み込み")

uploaded_file = st.file_uploader("ファイルをアップロードしてください")

if uploaded_file is not None:
    # ファイルがアップロードされた場合の処理
    df = pd.read_csv(uploaded_file)
    st.write(df)
