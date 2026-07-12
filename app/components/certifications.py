"""Certifications section."""
import streamlit as st
from app.utils.helpers import section_header


def render_certifications(data: dict) -> None:
    section_header("fas fa-certificate", "Certifications")
    badges = "".join(
        f'<span class="cert-badge scroll-reveal"><i class="{c["icon"]}"></i> &nbsp;{c["name"]}</span>'
        if "fa-" in c.get("icon", "") else f'<span class="cert-badge scroll-reveal">{c["icon"]} {c["name"]}</span>'
        for c in data.get("certifications", [])
    )
    st.markdown(
        f'<div class="cert-grid">{badges}</div>',
        unsafe_allow_html=True,
    )
