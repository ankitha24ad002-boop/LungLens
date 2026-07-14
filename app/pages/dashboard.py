from __future__ import annotations

import streamlit as st

from components.backend import get_backend_status, get_dashboard_snapshot, get_prediction_result
from components.ui import render_card, render_key_value_block, render_metric_row, render_page_header
from config import get_app_config, get_page_meta

def render() -> None:
    st.success("Dashboard render() function is being called")
    config = get_app_config()
    page_meta = get_page_meta("dashboard")
    snapshot = get_dashboard_snapshot(config)
    prediction = get_prediction_result(config)
    backend_status = get_backend_status(config)

    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    render_metric_row(
        [
            {"label": "Cases today", "value": snapshot["cases_today"]},
            {"label": "Urgent queue", "value": snapshot["urgent_queue"]},
            {"label": "Reviewed today", "value": snapshot["reviewed_today"]},
            {"label": "Avg latency", "value": f"{snapshot['average_latency_minutes']} min"},
        ]
    )

    left_col, right_col = st.columns([1.25, 1.0], gap="large")

    with left_col:
        st.markdown("")
        render_card(
            "Clinical operations summary",
            (
                f"Current backend state: {backend_status['label']}. {backend_status['detail']} "
                "The dashboard stays fully usable in demo mode for UI development."
            ),
        )
        st.markdown("")
        render_key_value_block(
            {
                "case_id": prediction["case_id"],
                "patient_id": prediction.get("patient_id", "Unknown"),
                "study_type": prediction["study_type"],
                "predicted_finding": prediction["finding"],
                "triage_band": prediction["triage_band"],
            }
        )

    with right_col:
        st.markdown("")
        render_card(
            "Today’s focus",
            (
                "Keep the upload-to-analysis flow short, make warnings impossible to miss, "
                "and preserve a clean clinician-first layout that feels trustworthy."
            ),
        )