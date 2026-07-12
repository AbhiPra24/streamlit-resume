"""'Now' section — what he's currently focused on, updated periodically."""
import streamlit as st
from app.utils.helpers import section_header, render_bullet_list


def render_now(data: dict) -> None:
    now = data.get("now")
    if not now:
        return

    section_header("fas fa-satellite-dish", "Now")
    bullets_html = render_bullet_list(now.get("items", []))
    st.markdown(
        f"""
        <div class="now-card scroll-reveal">
            <div class="now-updated"><i class="fas fa-clock"></i> &nbsp;Updated {now.get('updated', '')}</div>
            {bullets_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
