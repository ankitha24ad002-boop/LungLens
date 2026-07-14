from __future__ import annotations

import streamlit as st

from components.backend import save_uploaded_case
from components.ui import render_card, render_page_header
from config import get_page_meta

def render() -> None:
    page_meta = get_page_meta("upload")
    render_page_header(page_meta["title"], page_meta["description"])
    st.markdown("")

    left_col, right_col = st.columns([1.25, 1.0], gap="large")

    with left_col:
        uploaded_file = st.file_uploader(
            "Upload chest X-ray image",
            type=["png", "jpg", "jpeg"],
            help="Demo UI currently accepts image files while backend integration is pending.",
        )

        patient_id = st.text_input("Patient ID", value="PT-48392")
        age = st.number_input("Age", min_value=0, max_value=120, value=47, step=1)
        sex = st.selectbox("Sex", ["Female", "Male", "Other"], index=0)
        study_type = st.selectbox("Study type", ["PA Chest X-ray", "AP Chest X-ray", "Portable Chest X-ray"], index=0)
        symptoms = st.text_area(
            "Clinical notes",
            value="Fever, productive cough, mild shortness of breath.",
            height=120,
        )

        if st.button("Save upload for demo analysis", type="primary", use_container_width=True):
            save_uploaded_case(
                patient_id=patient_id,
                age=int(age),
                sex=sex,
                study_type=study_type,
                symptoms=symptoms,
                uploaded_name=uploaded_file.name if uploaded_file else None,
            )
            st.success("Upload details saved in session state. Open Analysis to see the demo result.")

    with right_col:
        render_card(
            "Upload guidance",
            (
                "This page is intentionally clinician-friendly: one upload area, a few essential fields, "
                "and a single action button. When your teammate connects FastAPI, the same screen can post the study to the backend."
            ),
        )
        st.markdown("")
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded study preview", use_column_width=True)
        else:
            st.info("No image selected yet. You can still save metadata and test the rest of the flow.")