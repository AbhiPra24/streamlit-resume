"""Writing / blog links section."""
import streamlit as st
from app.utils.helpers import section_header


def render_writing(data: dict) -> None:
    posts = data.get("writing", [])
    if not posts:
        return

    section_header("fas fa-pen-nib", "Writing")
    for post in posts:
        st.markdown(
            f"""
            <a class="project-card writing-card scroll-reveal" href="{post['url']}" target="_blank">
                <div class="project-title">{post['title']}</div>
                <div class="project-duration"><i class="fas fa-calendar-alt"></i> &nbsp;{post['date']}</div>
                <p class="writing-summary">{post['summary']}</p>
            </a>
            """,
            unsafe_allow_html=True,
        )
