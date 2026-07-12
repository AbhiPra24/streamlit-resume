"""Education section."""
import streamlit as st
from app.utils.helpers import section_header


def render_education(data: dict) -> None:
    section_header("fas fa-graduation-cap", "Education")
    for edu in data.get("education", []):
        icon_html = f'<i class="{edu["icon"]}"></i>' if "fa-" in edu["icon"] else edu["icon"]
        st.markdown(
            f"""
            <div class="edu-card scroll-reveal">
                <div class="edu-icon" style="color:var(--accent-cyan);">{icon_html}</div>
                <div>
                    <div class="edu-degree">{edu['degree']}</div>
                    <div class="edu-institution">{edu['institution']}</div>
                    <div class="edu-duration"><i class="fas fa-calendar-alt"></i> {edu['duration']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
