import pytest
from playwright.sync_api import Page, expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select only  option(1 option) from the dropdown

    # 1.by label  -- mostly prefered since it is visible on UI
    # page.locator("#country").select_option("India")  

    # page.locator("#country").select_option(label = "India")  # specifying label is optional

    # 2.by value  -- most time it is not present
    # page.locator("#country").select_option("germany")  # specify option value directly
    # page.locator("#country").select_option(value="germany")

    # 3.by Index
    # page.locator("#country").select_option(index=4)  # specify index keyword is mandatory and its start from 0


    # Count Number of dropdown elements
    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)
    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    for option in options_text:
        print(option)

    page.wait_for_timeout(6000)


# Note : Value based assertions not supported in playwright python since python has own assertion in pytest



