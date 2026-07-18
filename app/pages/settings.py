from __future__ import annotations

import streamlit as st

from components.backend import get_backend_status, get_runtime_config
from components.ui import render_card, render_page_header
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("settings")
    runtime = get_runtime_config(config)
    backend_status = get_backend_status(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    with st.form("settings_form"):
        backend_base_url = st.text_input("Backend base URL", value=runtime["backend_base_url"])
        demo_mode = st.checkbox("Use demo mode", value=runtime["demo_mode"])
        submitted = st.form_submit_button("Save settings", use_container_width=True)

        if submitted:
            st.session_state["backend_base_url"] = backend_base_url.strip() or config.backend_base_url
            st.session_state["demo_mode"] = demo_mode
            st.success("Runtime settings updated for this session.")

    st.markdown("")
    left_col, right_col = st.columns([1.0, 1.0], gap="large")

    with left_col:
        render_card(
            "Current backend status",
            f"{backend_status['label']} • {backend_status['detail']}",
        )

    with right_col:
        render_card(
            "Deployment note",
            (
                "This Streamlit frontend is cloud-ready. Set `LUNGLENS_BACKEND_URL` in your deployment environment "
                "to connect FastAPI later without changing page code."
            ),
        )