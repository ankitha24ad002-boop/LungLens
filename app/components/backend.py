from __future__ import annotations

import json
from typing import Any, Dict, List, Optional
from urllib import error, parse, request

import streamlit as st

from config import (
    AppConfig,
    get_default_runtime_settings,
    get_mock_dashboard,
    get_mock_heatmap_insights,
    get_mock_history,
    get_mock_prediction,
    get_mock_recommendations,
)

def initialize_runtime_state(config: AppConfig) -> None:
    if "runtime_settings" not in st.session_state:
        st.session_state["runtime_settings"] = get_default_runtime_settings()

    if "backend_base_url" not in st.session_state:
        st.session_state["backend_base_url"] = config.backend_base_url

    if "demo_mode" not in st.session_state:
        st.session_state["demo_mode"] = config.demo_mode

    if "uploaded_case" not in st.session_state:
        st.session_state["uploaded_case"] = None

def get_runtime_config(config: AppConfig) -> Dict[str, Any]:
    initialize_runtime_state(config)
    return {
        "backend_base_url": st.session_state.get("backend_base_url", config.backend_base_url),
        "demo_mode": st.session_state.get("demo_mode", config.demo_mode),
        "request_timeout_seconds": config.request_timeout_seconds,
        "environment": config.environment,
        "deployment_target": config.deployment_target,
    }

def build_api_url(base_url: str, path: str) -> str:
    sanitized_base = base_url.rstrip("/") + "/"
    sanitized_path = path.lstrip("/")
    return parse.urljoin(sanitized_base, sanitized_path)

def get_backend_status(config: AppConfig) -> Dict[str, str]:
    runtime = get_runtime_config(config)

    if runtime["demo_mode"]:
        return {
            "label": "Demo mode",
            "state": "warning",
            "detail": "Mock responses are active until the FastAPI backend is connected.",
        }

    health_url = build_api_url(runtime["backend_base_url"], "/health")

    try:
        response = request.urlopen(
            request.Request(health_url, method="GET"),
            timeout=runtime["request_timeout_seconds"],
        )
        payload = json.loads(response.read().decode("utf-8") or "{}")
        backend_state = str(payload.get("status", "ok")).lower()
        return {
            "label": "Connected",
            "state": "success" if backend_state in {"ok", "healthy", "ready"} else "warning",
            "detail": f"Backend health endpoint responded from {runtime['backend_base_url']}.",
        }
    except (error.URLError, error.HTTPError, TimeoutError, ValueError):
        return {
            "label": "Unavailable",
            "state": "error",
            "detail": (
                "Backend could not be reached. The frontend is still usable in demo mode "
                "once you enable it from Settings."
            ),
        }

def save_uploaded_case(
    patient_id: str,
    age: Optional[int],
    sex: str,
    study_type: str,
    symptoms: str,
    uploaded_name: Optional[str],
) -> None:
    st.session_state["uploaded_case"] = {
        "patient_id": patient_id or "Unknown",
        "patient_age": age or 0,
        "patient_sex": sex or "Unknown",
        "study_type": study_type or "Chest X-ray",
        "symptoms": symptoms or "Not provided",
        "uploaded_name": uploaded_name or "No file selected",
    }

def get_prediction_result(config: AppConfig) -> Dict[str, Any]:
    prediction = get_mock_prediction()
    uploaded_case = st.session_state.get("uploaded_case")

    if uploaded_case:
        prediction["patient_id"] = uploaded_case["patient_id"]
        prediction["patient_age"] = uploaded_case["patient_age"]
        prediction["patient_sex"] = uploaded_case["patient_sex"]
        prediction["study_type"] = uploaded_case["study_type"]
        prediction["uploaded_name"] = uploaded_case["uploaded_name"]
        prediction["clinical_summary"] = (
            f"Latest uploaded study: {uploaded_case['uploaded_name']}. "
            f"Symptoms noted: {uploaded_case['symptoms']}. "
            + prediction["clinical_summary"]
        )
    else:
        prediction["uploaded_name"] = "Demo study"

    return prediction

def get_dashboard_snapshot(config: AppConfig) -> Dict[str, Any]:
    snapshot = get_mock_dashboard()
    backend_status = get_backend_status(config)
    snapshot["backend_label"] = backend_status["label"]
    snapshot["demo_mode"] = "On" if get_runtime_config(config)["demo_mode"] else "Off"
    return snapshot

def get_explainability_result(config: AppConfig) -> Dict[str, Any]:
    prediction = get_prediction_result(config)
    return {
        "case_id": prediction["case_id"],
        "finding": prediction["finding"],
        "confidence": prediction["confidence"],
        "heatmap_available": prediction["heatmap_available"],
        "insights": get_mock_heatmap_insights(),
        "note": (
            "Grad-CAM is shown as a structured placeholder in demo mode. "
            "Connect `src/models/explain.py` through the backend later."
        ),
    }

def get_recommendation_result(config: AppConfig) -> Dict[str, Any]:
    prediction = get_prediction_result(config)
    return {
        "triage_band": prediction["triage_band"],
        "risk_level": prediction["risk_level"],
        "recommended_action": prediction["recommended_action"],
        "items": get_mock_recommendations(),
    }

def get_case_history(config: AppConfig) -> List[Dict[str, Any]]:
    history = get_mock_history()
    uploaded_case = st.session_state.get("uploaded_case")

    if uploaded_case:
        history = [
            {
                "case_id": "LIVE-UPLOAD",
                "timestamp": "Current session",
                "finding": "Pending or demo prediction",
                "confidence": 0.91,
                "triage_band": "Urgent",
                "status": f"Uploaded file: {uploaded_case['uploaded_name']}",
            }
        ] + history

    return history

def build_report_text(config: AppConfig) -> str:
    prediction = get_prediction_result(config)
    backend_status = get_backend_status(config)
    recommendations = get_recommendation_result(config)["items"]

    recommendation_lines = "\n".join(f"- {item}" for item in recommendations)
    return f"""LungLens Case Report

Case ID: {prediction['case_id']}
Patient ID: {prediction.get('patient_id', 'Unknown')}
Age: {prediction['patient_age']}
Sex: {prediction['patient_sex']}
Study Type: {prediction['study_type']}
Uploaded Study: {prediction.get('uploaded_name', 'Demo study')}

Predicted Finding: {prediction['finding']}
Confidence: {prediction['confidence']:.0%}
Triage Band: {prediction['triage_band']}
Risk Level: {prediction['risk_level']}

Clinical Summary:
{prediction['clinical_summary']}

Primary Recommendation:
{prediction['recommended_action']}

Suggested Next Steps:
{recommendation_lines}

Backend Status:
{backend_status['label']} - {backend_status['detail']}

Clinical Safety Note:
{config.disclaimer}
"""