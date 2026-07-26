import pytest

from playwright.sync_api import Page, expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # 1. Select specific checkbox
    # suday_chkbox = page.get_by_label("Sunday")
    # suday_chkbox.check()

    # expect(suday_chkbox).to_be_checked()

    # page.wait_for_timeout(5000)

    # 2. count number of checboxes
    # step1: create a list of checkbox labels and empty list to store the checkbox locators

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']  # maintans the label of checkboxes

    # checkboxes = []  # empty list to store the checkbox locators
    # step2: loop through the list of checkbox labels and get the locator for each checkbox and store it in the empty list
    # for day in days:
    #     chkbox = page.get_by_label(day)
    #     checkboxes.append(chkbox)

    checkboxes = [page.get_by_label(day) for day in days]  # list comprehension to get the checkbox locators

    print("Total number of checkboxes: ", len(checkboxes))

    # 3. Check all the checkboxes in one shot and assert all the checkboxes are checked

    # for chkbox in checkboxes:
    #     chkbox.check()
    #     expect(chkbox).to_be_checked()
    #     # page.wait_for_timeout(3000)

    # page.wait_for_timeout(5000)


    # 4. unselect/unchecked last 3 checkboxes
    # for chkbox in checkboxes[-3:]:
    #     chkbox.uncheck()
    #     expect(chkbox).not_to_be_checked()

    # page.wait_for_timeout(5000)

    # 5. Toggle checkboxes (if checkbox is checked then uncheck it and if it is unchecked then check it)
    # for chkbox in checkboxes:
    #     if chkbox.is_checked():
    #         chkbox.uncheck()
    #         expect(chkbox).not_to_be_checked()
    #     else:
    #         chkbox.check()
    #         expect(chkbox).to_be_checked()

    # page.wait_for_timeout(5000)

    # 6. Randomly checkboxes - check 1,3,6
    # index = [1,3,6]
    
    # for i in index:
    #     checkboxes[i].check()
    #     expect(checkboxes[i]).to_be_checked()
    #     page.wait_for_timeout(3000)

    # Select checkbox based on the label/input value by choice

    weekday = "Friday"
    for label in days:
        if label == weekday:
            chkbox = page.get_by_label(label)
            chkbox.check()
            expect(chkbox).to_be_checked()
            
    page.wait_for_timeout(5000)

# ! Note If we use css or xpath then it will be difficult to handle since the group of elements will not be written as form of list. and we can't assert operations since xpath or css never return element. They return only value
# Assignment verify this

    
