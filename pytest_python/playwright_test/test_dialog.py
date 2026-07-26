import pytest
from playwright.sync_api import expect,Page

@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach 1 Not preffered
    # registering event
    def handle_dialog(dialog):
        dialog.accept()


    page.on("dialog",handle_dialog)  #on() is for registering event
    page.wait_for_timeout(3000)
    page.locator('#alertBtn').click()  # clicking on the button which will open dialog
    page.wait_for_timeout(4000)

@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach 2 Using Lambda function
    
    page.on("dialog", lambda dialog :  dialog.accept())     # var =  lambda parameters: expression
    page.wait_for_timeout(5000)
    page.locator('#alertBtn').click()  # clicking on the button which will open dialog
    page.wait_for_timeout(5000)

def test_conformation_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach: Using Lambda function
    
    page.on("dialog", lambda dialog :  dialog.accept())     # var =  lambda parameters: expression. accept() for ok 
    page.wait_for_timeout(5000)
    page.locator('#confirmBtn').click()  # clicking on the button which will open dialog
    page.wait_for_timeout(5000)

    text = page.locator("#demo").inner_text()
    print("Output Text: ====>",text)

    page.wait_for_timeout(4000)

def test_conformation_dialog2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach: Using Lambda function
    
    page.on("dialog", lambda dialog :  dialog.dismiss())     # var =  lambda parameters: expression. dismiss() fro cancel
    page.wait_for_timeout(5000)
    page.locator('#confirmBtn').click()  # clicking on the button which will open dialog
    page.wait_for_timeout(5000)

    text = page.locator("#demo").inner_text()
    print("Output Text: ====>",text)
    expect(page.locator("#demo")).to_have_text('You pressed Cancel!')
    page.wait_for_timeout(4000)

def test_prompt_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach: Using Lambda function
    
    page.on("dialog", lambda dialog :  dialog.accept('John'))   # Since it is an interactive prompt so we can pass value through accept()
    page.wait_for_timeout(5000)
    page.locator('#promptBtn').click()  
    page.wait_for_timeout(5000)

    text = page.locator("#demo").inner_text()
    print("Output Text: ====>",text)

    expect(page.locator('#demo')).to_contain_text('John')

    page.wait_for_timeout(4000)

def test_prompt_dialog2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach: Using Lambda function
    
    page.on("dialog", lambda dialog :  dialog.dismiss())     
    page.locator('#promptBtn').click() 
    page.wait_for_timeout(5000)

    text = page.locator("#demo").inner_text()
    print("Output Text: ====>",text)
    # expect(page.locator("#demo")).to_have_text('You pressed Cancel!')
    page.wait_for_timeout(4000)