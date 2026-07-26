import json
from playwright.sync_api import expect, Page, Playwright, sync_playwright
import pytest

#Read JSON File

file = open('testdata/data.json','r')
login_data = json.load(file)



@pytest.mark.parametrize("email,password,validity",[
    (data["email"], data["password"], data["validity"]) for data in login_data
    ])
def test_login_dd(email,password,validity,page:Page):

    # Navigate to the demo web shop
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("#Email").fill(email)  #email id
    page.locator("#Password").fill(password)   # password

    page.locator("input[value='Log in']").click()

    # validation
    if validity=="valid":
        expect(page.locator("a[href='/logout']")).to_be_visible(timeout=5000)
    else:
        expect(page.locator("div.validation-summary-errors")).to_be_visible(timeout=5000) #checking for error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login") #checking for the login page URL


    