"""Experience timeline component."""
import streamlit as st
from app.utils.helpers import section_header, render_bullet_list


def render_experience(data: dict) -> None:
    section_header("💼", "Experience")
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)

    for job in data.get("experience", []):
        color = job.get("color", "#00d4ff")
        company_line = job["company"]
        if job.get("location"):
            company_line += f" &nbsp;·&nbsp; {job['location']}"

        bullets_html = render_bullet_list(job["bullets"])

        st.markdown(
            f"""
            <div class="timeline-item">
                <div class="timeline-dot" style="border-color:{color}; box-shadow: 0 0 10px {color}40;"></div>
                <div class="timeline-card" style="border-top: 2px solid {color}20;">
                    <div class="job-header">
                        <span class="job-title">{job['title']}</span>
                        <span class="job-duration">📅 {job['duration']}</span>
                    </div>
                    <div class="job-company" style="color:{color};">🏢 {company_line}</div>
                    {bullets_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
