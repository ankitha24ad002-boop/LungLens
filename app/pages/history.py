from __future__ import annotations

import streamlit as st

from components.backend import get_case_history
from components.ui import render_page_header, render_timeline
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("history")
    history_items = get_case_history(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")
    render_timeline(history_items)