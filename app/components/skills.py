"""Skills section — radar chart, animated progress bars + categorized tag pills."""
import plotly.graph_objects as go
import streamlit as st
from app.utils.helpers import section_header


def _render_radar_chart(skills: dict) -> None:
    """Plotly radar/spider chart of proficiency across skill categories."""
    categories = list(skills.keys())
    values = [info["proficiency"] for info in skills.values()]
    # Close the polygon by repeating the first point.
    categories_closed = categories + [categories[0]]
    values_closed = values + [values[0]]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values_closed,
            theta=categories_closed,
            fill="toself",
            fillcolor="rgba(0, 212, 255, 0.12)",
            line=dict(color="#00d4ff", width=2),
            marker=dict(color="#8b5cf6", size=6),
            name="Proficiency",
        )
    )
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showticklabels=True,
                tickfont=dict(color="#64748b", size=10),
                gridcolor="rgba(255,255,255,0.08)",
                linecolor="rgba(255,255,255,0.08)",
            ),
            angularaxis=dict(
                tickfont=dict(color="#e2e8f0", size=12),
                gridcolor="rgba(255,255,255,0.08)",
                linecolor="rgba(255,255,255,0.08)",
            ),
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=20, b=20),
        height=380,
        font=dict(family="Inter, sans-serif"),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


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

    if skills:
        _render_radar_chart(skills)

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
