"""Skills section — animated progress bars + Plotly radar chart + tag pills."""
import streamlit as st
import plotly.graph_objects as go
from app.utils.helpers import section_header


def _skill_bar(label: str, pct: int, color: str) -> str:
    return f"""
    <div class="skill-bar-container">
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


def _radar_chart(skills: dict) -> go.Figure:
    categories = list(skills.keys())
    values     = [v["proficiency"] for v in skills.values()]
    colors     = [v["color"] for v in skills.values()]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill="toself",
            fillcolor="rgba(0, 212, 255, 0.08)",
            line=dict(color="#00d4ff", width=2.5),
            marker=dict(color="#00d4ff", size=7, symbol="circle"),
            hovertemplate="<b>%{theta}</b><br>Proficiency: %{r}%<extra></extra>",
        )
    )
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(13, 21, 38, 0.6)",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color="#475569", size=10),
                gridcolor="rgba(255,255,255,0.05)",
                linecolor="rgba(255,255,255,0.05)",
            ),
            angularaxis=dict(
                tickfont=dict(color="#94a3b8", size=12),
                gridcolor="rgba(255,255,255,0.05)",
                linecolor="rgba(255,255,255,0.05)",
            ),
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e2e8f0"),
        margin=dict(t=30, b=30, l=30, r=30),
        height=380,
    )
    return fig


def render_skills(data: dict) -> None:
    section_header("🧠", "Skills")
    skills = data.get("skills", {})

    col_bars, col_radar = st.columns([1, 1], gap="large")

    with col_bars:
        bars_html = "".join(
            _skill_bar(name, info["proficiency"], info["color"])
            for name, info in skills.items()
        )
        st.markdown(bars_html, unsafe_allow_html=True)

    with col_radar:
        st.plotly_chart(
            _radar_chart(skills),
            width='stretch',
            config={"displayModeBar": False},
        )

    # Tag cloud (all tags)
    st.markdown(
        "<div style='margin-top:1.2rem;'><div class='skill-tags'>",
        unsafe_allow_html=True,
    )
    for name, info in skills.items():
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
    st.markdown("</div></div>", unsafe_allow_html=True)


def _hex_to_rgb(hex_color: str) -> str:
    """Convert #RRGGBB to 'R, G, B' string for rgba()."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"{r}, {g}, {b}"
