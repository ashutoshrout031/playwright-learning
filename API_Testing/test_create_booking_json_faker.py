#---------------------------------------------------------------------
# Test: Create Booking (POST request with static body)
# Request Type: POST
# Data: Dynamic JSON Data using Faker
#---------------------------------------------------------------------

from datetime import datetime, timedelta
from playwright.sync_api import Playwright,expect
import pytest,json
from faker import Faker

def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    req_ctnxt= playwright.request.new_context()

    # Load the data from external json file

    fake = Faker()

    first_name=fake.first_name()
    last_name=fake.last_name()
    total_price=fake.random_int(min=100, max=5000)
    deposit_paid=fake.boolean()
    checkin_date= datetime.now().strftime("%Y-%m-%d")
    checkout_date= (datetime.now() + timedelta (days=5)).strftime("%Y-%m-%d")
    additional_needs=fake.word()

    request_body = {
        "firstname" : first_name,
        "lastname" : last_name,
        "totalprice" : total_price,
        "depositpaid" : deposit_paid,
        "bookingdates" : {
            "checkin" : checkin_date,
            "checkout" : checkout_date
        },
        "additionalneeds" : additional_needs
    }

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

    assert booking["firstname"]== first_name
    assert booking["lastname"] == last_name
    assert booking["totalprice"] == total_price
    assert booking["depositpaid"] is deposit_paid
    assert booking["additionalneeds"] == additional_needs

    # Nested JSON validation
    assert booking["bookingdates"]["checkin"] == checkin_date
    assert booking["bookingdates"]["checkout"] == checkout_date

    # close the api context
    req_ctnxt.dispose()

