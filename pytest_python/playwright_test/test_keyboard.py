from playwright.sync_api import expect, Page

def test_keyboardaction(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    inpt_1 = page.locator('#input1')

    # 1. Focus on input 1
    inpt_1.focus()
    page.wait_for_timeout(3000)    
    # 2. provide the text in input 1

    page.keyboard.insert_text("Welcome")
    page.wait_for_timeout(3000)
    # 3. ctrl + A
    page.keyboard.press("Control+A")
    page.wait_for_timeout(3000)
    # 4. ctrl + C
    page.keyboard.press("Control+C")
    page.wait_for_timeout(3000)
    # 5. Press TAB key two times to navigate/focus on input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.wait_for_timeout(3000)
    # 6. ctrl + V - Paste the text inside 2nd inputbox -- input2
    page.keyboard.press("Control+V")
    page.wait_for_timeout(3000)
    # 7. Press TAB key two times to navigate/focus on input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.wait_for_timeout(3000)
    # 8. ctrl + V - Paste the text inside 3rd inputbox -- input3
    page.keyboard.press("Control+V")
    page.wait_for_timeout(3000)

    inpt_2 = page.locator("#input2")
    inpt_3 = page.locator("#input3")
    page.wait_for_timeout(3000)
    expect(inpt_2).to_have_value("Welcome")
    expect(inpt_3).to_have_value("Welcome")
    page.wait_for_timeout(3000)




