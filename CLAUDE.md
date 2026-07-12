# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A single-page interactive resume built with Streamlit. All resume content lives in one Python dict; the page is assembled by a chain of component-render functions that emit HTML/CSS directly via `st.markdown(..., unsafe_allow_html=True)` and `st.iframe`/`components.html` for iframe-embedded widgets (terminal, PDF button).

## Commands

```bash
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run (either form)
streamlit run app/main.py
bash run.sh                      # same, plus fixed port 8501 + dark theme flags

# Test (Playwright, headless, spins up its own Streamlit server on :8502)
pip install -r requirements-dev.txt
playwright install chromium
pytest tests/ -v --browser chromium

# Run a single test
pytest tests/test_resume.py::TestSections::test_skills_section -v --browser chromium
```

There is no linter or type checker configured. CI (`.github/workflows/ci.yml`) runs on push to `main`/`feature/*` and on PRs to `main`: sets up a venv, installs `requirements-dev.txt`, installs the Playwright Chromium browser, then runs the full `pytest` suite.

## Architecture

**Data flow is one-directional and centralized:** `app/data/resume.py` exports a single `RESUME_DATA` dict (name, summary, projects, experience, skills, education, certifications, stats). `app/main.py` imports it once and passes it into each `render_*(RESUME_DATA)` call in `app/components/`. There is no per-component data fetching — to change resume content, edit `RESUME_DATA` only; to change layout/order, edit the call sequence in `app/main.py`.

**Component contract:** each file in `app/components/` exposes one `render_<section>(data)` function (terminal takes no args) that:
1. Calls `section_header(icon, title)` from `app/utils/helpers.py` to emit a consistently-styled, anchor-linked (`id="{title.lower()}"`) section heading — sidebar nav links (`#home`, `#terminal`, `#summary`, etc.) jump to these anchors.
2. Renders content via raw HTML strings passed to `st.markdown(unsafe_allow_html=True)`, using inline `style=` attributes and CSS classes defined in `app/styles/main.css`.

Component functions are pure rendering — no logic beyond string formatting and iterating over `RESUME_DATA` sub-structures (e.g. `skills.py` iterates `data["skills"]` dict of `{tags, proficiency, color}`).

**Interactive widgets run inside iframes**, not as native Streamlit components, because they need arbitrary JS (typewriter animation, `window.print()`):
- `terminal.py` builds a complete standalone HTML document as a Python string (`TERMINAL_HTML`), base64-encodes it, and loads it via `st.iframe(src="data:text/html;base64,...")`. The typewriter script and scripted command/output sequence (`SEQUENCES`) live entirely inside that HTML string, not in Python.
- The PDF-export button in the sidebar (`app/main.py`) follows the same base64-data-URL-iframe pattern; there's also a near-duplicate implementation in `app/utils/pdf_export.py` (`render_pdf_button`, uses `components.html` instead) that is not currently wired into `main.py` — check which one is actually in use before editing PDF export behavior.

**Styling** is a single stylesheet (`app/styles/main.css`) injected once via `load_css()` in `main.py`, plus `.streamlit/config.toml` for the base Streamlit theme (dark, cyan/violet accent colors matching the CSS). Font Awesome icons are referenced as `fas fa-*` / `fab fa-*` class strings throughout component/data code — `section_header()` and header/stats rendering auto-detect `"fa-" in icon` to decide between an `<i class="...">` tag and a literal emoji/text icon.

**Tests are black-box browser tests**, not unit tests: `tests/conftest.py` launches a real `streamlit run` subprocess on port 8502 (session-scoped fixture, auto-torn-down), and `tests/test_resume.py` uses Playwright to assert on visible text/DOM elements (section headers, contact links, iframe presence, stat values). There's no fixture for testing `RESUME_DATA` or component functions in isolation — any content change should be checked against the literal strings asserted in `test_resume.py` (e.g. section header text, "ChargePoint"/"Cognizant" mentions, stat percentages) since they'll break if wording changes.
