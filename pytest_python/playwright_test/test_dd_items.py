import pytest

from playwright.sync_api import expect,Playwright,Page

searh_items = ['laptop','Gift card','smartphone','monitor']

# def test_search_items(page:Page):
#     page.goto('https://demowebshop.tricentis.com/')

#     page.locator('#small-searchterms').fill('laptop')   # We need to pass item name
#     page.locator("input[value ='Search']").click()

#     # Assertion

#     first_result = page.locator('h2 a').nth(0)

#     expect(first_result).to_contain_text("laptop",ignore_case=True)


# Data Driven Testing - Parametrization

@pytest.mark.parametrize('item',searh_items)
def test_search_items(page:Page,item):
    page.goto('https://demowebshop.tricentis.com/')

    page.locator('#small-searchterms').fill(item)   # We need to pass item name
    page.locator("input[value ='Search']").click()

    # Assertion

    first_result = page.locator('h2 a').nth(0)

    expect(first_result).to_contain_text(item,ignore_case=True)

