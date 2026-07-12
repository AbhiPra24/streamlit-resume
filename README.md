# ⚡ Abhinav Prakash — Interactive Resume

> **Senior SDET & AI Automation Engineer** | Built with Streamlit + Python

[![CI](https://github.com/AbhiPra24/streamlit-resume/actions/workflows/ci.yml/badge.svg)](https://github.com/AbhiPra24/streamlit-resume/actions)

---

## 🚀 Features

- 🎨 **Dark neon theme** — glassmorphism cards, gradient text, animated skill bars
- 🖥️ **Interactive terminal** — typewriter animation replaying career highlights
- 📊 **Plotly radar chart** — visual skill proficiency overview
- 📅 **Experience timeline** — colour-coded vertical timeline
- 📥 **PDF export** — browser print-to-PDF button
- 🧪 **Playwright headless tests** — full CI test coverage
- 🌿 **Feature-branch workflow** — production-grade branching strategy

---

## 📁 Structure

```
streamlit-resume/
├── app/
│   ├── main.py                # Streamlit entrypoint
│   ├── data/resume.py         # Combined resume data
│   ├── components/            # Modular UI components
│   ├── styles/main.css        # Dark neon CSS
│   └── utils/helpers.py       # Utilities
├── tests/
│   ├── conftest.py            # Playwright fixtures
│   └── test_resume.py         # Headless tests
├── .streamlit/config.toml     # Theme config
├── .github/workflows/ci.yml   # GitHub Actions CI
├── requirements.txt
├── requirements-dev.txt
└── run.sh
```

---

## ⚡ Quick Start

```bash
# 1. Clone
git clone https://github.com/AbhiPra24/streamlit-resume.git
cd streamlit-resume

# 2. Create venv & install
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run
streamlit run app/main.py
# or
bash run.sh
```

---

## 🧪 Running Tests

```bash
# Install dev deps
pip install -r requirements-dev.txt

# Install Playwright browsers
playwright install chromium

# Run tests
pytest tests/ -v --browser chromium
```

---

## 🌿 Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable production |
| `feature/*` | New features / resume updates |
| `fix/*` | Bug fixes |

---

## 📬 Contact

**Abhinav Prakash** · abhinavprakash616@gmail.com · [LinkedIn](https://linkedin.com/in/abhipra24)