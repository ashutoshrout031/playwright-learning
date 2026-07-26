import pytest
from playwright.sync_api import Page, expect

def test_verify_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_name = page.locator("#name")
    
    # check element is visible/enabled or not
    expect(text_name).to_be_visible()
    expect(text_name).to_be_enabled()

    #check the attribute of the element
    expect(text_name).to_have_attribute("maxlength","15")

    #get an attribute of hte element
    max_length = text_name.get_attribute("maxlength")
    print("Max length of the input box is: ", max_length)
    assert max_length == "15", f"Expected maxlength to be 15 but got {max_length}"   
    # in Python playwright we have to use pytest assert statement for validation instead of expect() method which is used in JavaScript/TypeScript

    # Fill the text inside the input box
    text_name.fill("Ram Charan Sampath")

    # get the input value from inputbox
    entered_value = text_name.input_value()
    print("Entered value in the input box is: ", entered_value)

    page.wait_for_timeout(5000)
    