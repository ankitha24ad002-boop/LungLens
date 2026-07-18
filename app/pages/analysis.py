from __future__ import annotations

import streamlit as st

from components.backend import get_prediction_result
from components.ui import (
    render_card,
    render_key_value_block,
    render_page_header,
    render_probability_list,
    render_severity_badge,
)
from config import get_app_config, get_page_meta

def render() -> None:
    config = get_app_config()
    page_meta = get_page_meta("analysis")
    prediction = get_prediction_result(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    top_left, top_right = st.columns([1.1, 1.0], gap="large")

    with top_left:
        render_key_value_block(
            {
                "case_id": prediction["case_id"],
                "patient_id": prediction.get("patient_id", "Unknown"),
                "finding": prediction["finding"],
                "confidence": f"{prediction['confidence']:.0%}",
                "uploaded_study": prediction.get("uploaded_name", "Demo study"),
            }
        )

    with top_right:
        render_card("Triage band", prediction["triage_band"])
        render_severity_badge(prediction["triage_band"])

    st.markdown("")
    lower_left, lower_right = st.columns([1.1, 1.0], gap="large")

    with lower_left:
        render_card("Clinical summary", prediction["clinical_summary"])

    with lower_right:
        render_card("Recommended action", prediction["recommended_action"])

    st.markdown("")
    st.markdown("### Differential probabilities")
    render_probability_list(prediction["top_differentials"])