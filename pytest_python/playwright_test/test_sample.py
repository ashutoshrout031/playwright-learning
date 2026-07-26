# '''
# Capture screenshots,videos and trace for the test
# '''
# import pytest
from playwright.sync_api import Playwright, expect, Page 

# def test_url(page:Page):
#     page.goto("https://demoblaze.com/index.html")
#     expect(page).to_have_url("https://demoblaze.com/index.html1")


# def test_Title(page:Page):
#     page.goto("https://demoblaze.com/index.html")
#     expect(page).to_have_title("STORE")

# def test_login(page:Page):
#     page.goto("https://demoblaze.com/index.html")
#     page.wait_for_timeout(4000)
#     page.locator('#login2').click()
#     page.locator('#loginusername').fill('pavanol')
#     page.locator('#loginpassword').fill('test@123')
#     page.locator("button:has-text('Log in')").click()
#     page.wait_for_timeout(10000)
#     expect(page.locator('#logout2')).to_be_visible()
#     expect(page.locator('#nameofuser')).to_have_text('Welcome pavanol')


def test_sample(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()
    
    page.get_by_text("PIM").click()
    page.wait_for_timeout(3000)

    

