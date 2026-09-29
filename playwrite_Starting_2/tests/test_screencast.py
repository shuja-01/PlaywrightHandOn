from playwright.sync_api import Page, expect

def test_screencast(page:Page):

    page.set_viewport_size({"width": 1920, "height": 1080})
    page.wait_for_timeout(3000)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(3000)

    page.screencast.start(
        path="screencast.webm",
    )
    page.wait_for_timeout(3000)

    page.screencast.show_actions(
        position="top-right",
        duration=2000,
        font_size=20,
    )

    page.screencast.show_chapter(
        title="Orange HRM Login Demo",
        description="This is a demo of Orange HRM login page",
        duration=5000,
    )

    username = page.locator("input[name='Username']")
    username.fill("Admin")
    page.wait_for_timeout(3000)
    password = page.locator("input[name='Password']")
    password.fill("admin123")
    page.locator("button[type='submit']").click()
    page.screencast.stop()
    page.wait_for_timeout(3000)
    