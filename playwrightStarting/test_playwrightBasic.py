import time
from playwright.sync_api import Page

# this playwright is a fixture provided by the pytest-playwright plugin, its avaiable globally
def test_playwrightBasic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    print(page.title())


# shortcut for the playwright : it will directly provide the page object and will open the browser with context automatically 
def test_playwrightSHortCur(page: Page):
    page.goto("https://www.google.com")
    print(page.title())


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy") #input should be wrapped inside <label> tag for this locator to work
    page.get_by_label("Password").fill("Learning@830$3mK2") #input should be wrapped inside <label> tag for this locator to work
    page.get_by_role("combobox").select_option("teach") #in this case the dropdown should be inside <select> tag
    # page.get_by_role("link", name="terms & conditions").click() #if text is in <a> tag, then use get_by_role("link", name="text")
    # page.get_by_role("checkbox", name="terms").click() #if checkbox is present in the dom, then use get_by_role("checkbox", name="text")
    page.locator("#terms").check() # using ud to slect the check box
    page.get_by_role("button", name="Sign In").click() # locates <input type="submit" value="Sign In">
    time.sleep(5)
