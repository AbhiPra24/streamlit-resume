"""Header component — hero section with name, title, contact pills, and stats."""
import streamlit as st
from app.utils.helpers import render_bullet_list


def render_header(data: dict) -> None:
    st.markdown(
        f"""
        <div class="hero-container" id="home">
            <div class="hero-name">{data['name']}</div>
            <div class="hero-title">{data['title']}</div>
            <div class="contact-pills">
                <a class="contact-pill" href="mailto:{data['email']}">
                    <i class="fas fa-envelope"></i> &nbsp;{data['email']}
                </a>
                <a class="contact-pill" href="tel:{data['phone']}">
                    <i class="fas fa-phone"></i> &nbsp;{data['phone']}
                </a>
                <span class="contact-pill">
                    <i class="fas fa-map-marker-alt"></i> &nbsp;{data['location']}
                </span>
                <a class="contact-pill" href="{data['linkedin_url']}" target="_blank">
                    <i class="fab fa-linkedin"></i> &nbsp;{data['linkedin']}
                </a>
                <a class="contact-pill" href="{data['github_url']}" target="_blank">
                    <i class="fab fa-github"></i> &nbsp;GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Stats row
    stats = data.get("stats", [])
    cols = st.columns(len(stats))
    for col, stat in zip(cols, stats):
        with col:
            icon_html = f'<i class="{stat["icon"]}"></i>' if "fa-" in stat["icon"] else stat["icon"]
            st.markdown(
                f"""
                <div class="stat-card scroll-reveal">
                    <div class="stat-icon">{icon_html}</div>
                    <div class="stat-value">{stat['value']}</div>
                    <div class="stat-label">{stat['label']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
