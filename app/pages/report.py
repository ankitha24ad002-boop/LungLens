from __future__ import annotations

import streamlit as st

from components.backend import build_report_text
from components.ui import render_card, render_page_header
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("report")
    report_text = build_report_text(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    render_card(
        "Report usage",
        (
            "This export is meant for review, discussion, and documentation support. "
            "It should stay concise, readable, and safe for clinical workflows."
        ),
    )
    st.markdown("")
    st.text_area("Generated report preview", value=report_text, height=360)
    st.download_button(
        "Download case report",
        data=report_text,
        file_name="lunglens_case_report.txt",
        mime="text/plain",
        use_container_width=True,
    )