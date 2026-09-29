from playwright.sync_api import Playwright

def test_apiChaining(playwright: Playwright):
    request = playwright.request.new_context()
    url = "https://gorest.co.in/public/v2/users"

    response = request.get(
        url,
        headers={"Authorization": "Bearer 43372f82f2332c239cf4e56e8dd9fc673fa31fb23d8979abcaec4114ba737a9d",
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