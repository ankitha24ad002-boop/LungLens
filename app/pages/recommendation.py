from __future__ import annotations

import streamlit as st

from components.backend import get_recommendation_result
from components.ui import render_bullet_list, render_card, render_page_header, render_severity_badge
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("recommendation")
    recommendation = get_recommendation_result(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    left_col, right_col = st.columns([1.0, 1.05], gap="large")

    with left_col:
        render_card("Risk level", recommendation["risk_level"])
        render_severity_badge(recommendation["triage_band"])

    with right_col:
        render_card("Primary recommendation", recommendation["recommended_action"])

    st.markdown("")
    render_bullet_list("Suggested next steps", recommendation["items"])