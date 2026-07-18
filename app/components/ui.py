from __future__ import annotations

from typing import Any, Dict, Iterable, List

import streamlit as st

from config import get_severity_style

def render_hero(title: str, subtitle: str, badges: Iterable[str]) -> None:
    badge_html = "".join(f'<span class="ll-badge">{badge}</span>' for badge in badges)
    st.markdown(
        f"""
        <div class="ll-hero">
            <div class="ll-kicker">Hospital-grade AI triage experience</div>
            <h1 class="ll-title">{title}</h1>
            <p class="ll-subtitle">{subtitle}</p>
            <div>{badge_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="ll-card">
            <div class="ll-section-title">{title}</div>
            <p class="ll-section-copy">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_metric_row(items: List[Dict[str, Any]]) -> None:
    columns = st.columns(len(items))
    for column, item in zip(columns, items):
        column.metric(item["label"], item["value"], item.get("delta"))

def render_page_header(title: str, description: str) -> None:
    st.markdown(
        f"""
        <div class="ll-card">
            <div class="ll-section-title">{title}</div>
            <p class="ll-section-copy">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_severity_badge(triage_band: str) -> None:
    style = get_severity_style(triage_band)
    st.markdown(
        f"""
        <div class="ll-pill" style="background:{style['color']}22; color:{style['color']}; border:1px solid {style['color']}55;">
            {style['label']}
        </div>
        <p class="ll-section-copy" style="margin-top:0.45rem;">{style['description']}</p>
        """,
        unsafe_allow_html=True,
    )

def render_key_value_block(data: Dict[str, Any]) -> None:
    rows = []
    for key, value in data.items():
        pretty_key = str(key).replace("_", " ").title()
        rows.append(
            f"""
            <div class="ll-mini-card">
                <div style="font-size:0.75rem; color:#8ea4c7; text-transform:uppercase; letter-spacing:0.06em;">{pretty_key}</div>
                <div style="font-size:1rem; color:#eff6ff; font-weight:700; margin-top:0.25rem;">{value}</div>
            </div>
            """
        )
    st.markdown("".join(rows), unsafe_allow_html=True)

def render_probability_list(items: List[Dict[str, Any]]) -> None:
    for item in items:
        probability = float(item["probability"]) * 100
        st.markdown(f"**{item['label']}**: {probability:.0f}%")
        st.progress(min(max(probability / 100, 0.0), 1.0))

def render_bullet_list(title: str, items: List[str]) -> None:
    bullet_html = "".join(f"<li>{item}</li>" for item in items)
    st.markdown(
        f"""
        <div class="ll-card">
            <div class="ll-section-title">{title}</div>
            <ul class="ll-section-copy" style="padding-left:1.1rem; margin:0;">
                {bullet_html}
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_timeline(history_items: List[Dict[str, Any]]) -> None:
    blocks = []
    for item in history_items:
        blocks.append(
            f"""
            <div class="ll-mini-card">
                <div style="display:flex; justify-content:space-between; gap:1rem; align-items:center;">
                    <div style="font-weight:700; color:#eff6ff;">{item['case_id']}</div>
                    <div style="color:#8ea4c7; font-size:0.84rem;">{item['timestamp']}</div>
                </div>
                <div style="margin-top:0.5rem; color:#dce8ff;">{item['finding']}</div>
                <div style="margin-top:0.35rem; color:#a3b3cc; font-size:0.9rem;">
                    Confidence: {float(item['confidence']) * 100:.0f}% • Triage: {item['triage_band']} • Status: {item['status']}
                </div>
            </div>
            """
        )
    st.markdown("".join(blocks), unsafe_allow_html=True)

def render_heatmap_placeholder() -> None:
    st.markdown(
        """
        <div class="ll-card" style="padding:1.4rem;">
            <div class="ll-section-title">Grad-CAM preview area</div>
            <div style="height:260px; border-radius:20px; border:1px solid rgba(128,167,255,0.18);
                        background:
                            radial-gradient(circle at 58% 52%, rgba(255,102,102,0.70), transparent 13%),
                            radial-gradient(circle at 48% 58%, rgba(255,196,84,0.45), transparent 21%),
                            linear-gradient(180deg, rgba(205,221,255,0.16), rgba(205,221,255,0.04));
                        display:flex; align-items:center; justify-content:center; color:#dce8ff;">
                Demo explainability canvas
            </div>
            <p class="ll-section-copy" style="margin-top:0.8rem;">
                This placeholder shows where the Grad-CAM heatmap will appear after backend integration.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )