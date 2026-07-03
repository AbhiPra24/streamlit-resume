"""
Streamlit Resume — Main Entrypoint
Abhinav Prakash | Senior SDET & AI Automation Engineer
"""
import sys
import os

# Ensure project root is on sys.path so `app.*` imports work when
# Streamlit runs this file directly (e.g. `streamlit run app/main.py`)
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import streamlit as st

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="Abhinav Prakash | Senior SDET & AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "mailto:abhinavprakash616@gmail.com",
        "Report a bug": "https://github.com/AbhiPra24",
        "About": "Interactive Resume — Built with Streamlit ⚡",
    },
)

# ── Local imports (after set_page_config) ───────────────────────────────────
from app.utils.helpers import load_css
from app.data.resume import RESUME_DATA
from app.components.header import render_header
from app.components.terminal import render_terminal
from app.components.summary import render_summary
from app.components.projects import render_projects
from app.components.experience import render_experience
from app.components.skills import render_skills
from app.components.education import render_education
from app.components.certifications import render_certifications

# ── CSS ──────────────────────────────────────────────────────────────────────
load_css("app/styles/main.css")

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-profile">
            <div class="sidebar-avatar">👨‍💻</div>
            <div class="sidebar-name">Abhinav Prakash</div>
            <div class="sidebar-title">Senior SDET & AI Engineer</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown("**🧭 Navigate**")
    nav_items = [
        ("🏠", "Home"),
        ("🖥️", "Terminal"),
        ("💡", "Summary"),
        ("🚀", "Projects"),
        ("💼", "Experience"),
        ("🧠", "Skills"),
        ("🎓", "Education"),
        ("📜", "Certifications"),
    ]
    for icon, label in nav_items:
        st.markdown(
            f'<a href="#{label.lower()}" class="sidebar-nav-item">{icon} &nbsp;{label}</a>',
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("**📥 Download**")
    # Print-to-PDF via browser
    st.iframe(
        srcdoc="""
        <html><body style="margin:0;background:transparent;">
        <button onclick="window.print()"
                style="
                    width:100%; padding:10px 0; border:none; border-radius:100px;
                    background:linear-gradient(135deg,#00d4ff,#8b5cf6);
                    color:#070b14; font-weight:700; font-size:14px;
                    cursor:pointer; font-family:Inter,sans-serif;
                    transition:opacity 0.2s;
                "
                onmouseover="this.style.opacity=0.85"
                onmouseout="this.style.opacity=1">
            📄 Save as PDF
        </button>
        </body></html>
        """,
        height=50,
    )

    st.divider()
    st.markdown(
        """
        <div style="font-size:0.72rem; color:#475569; text-align:center; line-height:1.7;">
            Built with ❤️ using Streamlit<br>
            <a href="https://github.com/AbhiPra24" style="color:#00d4ff; text-decoration:none;">
                🐙 GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Main Content ──────────────────────────────────────────────────────────────
render_header(RESUME_DATA)
render_terminal()
render_summary(RESUME_DATA)
render_projects(RESUME_DATA)
render_experience(RESUME_DATA)
render_skills(RESUME_DATA)
render_education(RESUME_DATA)
render_certifications(RESUME_DATA)

# Footer
st.markdown(
    """
    <div style="
        margin-top:4rem; padding:2rem 0; text-align:center;
        border-top:1px solid rgba(255,255,255,0.05);
        color:#475569; font-size:0.8rem; line-height:2;
    ">
        <span style="background:linear-gradient(135deg,#00d4ff,#8b5cf6);
                     -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                     font-weight:700;">
            Abhinav Prakash
        </span>
        &nbsp;·&nbsp; abhinavprakash616@gmail.com &nbsp;·&nbsp; +91 94575 48199<br>
        <span>Made with ⚡ Streamlit &amp; Python</span>
    </div>
    """,
    unsafe_allow_html=True,
)
