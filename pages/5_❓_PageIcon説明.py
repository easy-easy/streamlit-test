"""page_icon の表示位置デモ.

このファイルでは、st.set_page_config() のパラメータがどこに反映されるかを説明します。
"""

import streamlit as st

# ページ設定
st.set_page_config(
    page_title="My Custom Title",  # ← ブラウザのタブに表示されるテキスト
    page_icon="🗺️",  # ← ブラウザのタブに表示されるアイコン（ファビコン）
    layout="wide",  # ← ページレイアウト（"centered" or "wide"）
    initial_sidebar_state="expanded",  # ← サイドバーの初期状態
)

st.title("page_icon の表示位置について")

st.markdown("""
## `st.set_page_config()` パラメータの表示位置

### 1. `page_icon` 🗺️
**表示位置**: ブラウザのタブ（ファビコン）
- Webブラウザの上部にあるタブに小さなアイコンとして表示されます
- 複数のタブを開いているときに、このアイコンでページを識別できます
- 絵文字、URL、またはローカル画像ファイルを指定可能

### 2. `page_title`
**表示位置**: ブラウザのタブのテキスト
- `page_icon` の隣に表示されるテキスト
- 例: "🗺️ My Custom Title"

### 3. `layout`
**表示位置**: ページ全体のレイアウト
- `"centered"`: コンテンツが中央に配置（デフォルト）
- `"wide"`: コンテンツが画面幅いっぱいに配置

### 4. `initial_sidebar_state`
**表示位置**: サイドバーの表示状態
- `"expanded"`: サイドバーが展開された状態で表示（デフォルト）
- `"collapsed"`: サイドバーが折りたたまれた状態で表示
- `"auto"`: 自動判定

---

## 確認方法

1. このページを開いた状態で、**ブラウザのタブ**を見てください
2. タブに **🗺️ アイコン** と **"Mapping Demo"** というテキストが表示されているはずです
3. 他のページに移動すると、タブのアイコンとテキストが変わります

### 各ページのpage_icon:
- ホーム: 👋
- DataFrame Demo: 📊
- Plotting Demo: 📈
- Mapping Demo: 🗺️
- Animation Demo: 🎨
""")

# 実際の表示例
st.subheader("現在のページ設定")
st.code(
    """
st.set_page_config(
    page_title="Mapping Demo",  # ← タブのテキスト
    page_icon="🗺️"             # ← タブのアイコン
)
""",
    language="python",
)

st.info("""
💡 **ポイント**:
- `page_icon` は Streamlit アプリ内には表示されません
- ブラウザのタブでのみ確認できます
- ブックマークに保存した際にも、このアイコンが使用されます
""")

st.warning("""
⚠️ **注意**:
`st.set_page_config()` は**スクリプトの最初**に呼び出す必要があります。
他のStreamlitコマンドの後に呼び出すとエラーになります。
""")
