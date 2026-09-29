import time

from playwright.sync_api import Playwright

def test_postAPI(playwright: Playwright):
    request = playwright.request.new_context()
    url = "https://gorest.co.in/public/v2/users"

    unique_email = f"maschef{int(time.time())}@example.com"
    
    payload = { "name": "Master Chef", "email": unique_email, "gender": "male", "status": "active" }
    headers={"Authorization": "Bearer sdfv",
                     "Accept": "application/json"}
    
    response = request.post(
        url,
        headers=headers,
        data=payload
        )
    assert response.status == 201
    assert response.ok
    users = response.json()
    print(users)

    # assert users["name"] == "Master Chef"
    # assert users["gender"] == "male"
    assert users["name"] == payload["name"]
    assert users["gender"] == payload["gender"]

    assert "id" in users

    request.dispose()
