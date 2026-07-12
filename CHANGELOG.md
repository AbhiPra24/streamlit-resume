# Changelog

All notable changes to this project are tracked here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- **Plotly radar chart** in the Skills section (`app/components/skills.py`) — makes the
  README's long-standing "Plotly radar chart" claim actually true. Styled to blend into
  the dark theme (transparent background, cyan/purple palette).
- **Real scroll-triggered reveal animation** — `.scroll-reveal` elements now fade in via
  IntersectionObserver as they enter the viewport, and re-trigger on every scroll pass,
  instead of firing once on page load. Implemented via `st.iframe()` (raw HTML string)
  reaching across to `window.parent.document`, since `st.markdown(unsafe_allow_html=True)`
  never executes embedded `<script>` tags (`app/utils/helpers.py::render_scroll_reveal_script`).
- **Responsive breakpoints** (`@media (max-width: 768px)` and `480px`) for the hero,
  stats grid, timeline, project cards, and education cards — the app previously had zero
  responsive CSS beyond a `@media print` block.
- **New content sections**, each following the existing `render_<section>(data)` pattern:
  - `app/components/now.py` — "Now" section (what's currently being worked on).
  - `app/components/github_showcase.py` — static GitHub project showcase cards.
  - `app/components/testimonials.py` — quote/recommendation cards.
  - `app/components/writing.py` — blog/writing post links.
  - All backed by new placeholder `RESUME_DATA` keys (`now`, `github_projects`,
    `testimonials`, `writing`) marked `# TODO: personalize before sharing`.
- **Real resume PDF download button** (`app/utils/pdf_export.py::render_resume_download_button`)
  — `st.download_button` wired to `RESUME_DATA["resume_pdf_path"]`, gracefully no-ops if
  the file doesn't exist yet. Complements the existing browser print-to-PDF button.
- **Standalone static site** at `docs/` for GitHub Pages — plain HTML/CSS/vanilla JS,
  no build step, visually mirrors the Streamlit app's dark-neon theme:
  - `docs/index.html` — full page, all sections mirrored from the Streamlit app.
  - `docs/css/style.css` — design tokens ported verbatim from `app/styles/main.css`.
  - `docs/js/terminal.js` — typewriter animation ported from `app/components/terminal.py`.
  - `docs/js/radar.js` — lightweight canvas radar chart (no Plotly CDN dependency).
  - `docs/js/reveal.js` — scroll-reveal (simpler here — no iframe/innerHTML constraints).
  - `docs/favicon.svg` — lightning-bolt favicon matching the app's `page_icon="⚡"`.
  - **Not pushed to GitHub in this session** — built and verified locally only
    (`python3 -m http.server` from `docs/`, plus `file://` path-compatibility check).
  - **Content is manually duplicated** from `RESUME_DATA` (no shared build step) — keep
    both in sync by hand; each has a `keep in sync with app/data/resume.py` comment.
- **Docker artifacts** — written but not built/run in this session (user will verify locally):
  - `Dockerfile` — multi-stage build, `python:3.11-slim` base (matches CI's Python version),
    lean runtime image excludes tests/dev deps, `HEALTHCHECK` against Streamlit's health endpoint.
  - `.dockerignore` — excludes venv, tests, dev requirements, `docs/`, docs/editor cruft.
  - `docker-compose.yml` — optional convenience wrapper, port `8501:8501`.
- Exact-pinned `requirements.txt` (was `>=` floor pins) for reproducible Docker builds:
  `streamlit==1.59.1`, `plotly==6.9.0`, `pandas==2.3.3`, `Pillow==12.3.0`.

### Fixed
- **Underlined/blue links** on contact pills and sidebar nav items — Streamlit's own
  base `<a>` styling was overriding the app's un-derlined pill/nav-item CSS because the
  app's rules lacked `!important`. Added `!important` to `text-decoration`/`color` on
  `.contact-pill` and `.sidebar-nav-item`.
- **Duplicate PDF-button implementation** — `app/main.py` had an inline base64-iframe
  print button duplicating `app/utils/pdf_export.py::render_pdf_button`. `main.py` now
  imports and calls the shared implementation instead of re-declaring it.
- **`:nth-child` animation stagger** only covered the first 3–4 items (`.timeline-item`,
  `.stat-card`); extended to 6 so longer future lists don't silently lose the stagger.

### Changed
- Applied the previously-unused `pulse-glow` keyframe to `.contact-pill:hover`.
- Applied the previously-imported-but-unused `JetBrains Mono` font to duration/metadata
  text (`.job-duration`, `.project-duration`, `.skill-bar-pct`, `.edu-duration`) for a
  subtle "code-like" monospace accent fitting an SDET resume.
- Sidebar navigation (`app/main.py`) now includes the four new sections (Now, GitHub,
  Testimonials, Writing).

## Notes for next session
- `RESUME_DATA["now"]`, `["github_projects"]`, `["testimonials"]`, and `["writing"]`
  all contain placeholder copy — personalize before sharing publicly.
- `RESUME_DATA["resume_pdf_path"]` points to `app/assets/Abhinav_Prakash_Resume.pdf`,
  which doesn't exist yet — the download button silently no-ops until a real PDF is added.
- `docs/` static site content must be manually kept in sync with `app/data/resume.py`.
- Docker artifacts are untested in this session — run `docker build -t streamlit-resume .`
  and `docker run --rm -p 8501:8501 streamlit-resume` to verify.
- GitHub Pages hosting itself (repo Settings → Pages → serve `/docs` on `main`) and
  Streamlit Community Cloud deployment are both out of scope for this session — the user
  will push and configure those separately.
