import pytest
from playwright.sync_api import Page, expect

def test_bootstrap_dropdown(page:Page):
    # Lunch URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #Login steps

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()

    # click on PIM
    page.get_by_text("PIM").click()
    page.wait_for_timeout(3000)

    # click on the job title dropd down
    page.locator("form i").nth(2).click()  # this will open the  dropdown
    page.wait_for_timeout(3000)

    # count all the options in the dropdown
    options = page.locator("div[role='listbox'] span")
    option_count = options.count()
    print(f"Number of options in the dropdown: {option_count}")

    expect(options).to_have_count(option_count) # assertion for counting the option

    # Print all the options
    print("All the options from the dropdown ====>",options.all_text_contents())

    # Print all the options text using loop

    for i in range(option_count):
        print(options.nth(i).text_content())


    # select/click specific option
    for i in range(option_count):
        text = options.nth(i).inner_text()
        print(f"Option to be selecte ---> {text}")
        if text == 'Automaton Tester':
            print("Got matched")
            options.nth(i).click()
            break
    
    page.wait_for_timeout(6000)
    #Note : We can't use select_option() or index here since it is not select dropdown

