from playwright.sync_api import Page, expect


def test_verifyPageUrl(page:Page): # page is a builtin playwright fixture page is the part of Page class (Fixture is a reuable function)
    page.goto("https://www.saucedemo.com") #passing the url # by default open on chromium engine Edge/Chrome
    myurl = page.url
    print(f"Url of the application:{myurl}")
    # for verification playwright has its own assertion we are not going to use pytest assertion
    expect(page).to_have_url("https://www.saucedemo.com/") # verifying the url correct or not

def test_verifyTitile(page:Page):
    page.goto("https://www.saucedemo.com")

    myTitle = page.title()
    print(f"Title of the page: {myTitle}")
    expect(page).to_have_title("Swag Labs")


# https://www.saucedemo.com/
# https://practicetestautomation.com/blog/


