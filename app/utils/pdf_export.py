"""PDF export utility — triggers browser print dialog via JS."""
import streamlit.components.v1 as components


PRINT_BUTTON_HTML = """
<button
  id="pdf-btn"
  onclick="window.print()"
  style="
    width: 100%;
    padding: 10px 0;
    border: none;
    border-radius: 100px;
    background: linear-gradient(135deg, #00d4ff, #8b5cf6);
    color: #070b14;
    font-weight: 700;
    font-size: 14px;
    cursor: pointer;
    font-family: Inter, sans-serif;
    letter-spacing: 0.03em;
    transition: opacity 0.2s, transform 0.2s;
  "
  onmouseover="this.style.opacity=0.85; this.style.transform='translateY(-1px)';"
  onmouseout="this.style.opacity=1; this.style.transform='translateY(0)';"
>
  📄 Save as PDF
</button>
<style>
  @media print {
    [data-testid='stSidebar'],
    [data-testid='stToolbar'],
    header, footer, .stDeployButton { display: none !important; }
    .stApp { background: white !important; color: black !important; }
  }
</style>
"""


def render_pdf_button(height: int = 52) -> None:
    """Render a PDF download button that triggers window.print()."""
    components.html(PRINT_BUTTON_HTML, height=height)
