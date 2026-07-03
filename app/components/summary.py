"""Summary section — three glassmorphism cards."""
import streamlit as st
from app.utils.helpers import section_header, _md_bold


def render_summary(data: dict) -> None:
    section_header("💡", "Summary")
    bullets = data.get("summary", [])
    cols = st.columns(len(bullets))
    icons = ["⚡", "🤖", "🚀"]
    for col, bullet, icon in zip(cols, bullets, icons):
        with col:
            st.markdown(
                f"""
                <div class="summary-card">
                    <div style="font-size:1.8rem; margin-bottom:10px;">{icon}</div>
                    <p>{_md_bold(bullet)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
