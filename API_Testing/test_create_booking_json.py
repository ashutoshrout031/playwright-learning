#---------------------------------------------------------------------
# Test: Create Booking (POST request with static body)
# Request Type: POST
# Data: External JSON File
#---------------------------------------------------------------------

from playwright.sync_api import Playwright,expect
import pytest,json

def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    req_ctnxt= playwright.request.new_context()

    # Load the data from external json file

    file = open("json_test_data/post_request_body.json","r")
    request_body = json.load(file)

    response = req_ctnxt.post(f"{base_url}/booking",data=request_body)

    response_body = response.json()

    # validation

    assert response.ok
    assert response.status==200
    print("Response Body =======>",response_body)


    # Field/Attribute validation
    assert "bookingid" in response_body
    assert "booking" in response_body

    # data validation
    booking = response_body["booking"]
    print(booking["firstname"])

    assert booking["firstname"]== "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 1300
    assert booking["depositpaid"] is True
    assert booking["additionalneeds"] == "Super Bowls"

    # Nested JSON validation
    assert booking["bookingdates"]["checkin"] == "2026-07-26"
    assert booking["bookingdates"]["checkout"] == "2026-07-28"

    # close the api context
    req_ctnxt.dispose()

