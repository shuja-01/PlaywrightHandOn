import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_text("Playwright Test is an end-to-").click()
    page.get_by_role("link", name="Generating tests").click()