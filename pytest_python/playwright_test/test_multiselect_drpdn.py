import pytest
from playwright.sync_api import Page, expect

def test_multi_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options  from dropdown - 3 ways

    # page.locator('#colors').select_option(label = ["Red","Blue","Green"])  # - by label

    # page.locator('#colors').select_option(value = ["Red","Blue","Green"]) # -  by value

    # page.locator('#colors').select_option(index = [2,5])

    
    

    page.wait_for_timeout(7000)