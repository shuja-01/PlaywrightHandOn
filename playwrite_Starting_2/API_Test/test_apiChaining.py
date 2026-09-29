from playwright.sync_api import Playwright

def test_apiChaining(playwright: Playwright):
    request = playwright.request.new_context()
    url = "https://gorest.co.in/public/v2/users"

    response = request.get(
        url,
        headers={"Authorization": "Bearer dv",
                 "Accept": "application/json"}
        )

    assert response.status == 200

    users = response.json()
    print(users)


    user_id = users[1]["id"]
    print(user_id)

    response2 = request.get(f"https://gorest.co.in/public/v2/users/{user_id}")
    user = response2.json()
    print(user)
