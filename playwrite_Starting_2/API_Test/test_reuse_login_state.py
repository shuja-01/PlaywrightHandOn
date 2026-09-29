from playwright.sync_api import Page, expect

def test_reuse_login_state(page: Page):
    context = page.context.browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    page.wait_for_timeout(3000)
    expect(page.locator("h6")).to_have_text("Dashboard")
    