'''
Valid - S - passed
Valid - U - failed

invalid - S - failed
invalid - U - passed
'''
login_test_data = [ ("laura.taylor1234@example.com","test123","valid"),
                    ("invaliduser@example.com","test321","invalid"),
                    ("validuser@example.com","testxyz","invalid"),
                    ("","","invalid")
                   ]


from playwright.sync_api import expect, Page, Playwright, sync_playwright
import pytest

@pytest.mark.parametrize("email,password,validity",login_test_data)
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


    