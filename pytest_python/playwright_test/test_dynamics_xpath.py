import pytest

from playwright.sync_api import Page,expect


def test_handle_dynamic_element(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)
    for i in range(5):
       button =  page.locator("//button[starts-with(@name,'st')]")
       button.click()
       page.wait_for_timeout(3000)

       
