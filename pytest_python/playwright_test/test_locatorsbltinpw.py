# https://demo.nopcommerce.com/ 
# https://automationintesting.online/
# https://demo.automationtesting.in/Index.html
# https://testautomationpractice.blogspot.com/
# https://opensource-demo.orangehrmlive.com/   ******************* Assignment *************************
# https://demowebshop.tricentis.com/
# https://testpages.eviltester.com/pages/basics/basic-web-page/

# https://dev.to/mdmoeenajazkhan/ui-automation-testing-demo-site-4gid ----  source


import pytest
import re
from playwright.sync_api import Page, expect
import time

'''
   1) page.get_by_alt_text()
   2) page.get_by_text()
   3) get_by_role() Not an attribute 
   4) page.get_by_label()
   5) page.get_by_placeholder()
   6) page.get_by_title()
   7)page.get_by_test_id()

'''


# def test_verifyPageUrl(page:Page):
#     page.goto("https://www.nopcommerce.com/en")
#     expect(page).to_have_url("https://www.nopcommerce.com/en")


#  # page.get_alt_text() --> to locate images, logos mostly it is used (alt attribute)
def test_verify_pwlocators(page:Page):

   # page.goto("https://www.nopcommerce.com/en")
   # page.wait_for_timeout(5000)  # 7000ms = 7sec
   
   # logo = page.get_by_alt_text("nopCommerce")
   # expect(logo).to_be_visible()
   # # expect(page.get_by_alt_text("nopCommerce demo store")).to_be_visible()  --oneliner
   # # page.close()

   # # page.get_by_text()
   # expect(page.get_by_text("Free and open-source eCommerce platform")).to_be_visible() # full text
   # expect(page.get_by_text("Free and open")).to_be_visible() # partial text
   # expect(page.get_by_text(re.compile(".*Free.*"))).to_be_visible() # Regexp


   # page.get_role

   # page.goto("https://testautomationpractice.blogspot.com/")
   # time.sleep(4)
   # expect(page.get_by_role("heading", name="GUI Elements")).to_be_visible()
   

   # page.get_by_label  Note check lable for should be mathced with the associate field id otherwise it will fail

   # page.get_by_label("Name:",exact=False).fill("Ram Charan Sampat")
   # page.get_by_label("Email:",exact=False).fill("ramcharan@fakemail.com")
   # page.get_by_label("Phone:",exact=False).fill("98814441141")


   # page.get_by_placeholder
   # page.get_by_placeholder("Enter Name").fill("Ram Charan Sampath")
   # page.get_by_placeholder("Enter EMail").fill("testing.auto@fakemail.com")
   # page.get_by_placeholder("Enter Phone").fill("9982959210")
   # try:
   #    page.get_by_label("Address:").fill("Tester Nagar")
   # except Exception as e:
   #    print(e)
   # page.wait_for_timeout(2000)
   # page.goto("https://practice.automationtesting.in/my-account/")
   # time.sleep(4)
   # page.get_by_label("Username or email address ").fill("testing@fakemail.com")
   # page.get_by_label("Password ").first.fill("Randipuabedha")
   # page.wait_for_timeout(4000)

   # page.get_by_title
   page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
   time.sleep(3)
   expect(page.get_by_title("Home page link")).to_have_text("Home")
   expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
   page.wait_for_timeout(4000)

   #page.get_by_test_id
   expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
   expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
   page.wait_for_timeout(7000)






 # page.locator("#name").fill("Ram Sampat")
