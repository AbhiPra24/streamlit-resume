"""Testimonials / recommendations section."""
import streamlit as st
from app.utils.helpers import section_header


def render_testimonials(data: dict) -> None:
    testimonials = data.get("testimonials", [])
    if not testimonials:
        return

    section_header("fas fa-quote-left", "Testimonials")
    for t in testimonials:
        st.markdown(
            f"""
            <div class="testimonial-card scroll-reveal">
                <div class="testimonial-quote">&ldquo;{t['quote']}&rdquo;</div>
                <div class="testimonial-author">
                    <strong>{t['author']}</strong>
                    <span class="testimonial-role">{t['role']} &middot; {t['company']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
