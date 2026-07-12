"""Technical Projects section."""
import streamlit as st
from app.utils.helpers import section_header, render_bullet_list


def render_projects(data: dict) -> None:
    section_header("fas fa-rocket", "Technical Projects")
    for project in data.get("projects", []):
        tags_html = "".join(
            f'<span class="tag">{t}</span>' for t in project.get("tags", [])
        )
        bullets_html = render_bullet_list(project["bullets"])
        st.markdown(
            f"""
            <div class="project-card scroll-reveal">
                <div class="project-title">{project['title']}</div>
                <div class="project-duration"><i class="fas fa-clock"></i> {project['duration']}</div>
                <div class="project-tags">{tags_html}</div>
                {bullets_html}
            </div>
            """,
            unsafe_allow_html=True,
        )
