from __future__ import annotations

import streamlit as st

from config import AppConfig

def configure_page(config: AppConfig) -> None:
    st.set_page_config(
        page_title=config.page_title,
        page_icon=config.page_icon,
        layout=config.app_layout,
        initial_sidebar_state="expanded",
    )

def apply_theme() -> None:
    st.markdown(
        """
        <style>
            :root {
                --ll-bg-start: #07111f;
                --ll-bg-end: #0a1730;
                --ll-surface: rgba(12, 24, 44, 0.92);
                --ll-surface-soft: rgba(18, 32, 58, 0.72);
                --ll-border: rgba(128, 167, 255, 0.18);
                --ll-text: #eff6ff;
                --ll-muted: #a3b3cc;
                --ll-primary: #6ea8fe;
                --ll-secondary: #8fd3ff;
                --ll-success: #36c78b;
                --ll-warning: #f6c454;
                --ll-danger: #ff7d7d;
                --ll-shadow: 0 20px 50px rgba(0, 0, 0, 0.18);
            }

            .stApp {
                background:
                    radial-gradient(circle at top right, rgba(110, 168, 254, 0.16), transparent 22%),
                    linear-gradient(180deg, var(--ll-bg-start) 0%, var(--ll-bg-end) 100%);
                color: var(--ll-text);
            }

            [data-testid="stSidebar"] {
                background: rgba(5, 12, 24, 0.98);
                border-right: 1px solid var(--ll-border);
            }

            .block-container {
                padding-top: 1.1rem;
                padding-bottom: 2rem;
                max-width: 1280px;
            }

            .ll-card {
                background: var(--ll-surface);
                border: 1px solid var(--ll-border);
                border-radius: 20px;
                padding: 1rem 1.1rem;
                box-shadow: var(--ll-shadow);
                backdrop-filter: blur(10px);
            }

            .ll-hero {
                background:
                    linear-gradient(135deg, rgba(110, 168, 254, 0.22), rgba(54, 199, 139, 0.12)),
                    var(--ll-surface);
                border: 1px solid var(--ll-border);
                border-radius: 24px;
                padding: 1.3rem;
                margin-bottom: 1rem;
            }

            .ll-kicker {
                font-size: 0.76rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                color: var(--ll-primary);
                font-weight: 700;
                margin-bottom: 0.35rem;
            }

            .ll-title {
                font-size: 2rem;
                font-weight: 800;
                line-height: 1.15;
                color: var(--ll-text);
                margin: 0;
            }

            .ll-subtitle {
                color: var(--ll-muted);
                font-size: 0.98rem;
                margin-top: 0.55rem;
                margin-bottom: 0;
            }

            .ll-badge {
                display: inline-block;
                padding: 0.32rem 0.7rem;
                border-radius: 999px;
                border: 1px solid rgba(110, 168, 254, 0.18);
                background: rgba(110, 168, 254, 0.12);
                color: #d9e8ff;
                font-size: 0.8rem;
                font-weight: 600;
                margin-right: 0.45rem;
                margin-top: 0.55rem;
            }

            .ll-section-title {
                font-size: 1rem;
                font-weight: 700;
                color: var(--ll-text);
                margin-bottom: 0.55rem;
            }

            .ll-section-copy {
                color: var(--ll-muted);
                margin-top: 0;
                margin-bottom: 0;
                font-size: 0.94rem;
                line-height: 1.5;
            }

            .ll-pill {
                display: inline-block;
                border-radius: 999px;
                padding: 0.28rem 0.68rem;
                font-size: 0.78rem;
                font-weight: 700;
                margin-top: 0.25rem;
            }

            .ll-mini-card {
                background: var(--ll-surface-soft);
                border: 1px solid var(--ll-border);
                border-radius: 16px;
                padding: 0.85rem 0.95rem;
                margin-bottom: 0.75rem;
            }

            .ll-divider {
                height: 1px;
                background: var(--ll-border);
                margin: 0.9rem 0;
            }

            .ll-footer {
                color: var(--ll-muted);
                text-align: center;
                margin-top: 1rem;
                font-size: 0.85rem;
            }

            .ll-code-note {
                color: var(--ll-secondary);
                font-size: 0.85rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )