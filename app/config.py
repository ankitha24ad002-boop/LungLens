from __future__ import annotations

import os
from dataclasses import asdict, dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class AppConfig:
    app_name: str = "LungLens"
    app_tagline: str = "AI-assisted chest X-ray triage workspace"
    app_version: str = "1.0.0"
    deployment_target: str = os.getenv("LUNGLENS_DEPLOYMENT_TARGET", "cloud")
    environment: str = os.getenv("LUNGLENS_ENV", "production")
    demo_mode: bool = os.getenv("LUNGLENS_DEMO_MODE", "true").lower() == "true"
    backend_base_url: str = os.getenv(
        "LUNGLENS_BACKEND_URL",
        "https://api.lunglens.example.com",
    )
    request_timeout_seconds: int = int(os.getenv("LUNGLENS_REQUEST_TIMEOUT", "20"))
    page_title: str = "LungLens"
    page_icon: str = "🫁"
    app_layout: str = "wide"
    support_email: str = "care@lunglens.ai"
    hospital_name: str = "LungLens Clinical AI Suite"
    disclaimer: str = (
        "This tool supports clinical review and triage prioritization. "
        "It must not be used as the sole basis for diagnosis."
    )


APP_CONFIG = AppConfig()


NAVIGATION_ITEMS: List[Dict[str, str]] = [
    {"label": "Dashboard", "module": "dashboard"},
    {"label": "Upload", "module": "upload"},
    {"label": "Analysis", "module": "analysis"},
    {"label": "Explainability", "module": "explainability"},
    {"label": "Recommendation", "module": "recommendation"},
    {"label": "Report", "module": "report"},
    {"label": "History", "module": "history"},
    {"label": "About Model", "module": "about_model"},
    {"label": "Settings", "module": "settings"},
]


PAGE_METADATA: Dict[str, Dict[str, str]] = {
    "dashboard": {
        "title": "Clinical Dashboard",
        "description": "Live overview of triage flow, backend status, and current case.",
    },
    "upload": {
        "title": "Study Upload",
        "description": "Upload a chest X-ray and capture basic patient metadata.",
    },
    "analysis": {
        "title": "Prediction Analysis",
        "description": "Review finding confidence, differentials, and clinical summary.",
    },
    "explainability": {
        "title": "Explainability",
        "description": "Inspect Grad-CAM highlights and model attention guidance.",
    },
    "recommendation": {
        "title": "Clinical Recommendation",
        "description": "See triage-safe next actions aligned with the model output.",
    },
    "report": {
        "title": "Case Report",
        "description": "Generate a concise case report for discussion and export.",
    },
    "history": {
        "title": "Case History",
        "description": "Track recent cases and review workflow state changes.",
    },
    "about_model": {
        "title": "About the Model",
        "description": "Understand intended use, limits, and operating assumptions.",
    },
    "settings": {
        "title": "Settings",
        "description": "Manage backend endpoint, timeouts, and demo experience.",
    },
}


SEVERITY_STYLES: Dict[str, Dict[str, str]] = {
    "Normal": {
        "label": "Normal",
        "color": "#36c78b",
        "description": "No urgent abnormality suggested in the demo result.",
    },
    "Monitor": {
        "label": "Monitor",
        "color": "#f6c454",
        "description": "Mild concern. Clinical review is recommended.",
    },
    "Urgent": {
        "label": "Urgent",
        "color": "#ff8a4c",
        "description": "Time-sensitive review is advised for this case.",
    },
    "Critical": {
        "label": "Critical",
        "color": "#ff6b6b",
        "description": "Immediate clinical attention is recommended.",
    },
}


