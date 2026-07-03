"""Utility helpers — CSS loader and HTML rendering."""
import pathlib
import streamlit as st


def load_css(path: str) -> None:
    """Inject a CSS file into the Streamlit app."""
    css_path = pathlib.Path(path)
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def section_header(icon: str, title: str) -> None:
    """Render a styled section header."""
    icon_html = f'<i class="{icon}" style="font-size:1.3rem;"></i>' if "fa-" in icon else f'<span style="font-size:1.3rem;">{icon}</span>'
    st.markdown(
        f"""
        <div class="section-header scroll-reveal" id="{title.lower()}">
            {icon_html}
            <span class="section-header-text">{title}</span>
            <div class="section-header-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_bullet_list(bullets: list[str]) -> str:
    """Convert a list of bullet strings to an HTML <ul>."""
    items = "".join(
        f"<li>{_md_bold(b)}</li>" for b in bullets
    )
    return f'<ul class="bullet-list">{items}</ul>'


def _md_bold(text: str) -> str:
    """Convert **bold** markdown to <strong> HTML."""
    import re
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
