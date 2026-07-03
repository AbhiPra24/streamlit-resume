"""Education section."""
import streamlit as st
from app.utils.helpers import section_header


def render_education(data: dict) -> None:
    section_header("🎓", "Education")
    for edu in data.get("education", []):
        st.markdown(
            f"""
            <div class="edu-card">
                <div class="edu-icon">{edu['icon']}</div>
                <div>
                    <div class="edu-degree">{edu['degree']}</div>
                    <div class="edu-institution">{edu['institution']}</div>
                    <div class="edu-duration">📅 {edu['duration']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
