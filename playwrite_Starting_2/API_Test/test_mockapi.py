import json
from playwright.sync_api import Playwright, Page

def test_mock_user(page:Page):
    mock_data = {
        "id":999999,
        "name":"Testing",
        "email":"testing@test.com",
        "gender": "Male",
        "status":"inactive"
    }

    page.route("**/public/v2/users", lambda route: route.fulfill(
        status=201,
        content_type="application/json",
        body=json.dumps(mock_data)
    ))
    with page.expect_response("**/public/v2/users") as response_info:
        page.evaluate("""
            fetch("https://gorest.co.in/public/v2/users", { method: "POST"})
            
            """)
    body = response_info.value.json()

    assert response_info.value.status == 201
    assert body["id"]==999999
    print(body)