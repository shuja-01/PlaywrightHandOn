from playwright.sync_api import Page, expect

def test_sortable_web_table(page:Page):
    page.goto("https://practice-automation.com/tables/")
    page.wait_for_timeout(3000)
    table = page.locator("table").nth(1)
    page.wait_for_timeout(3000)
    rows = table.locator("tr")
    expect(rows).to_have_count(11)
    expect(rows.first).to_be_visible()
    page.locator("text=Population (million)").click()
    page.wait_for_timeout(3000)

    pupulation_list = []
    for i in range(rows.count()):
        cells = rows.nth(1).locator("td")
        population_text = cells.nth(2).inner_text()
        clean_value = population_text.replace(",", "")
        populaion = float(clean_value)
        pupulation_list.append(populaion)
    print("Actual Population List:", pupulation_list)

    expected_population_list = sorted(pupulation_list)
    assert pupulation_list == expected_population_list
