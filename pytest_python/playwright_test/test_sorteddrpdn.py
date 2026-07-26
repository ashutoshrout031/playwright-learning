import pytest
from playwright.sync_api import Page, expect

def test_sorted_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    drop_down_opt = page.locator("#colors>option") # unsorted list

    # drop_down_opt = page.locator("#animals>option")  # sorted list

    option_text = [text.strip() for text in drop_down_opt.all_text_contents()]

    original_lst = option_text.copy()

    sorted_list = sorted(option_text)  # sorted(option_text, reverse=True) for descending order

    print("Original List: ",original_lst)
    print("Sorted List:", sorted_list)

    if original_lst == sorted_list:
        print("Dropdown options are sorted order ... ")
    else:
        print("Dropdown options are not sorted order ... ")

    page.wait_for_timeout(4000)