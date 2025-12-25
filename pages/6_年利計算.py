import pandas as pd
import streamlit as st

from src.sample1 import calc_interest, calc_interest_with_payment, render

first_container = st.container(border=True)

with first_container:
    render()

second_container = st.container()

with second_container:
    initial_balance = st.number_input("初期資産", value=5000, step=1000)
    arp = st.number_input("年利", value=5)
    years = st.number_input("年数", value=20, step=5)
    annual_payment = st.number_input("年間支払い金額", value=200, step=100)
    total_payment_arp = st.number_input("総支払い金額の年利率", value=0.1)

    st.session_state.annual_balance = calc_interest_with_payment(
        initial_balance, arp, years, annual_payment, total_payment_arp
    )

    st.text("年利計算")

    # ファイルがアップロードされた場合の処理
    df = pd.DataFrame(st.session_state.annual_balance).style.format("{:.2f}")
    # st.dataframe(df)
    st.dataframe(df, height=40 * years)
    # st.table(df)
