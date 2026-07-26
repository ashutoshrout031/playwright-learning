import pytest
from playwright.sync_api import expect, Page

from loginpage import LoginPage 
from homepage import HomePage 
from cart_page import CartPage  

@pytest.mark.parametrize("username,password,product_name",[
    ("pavanol","test@123","Samsung galaxy s6")
])
def test_user_can_login_and_add_product_to_cart(page:Page,username,password,product_name):
    page.goto("https://demoblaze.com/index.html")

    # Login
    loginPage = LoginPage(page)
    loginPage.login()
    loginPage.enter_username(username)
    loginPage.enter_password(password)
    loginPage.click_login_button()


    expect(page.locator("#nameofuser")).to_contain_text(f"Welcome {username}")


    # Homepage
    homePage = HomePage(page)
    homePage.add_product_to_cart(product_name)
    # page.wait_for_timeout(4000)
    homePage.goto_cart()
    # page.wait_for_timeout(4000)

    # Cart Page
    cp = CartPage(page)
    product_in_cart = cp.check_product_in_cart(product_name)

    #assertion
    expect(product_in_cart).to_be_visible()
    

