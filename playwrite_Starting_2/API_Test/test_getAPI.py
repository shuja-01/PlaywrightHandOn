from playwright.sync_api import Playwright

def test_getAPI(playwright: Playwright):
    request = playwright.request.new_context()
    url = "https://gorest.co.in/public/v2/users"

    response = request.get(
        url,
        headers={"Authorization": "Bearer 43372f82f2332c239cf4e56e8dd9fc673fa31fb23d8979abcaec4114ba737a9d",
                 "Accept": "application/json"}
        )

    assert response.status == 200
    assert response.ok
    assert "application/json" in response.headers["content-type"]

    users = response.json()

    assert len(users) > 0

    # print(users)
    first_user = users[0]
    print(first_user)

    assert isinstance(first_user["id"], int)
    assert first_user["id"] > 0

    assert first_user["gender"] in ["male", "female"]
    assert "id" in first_user
    assert first_user["id"] == 8612828