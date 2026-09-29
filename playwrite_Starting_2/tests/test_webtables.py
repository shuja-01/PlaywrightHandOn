from playwright.sync_api import Page, expect

def test_web_table(page:Page):
    page.goto("https://practice-automation.com/tables/")
    page.wait_for_timeout(3000)
    table = page.locator("table").first
    table.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)
    rows = table.locator("tr")
    expect(rows).to_have_count(4)

    for i in range(rows.count()):
        cells = rows.nth(i).locator("td")
        expect(cells).to_have_count(2)
        if cells.count()> 0 and cells.nth(0).inner_text() == "Oranges":
            expect(cells.nth(1)).to_have_text("$3.99")
            break