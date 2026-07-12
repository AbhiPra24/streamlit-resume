"""Skills section — animated progress bars + categorized tag pills."""
import streamlit as st
from app.utils.helpers import section_header


def _skill_bar(label: str, pct: int, color: str) -> str:
    return f"""
    <div class="skill-bar-container scroll-reveal">
        <div class="skill-bar-header">
            <span class="skill-bar-label">{label}</span>
            <span class="skill-bar-pct" style="color:{color};">{pct}%</span>
        </div>
        <div class="skill-bar-track">
            <div class="skill-bar-fill"
                 style="width:{pct}%; background: linear-gradient(90deg, {color}, {color}80);">
            </div>
        </div>
    </div>
    """


def render_skills(data: dict) -> None:
    section_header("fas fa-brain", "Skills")
    skills = data.get("skills", {})

    bars_html = "".join(
        _skill_bar(name, info["proficiency"], info["color"])
        for name, info in skills.items()
    )
    st.markdown(bars_html, unsafe_allow_html=True)

    # Tag cloud (categorized)
    st.markdown("<div style='margin-top:2rem;' class='scroll-reveal'>", unsafe_allow_html=True)
    for name, info in skills.items():
        st.markdown(f"<div style='margin-top: 1rem;'><strong style='color: var(--text-primary); font-size: 0.9rem;'>{name}</strong></div>", unsafe_allow_html=True)
        tags_html = "".join(
            f"""<span class="skill-tag"
                     style="color:{info['color']};
                            border-color:{info['color']}40;
                            background:rgba({_hex_to_rgb(info['color'])},0.07);">
                    {tag}
                </span>"""
            for tag in info["tags"]
        )
        st.markdown(
            f'<div class="skill-tags" style="margin-bottom:8px;">{tags_html}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


def _hex_to_rgb(hex_color: str) -> str:
    """Convert #RRGGBB to 'R, G, B' string for rgba()."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"{r}, {g}, {b}"
