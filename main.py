import streamlit as st

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="👋",
)

st.title("👋 はじめてのStreamlitアプリ")
st.write("Hello, World!")

st.markdown(
    """
    このアプリには複数のデモページがあります。
    左側のサイドバーからページを選択してください:
    
    - **DataFrame Demo**: データフレームとチャートの表示
    - **Plotting Demo**: リアルタイムプロット
    - **Mapping Demo**: 地理空間データの可視化
    - **Animation Demo**: フラクタルアニメーション
    """
)


def on_button_click():
    st.sidebar.success("ボタンがクリックされました！")
    st.balloons()


st.sidebar.header("Sidebar Header")
st.sidebar.title("サイドバー タイトル")
st.sidebar.write("This is the sidebar.")
st.sidebar.button("サイドバー ボタン", on_click=on_button_click)
st.sidebar.radio("ラジオボタン", ("オプション 1", "オプション 2", "オプション 3"))
st.sidebar.checkbox("チェックボックス")
st.sidebar.selectbox("セレクトボックス", ("オプション A", "オプション B", "オプション C"))
st.sidebar.multiselect("マルチセレクト", ("選択肢 X", "選択肢 Y", "選択肢 Z"))
st.sidebar.slider("年齢を選択", 0, 100, 30)
# st.sidebar.slider("スライダー", 0, 100, 50)
st.sidebar.text_input("テキスト入力", "デフォルト テキスト")
st.sidebar.text_area("テキストエリア", "デフォルト テキストエリア")
st.sidebar.date_input("日付入力")
st.sidebar.time_input("時間入力")
st.sidebar.file_uploader("ファイルアップローダー")
st.sidebar.color_picker("色選択")

st.radio("ラジオボタン", ("オプション 1", "オプション 2", "オプション 3"))

st.header("Header")
st.subheader("Subheader")
st.caption("これはキャプションです")
st.markdown("Markdown **太字** *イタリック* [リンク](https://streamlit.io)")
st.latex(r"E=mc^2")
st.code("print('Hello, Streamlit!')", language="python")


st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

name = st.text_input("Your name", "Type here")
age = st.slider("Your age", 0, 130, 25)
if name:
    st.write(f"{name}さん、{age}歳ですね！")
