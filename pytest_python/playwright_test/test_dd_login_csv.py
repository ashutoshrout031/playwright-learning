import csv
from playwright.sync_api import expect, Page, Playwright, sync_playwright
import pytest

#Read CSV File

login_data = []
file = open('testdata/data.csv',newline='',encoding='utf-8')
reader = csv.DictReader(file)

for row in reader:
    login_data.append((row["email"], row["password"], row["validity"]))


@pytest.mark.parametrize("email,password,validity",login_data)
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


    