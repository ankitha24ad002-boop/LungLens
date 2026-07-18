from __future__ import annotations

import importlib
from typing import Callable, Optional

import streamlit as st

from components.backend import (
    get_backend_status,
    get_prediction_result,
    initialize_runtime_state,
)
from components.icons import page_label
from components.ui import render_hero, render_metric_row
from config import (
    AppConfig,
    get_app_config,
    get_navigation_items,
    get_page_meta,
)
from theme import apply_theme, configure_page


def load_page_renderer(module_name: str) -> Optional[Callable[[], None]]:
    try:
        module = importlib.import_module(f"pages.{module_name}")
        render_fn = getattr(module, "render", None)
        if callable(render_fn):
            return render_fn
    except Exception as exc:
        st.error(f"Unable to load page `{module_name}`. Error: {exc}")
        return None
    return None


def render_sidebar(config: AppConfig) -> str:
    navigation_items = get_navigation_items()
    labels = [item["label"] for item in navigation_items]
    modules = {item["label"]: item["module"] for item in navigation_items}

    with st.sidebar:
        st.markdown("## LungLens")
        st.caption("Frontend UI + Explainability")
        st.markdown(
            """
            <div class="ll-card">
                <div class="ll-section-title">Navigation</div>
                <p class="ll-section-copy">
                    Use the sidebar to move through the full clinician workflow.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("")

        selected_label = st.radio(
            "Pages",
            labels,
            format_func=lambda label: page_label(label, modules[label]),
            label_visibility="collapsed",
        )

        st.markdown("")
        backend_status = get_backend_status(config)
        st.metric("Version", config.app_version)
        st.metric(
            "Mode",
            "Demo" if st.session_state.get("demo_mode", config.demo_mode) else "Live",
        )
        st.caption(f"Backend status: {backend_status['label']}")
        st.caption(
            f"API target: `{st.session_state.get('backend_base_url', config.backend_base_url)}`"
        )

    return modules[selected_label]


def render_shell_metrics(config: AppConfig) -> None:
    prediction = get_prediction_result(config)
    backend_status = get_backend_status(config)

    render_metric_row(
        [
            {"label": "Case ID", "value": prediction["case_id"]},
            {"label": "Study", "value": prediction["study_type"]},
            {"label": "Finding", "value": prediction["finding"]},
            {"label": "Backend", "value": backend_status["label"]},
        ]
    )


def main() -> None:
    config = get_app_config()

    configure_page(config)
    apply_theme()
    initialize_runtime_state(config)

    active_module = render_sidebar(config)
    page_meta = get_page_meta(active_module)

    render_hero(
        title=config.app_name,
        subtitle=config.app_tagline,
        badges=[
            f"Page: {page_meta['title']}",
            f"Target: {config.deployment_target.title()}",
            "Streamlit frontend",
        ],
    )

    render_shell_metrics(config)
    st.markdown("")

    page_renderer = load_page_renderer(active_module)

    if page_renderer is not None:
        page_renderer()
    else:
        st.warning(
            "This page could not be loaded. Check the page module import and render function."
        )

    st.markdown(
        f"""
        <div class="ll-footer">
            {config.app_name} v{config.app_version} • Clinical AI frontend • Cloud deployment friendly
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()