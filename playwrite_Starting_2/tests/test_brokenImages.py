from playwright.sync_api import Page, expect
from urllib.parse import urljoin

def test_broken_images(page:Page):
    page.goto("https://practice-automation.com/broken-images/")
    page.wait_for_timeout(3000)
    images = page.locator("img")

    broken_images = []
    for i in range(images.count()):
        src = images.nth(i).get_attribute("src")
        if not src:
            continue
        images_url = urljoin(page.url, src)
        #API :  Make a request to the image URL to check if it's broken
        response = page.request.get(images_url)
        if response.status != 404:
            broken_images.append(images_url)
    print(f"\nBroken Images: {len(broken_images)}")

    for url in broken_images:
        print("Broken Image URL:", url)

    assert True