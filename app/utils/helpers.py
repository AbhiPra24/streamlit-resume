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


def render_scroll_reveal_script() -> None:
    """Re-trigger `.scroll-reveal` fade-ins on actual scroll via IntersectionObserver.

    `st.markdown(unsafe_allow_html=True)` sets `.innerHTML` under the hood, and
    browsers never execute <script> tags inserted that way — so a script can't
    run in the main document via st.markdown. `st.iframe()` given a raw HTML
    string instead renders it into a real `srcdoc` iframe that's same-origin
    with the parent page, so script inside it can reach across via
    `window.parent.document` and observe the real section elements (unlike the
    terminal's `data:` URI iframe, which has an opaque origin and can't touch
    the parent DOM at all). A body containing only a <script> and no real
    element got silently inlined instead of iframed in testing — including a
    real (invisible) element alongside the script reliably forces iframe
    embedding, mirroring the working pattern in pdf_export.py.
    """
    st.iframe(
        """
        <div id="scroll-reveal-watcher" style="display:none;"></div>
        <script>
        (function () {
            const doc = window.parent.document;
            doc.body.classList.add('reveal-ready');

            const io = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    entry.target.classList.toggle('is-visible', entry.isIntersecting);
                });
            }, { threshold: 0.15 });

            function observeAll() {
                doc.querySelectorAll('.scroll-reveal').forEach((el) => io.observe(el));
            }

            // Streamlit re-renders parts of the DOM async; retry briefly on load.
            observeAll();
            setTimeout(observeAll, 500);
            setTimeout(observeAll, 1500);
        })();
        </script>
        """,
        height=1,
    )
