"""GitHub project showcase — static placeholder data, no live API calls."""
import streamlit as st
from app.utils.helpers import section_header


def render_github_projects(data: dict) -> None:
    projects = data.get("github_projects", [])
    if not projects:
        return

    section_header("fab fa-github", "GitHub")
    for repo in projects:
        st.markdown(
            f"""
            <a class="project-card github-card scroll-reveal" href="{repo['url']}" target="_blank">
                <div class="project-title"><i class="fab fa-github"></i> &nbsp;{repo['name']}</div>
                <p class="github-description">{repo['description']}</p>
                <div class="project-tags">
                    <span class="tag">{repo['language']}</span>
                    <span class="tag"><i class="fas fa-star"></i> &nbsp;{repo['stars']}</span>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )
