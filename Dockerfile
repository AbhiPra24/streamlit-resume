# syntax=docker/dockerfile:1

# ---- Stage 1: builder — install dependencies only ----
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---- Stage 2: runtime — lean image, no dev/test deps ----
FROM python:3.11-slim AS runtime

WORKDIR /app

# Bring over only the installed packages from the builder stage.
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Application code + theme config only — no tests/, no requirements-dev.txt,
# no docs/ (the static GitHub Pages site ships independently of this image).
COPY app/ ./app/
COPY .streamlit/ ./.streamlit/

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')" || exit 1

# --server.address=0.0.0.0 is required for the app to be reachable from
# outside the container (run.sh's localhost binding only works for
# non-containerized local use).
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
