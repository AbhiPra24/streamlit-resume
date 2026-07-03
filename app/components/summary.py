"""Summary section — three glassmorphism cards."""
import streamlit as st
from app.utils.helpers import section_header, _md_bold


def render_summary(data: dict) -> None:
    section_header("fas fa-list-alt", "Summary")
    bullets = data.get("summary", [])
    cols = st.columns(len(bullets))
    icons = ["fas fa-bolt", "fas fa-robot", "fas fa-rocket"]
    for col, bullet, icon in zip(cols, bullets, icons):
        with col:
            st.markdown(
                f"""
                <div class="summary-card scroll-reveal">
                    <div style="font-size:1.8rem; margin-bottom:10px; color:var(--accent-cyan);"><i class="{icon}"></i></div>
                    <p>{_md_bold(bullet)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
