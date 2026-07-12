"""
Playwright headless tests for the interactive Streamlit resume.
"""
import pytest
from playwright.sync_api import Page, expect


# ── Helpers ──────────────────────────────────────────────────────────────────

def goto(page: Page, url: str) -> None:
    page.goto(url, wait_until="domcontentloaded")
    # Wait for Streamlit to finish rendering
    page.wait_for_function(
        "() => !document.querySelector('[data-testid=\"stSpinner\"]')",
        timeout=20_000,
    )


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestPageLoad:
    def test_page_title(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page).to_have_title("Abhinav Prakash | Senior SDET & AI Engineer")

    def test_hero_name_visible(self, page: Page, app_url: str):
        goto(page, app_url)
        locator = page.locator("text=Abhinav Prakash").first
        expect(locator).to_be_visible(timeout=15_000)

    def test_hero_title_visible(self, page: Page, app_url: str):
        goto(page, app_url)
        locator = page.locator("text=Senior SDET & AI Automation Engineer").first
        expect(locator).to_be_visible(timeout=15_000)


class TestSections:
    def test_summary_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=SUMMARY").first).to_be_visible(timeout=15_000)

    def test_terminal_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=INTERACTIVE TERMINAL").first).to_be_visible(timeout=15_000)

    def test_projects_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=TECHNICAL PROJECTS").first).to_be_visible(timeout=15_000)

    def test_experience_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=EXPERIENCE").first).to_be_visible(timeout=15_000)

    def test_skills_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=SKILLS").first).to_be_visible(timeout=15_000)

    def test_education_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=EDUCATION").first).to_be_visible(timeout=15_000)

    def test_certifications_section(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=CERTIFICATIONS").first).to_be_visible(timeout=15_000)


class TestContent:
    def test_chargepoint_experience(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=ChargePoint").first).to_be_visible(timeout=15_000)

    def test_cognizant_experience(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=Cognizant").first).to_be_visible(timeout=15_000)

    def test_iit_roorkee_education(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=Roorkee").first).to_be_visible(timeout=15_000)

    def test_mcp_project_visible(self, page: Page, app_url: str):
        goto(page, app_url)
        expect(page.locator("text=MCP Server").first).to_be_visible(timeout=15_000)

    def test_stats_cards(self, page: Page, app_url: str):
        goto(page, app_url)
        # Four stat cards should all render
        for stat_text in ["5+", "40%", "30%", "25%"]:
            expect(page.locator(f"text={stat_text}").first).to_be_visible(timeout=15_000)


class TestInteractivity:
    def test_terminal_iframe_present(self, page: Page, app_url: str):
        goto(page, app_url)
        # Terminal component renders as an iframe
        page.wait_for_selector("iframe", timeout=20_000)
        iframes = page.locator("iframe").all()
        assert len(iframes) >= 1, "No iframe found — terminal component missing"

    def test_sidebar_present(self, page: Page, app_url: str):
        goto(page, app_url)
        sidebar = page.locator("[data-testid='stSidebar']")
        expect(sidebar).to_be_visible(timeout=15_000)

    def test_plotly_chart_present(self, page: Page, app_url: str):
        goto(page, app_url)
        # Plotly chart renders inside an iframe or as a div
        page.wait_for_selector(".js-plotly-plot, iframe", timeout=20_000)

    def test_contact_email_link(self, page: Page, app_url: str):
        goto(page, app_url)
        email_link = page.locator("a[href='mailto:abhinavprakash616@gmail.com']").first
        expect(email_link).to_be_visible(timeout=15_000)

    def test_linkedin_link(self, page: Page, app_url: str):
        goto(page, app_url)
        linkedin = page.locator("a[href*='linkedin.com']").first
        expect(linkedin).to_be_visible(timeout=15_000)
