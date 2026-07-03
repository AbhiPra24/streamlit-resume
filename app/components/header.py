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
                    📧 {data['email']}
                </a>
                <a class="contact-pill" href="tel:{data['phone']}">
                    📱 {data['phone']}
                </a>
                <span class="contact-pill">
                    📍 {data['location']}
                </span>
                <a class="contact-pill" href="{data['linkedin_url']}" target="_blank">
                    💼 {data['linkedin']}
                </a>
                <a class="contact-pill" href="{data['github_url']}" target="_blank">
                    🐙 GitHub
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
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-icon">{stat['icon']}</div>
                    <div class="stat-value">{stat['value']}</div>
                    <div class="stat-label">{stat['label']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
