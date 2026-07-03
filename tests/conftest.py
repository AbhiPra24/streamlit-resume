"""
pytest conftest — starts Streamlit server before tests and tears it down after.
"""
import socket
import subprocess
import sys
import time
from pathlib import Path

import pytest

BASE_URL = "http://localhost:8502"
APP_PATH = str(Path(__file__).parent.parent / "app" / "main.py")


def _port_open(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        return s.connect_ex(("localhost", port)) == 0


@pytest.fixture(scope="session", autouse=True)
def streamlit_server():
    """Spin up the Streamlit app for the test session."""
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            APP_PATH,
            "--server.port=8502",
            "--server.headless=true",
            "--server.runOnSave=false",
            "--global.developmentMode=false",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Wait up to 30 s for server to be ready
    for _ in range(30):
        if _port_open(8502):
            break
        time.sleep(1)
    else:
        proc.terminate()
        pytest.fail("Streamlit server did not start within 30 seconds.")

    yield BASE_URL

    proc.terminate()
    proc.wait(timeout=10)


@pytest.fixture()
def app_url(streamlit_server):
    return streamlit_server
