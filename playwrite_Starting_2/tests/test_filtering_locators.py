import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/v1/index.html")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # using text filter to select the product and click on add to cart button
    # product1 = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    # product1.locator("button:has-text(\"Add to cart\")").click()
    # using locator filter to select the product and click on add to cart button
    product1 = page.locator(".inventory_item").filter(has=page.locator("button.btn_inventory"))
    product1.first.locator("button").click()
    # products = page.locator(".inventory_item_name")
    page.wait_for_timeout(5000)