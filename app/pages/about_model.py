from __future__ import annotations

import streamlit as st

from components.ui import render_bullet_list, render_card, render_page_header
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("about_model")

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    left_col, right_col = st.columns([1.0, 1.0], gap="large")

    with left_col:
        render_card(
            "Model summary",
            (
                "LungLens is designed as a chest X-ray triage assistant. "
                "The Streamlit frontend stays separate from training and inference code so your teammates can evolve the model safely."
            ),
        )
        st.markdown("")
        render_card("Clinical disclaimer", config.disclaimer)

    with right_col:
        render_bullet_list(
            "What clinicians should know",
            [
                "Predictions are probabilistic outputs, not final diagnoses.",
                "Explainability maps are supportive visual cues, not proof.",
                "Human review remains necessary before clinical action.",
                "Performance depends on data quality and deployment context.",
            ],
        )