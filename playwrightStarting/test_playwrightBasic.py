from playwright.sync_api import Page

# this playwright is a fixture provided by the pytest-playwright plugin, its avaiable globally
def test_playwrightBasic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    print(page.title())


# shortcut for the playwright : it will directly provide the page object and will open the browser with context automatically 
def test_playwrightSHortCur(page:Page):
    page.goto("https://www.google.com")
    print(page.title())