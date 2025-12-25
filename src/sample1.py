import pandas as pd
import streamlit as st


def render():
    st.title("ファイル読み込み")

    uploaded_file = st.file_uploader("ファイルをアップロードしてください")

    if uploaded_file is not None:
        # ファイルがアップロードされた場合の処理
        df = pd.read_csv(uploaded_file)
        st.write(df)


def calc_interest(init_value, arp, years):
    """年利計算

    Args:
        init_value: 初期資産
        arp: 年利率 (%)
        years: 年数

    Returns:
        年ごとの資産額のリスト
    """
    annual_balances = [init_value * (1 + arp / 100) ** i for i in range(years + 1)]

    # # another logic
    # annual_balances = [init_value]
    # for i in range(years):
    #     curr = annual_balances[-1]
    #     next_balance = curr * (1 + arp/100)
    #     annual_balances.append(next_balance)
    return annual_balances


def calc_interest_with_payment(init_value: int, arp: int, years: int, annual_payment: int, total_payment_arp: int):
    """年利計算

    Args:
        init_value: 初期資産
        arp: 年利率 (%)
        years: 年数
        annual_payment: 年間支払い金額
        total_payment_arp: 総支払い金額の年利率 (%)

    Returns:
        年ごとの資産額のリスト
    """
    # annual_balances = [init_value * (1 + arp/100) ** i - annual_payment for i in range(years + 1)]

    # # another logic
    annual_balances = [init_value - annual_payment]
    for i in range(years):
        curr = annual_balances[-1]
        next_balance = (
            curr * (1 + arp / 100)
            - annual_payment
            - ((init_value - annual_payment * (i + 1)) * total_payment_arp / 100)
        )
        annual_balances.append(next_balance)
    return annual_balances
