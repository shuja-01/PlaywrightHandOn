from playwright.sync_api import Page, expect
from urllib.parse import urljoin

def test_new_tab(page:Page):
    page.goto("https://practice-automation.com/window-operations/")
    page.wait_for_timeout(3000)

    with page.expect_popup() as new_tab_info:
        page.get_by_role("button", name="New Tab").click()

    new_tab = new_tab_info.value
    new_tab.wait_for_load_state()
    page.wait_for_timeout(3000)
    assert new_tab.url == "https://automatenow.io/"
    print(new_tab.url)
    page.bring_to_front()
    page.wait_for_timeout(3000)
    new_tab_button = page.get_by_role("button", name="New Tab")
    assert new_tab_button.is_visible()