MOCK_PREDICTION: Dict[str, Any] = {
    "case_id": "LL-2026-0142",
    "patient_id": "PT-48392",
    "patient_age": 47,
    "patient_sex": "Female",
    "study_type": "PA Chest X-ray",
    "finding": "Pneumonia suspected",
    "confidence": 0.91,
    "triage_band": "Urgent",
    "risk_level": "High",
    "recommended_action": (
        "Prioritize physician review, correlate with symptoms and oxygen saturation, "
        "and confirm using the radiology workflow."
    ),
    "clinical_summary": (
        "Patchy left lower-zone opacity is simulated in the demo output. "
        "The model confidence is high enough to trigger urgent review in triage mode."
    ),
    "heatmap_available": False,
    "top_differentials": [
        {"label": "Pneumonia", "probability": 0.91},
        {"label": "Pleural Effusion", "probability": 0.37},
        {"label": "Normal", "probability": 0.08},
    ],
}


MOCK_HISTORY: List[Dict[str, Any]] = [
    {
        "case_id": "LL-2026-0142",
        "timestamp": "2026-07-14 09:10",
        "finding": "Pneumonia suspected",
        "confidence": 0.91,
        "triage_band": "Urgent",
        "status": "Awaiting radiology review",
    },
    {
        "case_id": "LL-2026-0141",
        "timestamp": "2026-07-14 08:52",
        "finding": "No acute cardiopulmonary abnormality",
        "confidence": 0.87,
        "triage_band": "Normal",
        "status": "Completed",
    },
    {
        "case_id": "LL-2026-0140",
        "timestamp": "2026-07-14 08:25",
        "finding": "Possible pleural effusion",
        "confidence": 0.74,
        "triage_band": "Monitor",
        "status": "Needs clinical correlation",
    },
]


MOCK_DASHBOARD: Dict[str, Any] = {
    "cases_today": 24,
    "urgent_queue": 3,
    "reviewed_today": 18,
    "average_latency_minutes": 2.4,
}


MOCK_HEATMAP_INSIGHTS: List[Dict[str, str]] = [
    {
        "region": "Left lower lung zone",
        "importance": "High",
        "note": "Model focus is strongest around the simulated opacity region.",
    },
    {
        "region": "Perihilar region",
        "importance": "Medium",
        "note": "Secondary attention likely reflects supporting contextual texture.",
    },
    {
        "region": "Cardiomediastinal silhouette",
        "importance": "Low",
        "note": "Low relevance in the current mock Grad-CAM explanation.",
    },
]


MOCK_RECOMMENDATIONS: List[str] = [
    "Escalate this case for clinician review within the urgent queue.",
    "Correlate the result with temperature, oxygen saturation, and symptoms.",
    "Use Grad-CAM as supportive evidence, not as a standalone diagnosis tool.",
    "Confirm the final decision with a radiologist or responsible physician.",
]


DEFAULT_RUNTIME_SETTINGS: Dict[str, Any] = {
    "theme_mode": "dark",
    "show_demo_banner": True,
    "compact_sidebar": False,
}


def get_app_config() -> AppConfig:
    return APP_CONFIG


def get_navigation_items() -> List[Dict[str, str]]:
    return list(NAVIGATION_ITEMS)


def get_page_meta(module_name: str) -> Dict[str, str]:
    return PAGE_METADATA.get(
        module_name,
        {"title": "LungLens", "description": "Clinical AI application page."},
    )


def get_mock_prediction() -> Dict[str, Any]:
    return dict(MOCK_PREDICTION)


def get_mock_history() -> List[Dict[str, Any]]:
    return list(MOCK_HISTORY)


def get_mock_dashboard() -> Dict[str, Any]:
    return dict(MOCK_DASHBOARD)


def get_mock_heatmap_insights() -> List[Dict[str, str]]:
    return list(MOCK_HEATMAP_INSIGHTS)


def get_mock_recommendations() -> List[str]:
    return list(MOCK_RECOMMENDATIONS)


def get_default_runtime_settings() -> Dict[str, Any]:
    return dict(DEFAULT_RUNTIME_SETTINGS)


def get_severity_style(triage_band: str) -> Dict[str, str]:
    return dict(
        SEVERITY_STYLES.get(
            triage_band,
            {
                "label": "Unknown",
                "color": "#6ea8fe",
                "description": "Severity band is not available yet.",
            },
        )
    )


def export_config() -> Dict[str, Any]:
    return asdict(APP_CONFIG)
