"""
1) Create Booking (POST) ----> booking id
2) Get Booking Details (GET) -  By ID, By Names, By Dates
3) Create Token (POST/auth)
4) Partial Update Booking (PATCH)
5) Full Update Booking (PUT)
6) Delete Booking (DELETE)
"""

import json
import pytest
from playwright.sync_api import Playwright,expect

# Base URL
base_url = "https://restful-booker.herokuapp.com"

# Utility function -  reading json file
def read_json_file(file_path):
    file = open(file_path,"r")
    return json.load(file)

# Fixture - creates playwright request context

@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()


# 1. Create Booking (POST) ---> booking id
def test_create_booking(request_context):
    data = read_json_file("json_test_data/post_request_body.json")
    response = request_context.post(f"{base_url}/booking", data=data)

    assert response.ok, "POST request failed"
    assert response.status == 200

    response_body =response.json()

    print("Create Booking Response:", response_body)

    assert "bookingid" in response_body, "Booking ID not found in response"
    assert "booking" in response_body, "Booking details not found in response"

    booking = response_body["booking"]

    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["totalprice"] == data["totalprice"]
    assert booking["depositpaid"] == data["depositpaid"]
    assert booking["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"] 
    assert booking["additionalneeds"] == data["additionalneeds"]

    global booking_id  # We are making booking id global so that we can use it in other test methods
    booking_id = response_body["bookingid"]
    # return booking_id  # We can't return booking_id since it is a test method and test method never support returning value


# 2. Get Booking Details (GET) By ID, By Names, By Dates

def test_get_booking_by_id(request_context):
    response = request_context.get(f"{base_url}/booking/{booking_id}")   #https://restful-booker.herokuapp.com/booking/1

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print(f"Booking Details by ID {booking_id} Response:", response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body


def test_get_booking_by_name(request_context):
    names_param = {
        "firstname": "Jim",
        "lastname": "Brown"
    }

    # Passing query parameters in GET request
    response = request_context.get(f"{base_url}/booking", params=names_param)   
    # https://restful-booker.herokuapp.com/booking?firstname=sally&lastname=brown


    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print(f"Booking Details by ID's Fetched by Names  {names_param}", response_body)
    assert len(response_body) > 0
    for item in response_body:
        assert "bookingid" in item

    
# def test_get_booking_by_dates(request_context):
#     dates_param = {
#         "checkin": "2026-07-26",
#         "checkout": "2026-07-28"
#     }

#     # Passing query parameters in GET request
#     response = request_context.get(f"{base_url}/booking", params=dates_param)   
#     # https://restful-booker.herokuapp.com/booking?checkin=2014-03-13&checkout=2014-05-21


#     assert response.ok
#     assert response.status == 200

#     response_body = response.json()
#     print(f"Booking Details by ID's Fetched by Dates  {dates_param}", response_body)
#     assert len(response_body) > 0
#     for item in response_body:
#         assert "bookingid" in item

# 3. Create Token (POST/auth)
def test_create_token(request_context):
    data = read_json_file("json_test_data/token_request_body.json")
    response = request_context.post(f"{base_url}/auth", data=data)

    assert response.ok, "POST request failed"
    assert response.status == 200

    response_body =response.json()

    print("Create Token Response:", response_body)

    assert "token" in response_body, "Token not found in response"

    global token  # We are making token global so that we can use it in other test methods
    token = response_body["token"]

# 4. Partial Update Booking (PATCH)
def test_partial_update_booking(request_context):
    data = read_json_file("json_test_data/patch_request_body.json")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

    response = request_context.patch(f"{base_url}/booking/{booking_id}", data=data, headers=headers)

    assert response.ok, "PATCH request failed"
    assert response.status == 200

    response_body = response.json()

    print("Partial Update Booking Response:", response_body)

    for key in data.keys():
        assert key in response_body, f"{key} not found in response"
        assert response_body[key] == data[key], f"{key} not updated correctly"


# Full Update Booking (PUT)
def test_full_update_booking(request_context):
    data = read_json_file("json_test_data/put_request_body.json")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

    response = request_context.put(f"{base_url}/booking/{booking_id}", data=data, headers=headers)

    assert response.ok, "PUT request failed"
    assert response.status == 200

    response_body = response.json()

    print("Full Update Booking Response:", response_body)

    for key in data.keys():
        assert key in response_body, f"{key} not found in response"
        assert response_body[key] == data[key], f"{key} not updated correctly"

# 5. Delete Booking (DELETE)
def test_delete_booking(request_context):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

    response = request_context.delete(f"{base_url}/booking/{booking_id}", headers=headers)

    assert response.ok, "DELETE request failed"
    assert response.status == 201

    print(f"Booking with ID {booking_id} deleted successfully.")