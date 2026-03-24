import requests
from config import BASE_URL

def test_github_api_status():
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "API is not reachable"

def test_github_api_content():
    response = requests.get(BASE_URL)
    data = response.json()
    assert "current_user_url" in data, "Invalid API response"

def test_invalid_endpoint():
    response = requests.get(BASE_URL + "/invalid")
    assert response.status_code == 200, "Intentional failure for testing"

def get_test_cases():
    return [
        test_github_api_status,
        test_github_api_content,
        test_invalid_endpoint
    ]
