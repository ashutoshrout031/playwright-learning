import pytest

from playwright.sync_api import Page, expect

def test_verify_radiobutton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    male_radio = page.locator("#male")
    
    # check element is visible/enabled or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    # male radio button should not be checked by default
    expect(male_radio).not_to_be_checked()

    # Select/Check the radio button
    male_radio.check()

    # after checking the radio button it should be checked
    expect(male_radio).to_be_checked()

    page.wait_for_timeout(5000)
