from __future__ import annotations

import streamlit as st

from components.backend import get_explainability_result
from components.ui import render_card, render_heatmap_placeholder, render_page_header
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("explainability")
    explainability = get_explainability_result(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    left_col, right_col = st.columns([1.15, 1.0], gap="large")

    with left_col:
        render_heatmap_placeholder()

    with right_col:
        render_card(
            "Explainability note",
            (
                f"Finding: {explainability['finding']} • Confidence: {explainability['confidence']:.0%}. "
                + explainability["note"]
            ),
        )
        st.markdown("")
        st.markdown("### Model attention notes")
        for item in explainability["insights"]:
            render_card(
                f"{item['region']} • {item['importance']}",
                item["note"],
            )

    st.info("Grad-CAM should be shown as supportive evidence for clinicians, not as the final diagnosis.")