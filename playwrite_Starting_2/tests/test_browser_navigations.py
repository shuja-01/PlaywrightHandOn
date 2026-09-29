import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.wait_for_timeout(30000)
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # click on forgot password link
    page.locator("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
    page.wait_for_timeout(5000)

    # go back to login page : navigation button
    page.go_back()
    page.wait_for_timeout(5000)

    # go forward to forgot password page : navigation button
    page.go_forward()
    page.wait_for_timeout(5000)

    # reload the page
    page.reload()
    page.wait_for_timeout(5000)