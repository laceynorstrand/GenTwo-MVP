import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="GenTwo", layout="wide")

html_file = next(Path(__file__).parent.glob("*.html"), None)

if html_file is None:
    st.error("No HTML file found in the repo.")
else:
    html = html_file.read_text(encoding="utf-8")
    components.html(html, height=900, scrolling=True)
