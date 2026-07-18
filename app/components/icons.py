from __future__ import annotations

from typing import Dict

ICON_MAP: Dict[str, str] = {
    "dashboard": "📊",
    "upload": "📤",
    "analysis": "🧪",
    "explainability": "🧭",
    "recommendation": "🩺",
    "report": "📝",
    "history": "🕘",
    "about_model": "🤖",
    "settings": "⚙️",
    "backend": "🔗",
    "status_ok": "🟢",
    "status_warn": "🟡",
    "status_error": "🔴",
    "patient": "🧑",
    "scan": "🫁",
}

def get_icon(name: str) -> str:
    return ICON_MAP.get(name, "•")

def page_label(label: str, module_name: str) -> str:
    return f"{get_icon(module_name)} {label}"