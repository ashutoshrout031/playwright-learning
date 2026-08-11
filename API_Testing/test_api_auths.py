import pytest
import base64

from playwright.sync_api import Playwright

# basic Auth
# username: user
# password: pass

# def test_basic_auth(playwright: Playwright):
#     request_context = playwright.request.new_context()

#     credential = base64.b64encode(b"user:pass").decode("utf-8")

#     response = request_context.get("https://httpbin.org/basic-auth/user/pass", headers={"Authorization": f"Basic {credential}"})
#     assert response.status == 200

#     response_body = response.json()

#     print("Response body:", response_body)

#     request_context.dispose()


# basic Auth2
# username: admin
# password: admin

# def test_basic_auth(playwright: Playwright):
#     request_context = playwright.request.new_context()

#     credential = base64.b64encode(b"admin:admin").decode("utf-8")

#     response = request_context.get("https://the-internet.herokuapp.com/basic_auth", headers={"Authorization": f"Basic {credential}"})
#     assert response.status == 200

#     response_body = response.text()

#     print("Response body:", response_body)

#     request_context.dispose()


# Bearer Token Authentication
# url:https://api.github.com/user/repos

# def test_bearer_token_auth_github_rep(playwright: Playwright):
#     
#     request_context = playwright.request.new_context()

#     response = request_context.get("https://api.github.com/user/repos", headers={"Authorization": f"Bearer {token}"})


#     assert response.status == 200
#     response_body = response.json()

#     print("Response body:", response_body)

#     request_context.dispose()

# Bearer Token Authentication
# url:https://api.github.com/user

# def test_bearer_token_auth_github_user(playwright: Playwright):
#     
#     request_context = playwright.request.new_context()

#     response = request_context.get("https://api.github.com/user", headers={"Authorization": f"Bearer {token}"})


#     assert response.status == 200
#     response_body = response.json()

#     print("Response body:", response_body)

#     request_context.dispose()


# API Key Authentication - Weather app
# Webpage: https://openweathermap.org/
# url : https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# def test_api_key_auth_openweather(playwright: Playwright):
#     # key = '462b563c70b29c95617b97e9f2ff8a61'
#     request_context = playwright.request.new_context()
#     qparams = {
#         "q": "Delhi",
#         "appid": "462b563c70b29c95617b97e9f2ff8a61"
#     }

#     response = request_context.get("https://api.openweathermap.org/data/2.5/weather",params=qparams)


#     assert response.status == 200
#     response_body = response.json()

#     print("Weather Info:", response_body)

#     request_context.dispose()


# API Key Application - weatherApi
# Source webpage: https://www.weatherapi.com/docs/
# url : http://api.weatherapi.com/v1/current.json


# def test_api_key_auth_weatherapi(playwright: Playwright):
#     # key = '9c9fce0a450e4243abe02131260908'
#     request_context = playwright.request.new_context()
#     qparams = {
#         "q": "Bhubaneswar",
#         "KEY": "9c9fce0a450e4243abe02131260908"
#     }

#     response = request_context.get("http://api.weatherapi.com/v1/current.json",params=qparams)


#     assert response.status == 200
#     response_body = response.json()

#     print("Weather Info:", response_body)

#     request_context.dispose()


# OAuth2 Authentication

"""
1) From the application get the following. (Manual process)


https://imgur.com/

1) Client ID

2) Client Secrete


2) Send Post request for getting token

POST https://api.imgur.com/oauth2/token

ClientID

Client secrete

tokenURL

Redirect URL

Grant type


Authorization code

you will get token once POST request is succesfull.

3) Use Token to do API call (Get request).
"""

def test_verify_oauth2_authentication(playwright: Playwright):
    # Step 1: Initialize request context
    request_context = playwright.request.new_context()

    # Step 2: Define client credentials and OAuth2 parameters
    client_id = "cff93d24167b033"
    client_secret = "ac85c1a5bc7e775cfbcd5b40188a2aa3b9be68d2"
    redirect_uri = "https://www.getpostman.com/oauth2/callback"
    grant_type = "authorization_code"
    authorization_code = "4c91c2e0de4cc9fa95ddb6e3fd0df11cc29ef739"  # Replace with valid code

    # Step 3: Send POST request to get the access token
    token_response = request_context.post(
        "https://api.imgur.com/oauth2/token",
        form={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "code": authorization_code,
            "redirect_uri": redirect_uri
        }
    )

    # Step 4: Validate token response
    assert token_response.status == 200
    token_data = token_response.json()
    access_token = token_data.get("access_token")
    print(f"\nGenerated Access Token: {access_token}")

    assert access_token is not None, "Access token not found in response!"

    # Step 5: Use access token to make authenticated GET request
    image_response = request_context.get(
        "https://api.imgur.com/3/account/me/images",
        headers={
            "Authorization": f"Bearer {access_token}"}
    )

    # Step 6: Validate image API response
    assert image_response.status == 200
    print("\nResponse JSON:", image_response.json())

    # Step 7: Cleanup
    request_context.dispose()