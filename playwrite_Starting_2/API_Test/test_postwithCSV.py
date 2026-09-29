import csv
import time
from playwright.sync_api import Playwright

def read_csv_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def test_createUser(playwright: Playwright):
    request = playwright.request.new_context()
    url = "https://gorest.co.in/public/v2/users"

    users_list = read_csv_data('users.csv')

    for user_data in users_list:
        # Append a timestamp to prevent duplicate email 422 errors
        username, domain = user_data["email"].split("@")
        unique_email = f"{username}_{int(time.time()*1000)}@{domain}"

        payload = {
            "name": user_data["name"],
            "email": unique_email,
            "gender": user_data["gender"],
            "status": user_data["status"]
        }
        
        headers = {
            "Authorization": "Bearer 43372f82f2332c239cf4e56e8dd9fc673fa31fb23d8979abcaec4114ba737a9d",
            "Accept": "application/json"
        }

        response = request.post(url, headers=headers, data=payload)
        
        assert response.status == 201
        assert response.ok

        response_body = response.json()
        print(response_body)

        assert response_body["name"] == payload["name"]
        assert response_body["gender"] == payload["gender"]
        assert "id" in response_body

    # Dispose the context after the loop finishes
    request.dispose()