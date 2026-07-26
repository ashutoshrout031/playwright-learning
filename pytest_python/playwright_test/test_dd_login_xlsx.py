'''
openpyxl
    pip install openpyxl


    ExcelFile ----> Workbook ----> Worksheet ----> Rows/Columns ----> Cell
'''


from playwright.sync_api import expect, Page, Playwright, sync_playwright
import pytest
import openpyxl as opxl



# reading data from excel file

login_data = []
workbook = opxl.load_workbook("testdata/data.xlsx")
worksheet = workbook.active  # or workbook["Sheet1"]  # if you want to access a specific sheet by name 

# Reading data from the worksheet using loop and appending it to the login_data list
for row in worksheet.iter_rows(min_row=2, values_only=True):
    email, password, validity = row
    login_data.append((str(email or ""), str(password or ""), str(validity or "")))

workbook.close()  # Close the workbook after reading the data


@pytest.mark.parametrize("email,password,validity", login_data)
def test_login_dd(email, password, validity, page: Page):

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


    