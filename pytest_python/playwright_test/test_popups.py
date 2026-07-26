from playwright.sync_api import Playwright, expect

def test_popups(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("popup", lambda popup: popup.wait_for_load_state())

    page.locator("#PopUp").click()

    page.wait_for_timeout(4000)

    all_popups = context.pages
    print(f"Total popups opened: {len(all_popups)}")

    # capture urls of all the popups pages
    for pw in all_popups:
        print("URL==>",pw.url)
        print("Title==>", pw.title())
        print("---------------------------------------------------")
        title = pw.title()
        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(4000)
            expect(pw).to_have_title("Installation | Playwright")
            pw.close() # closing the popup page

    page.wait_for_timeout(4000)

    context.close()  # closing the context
    browser.close()  # closing the browser


    """
    We started only one page. After clicking on the button, 3 popups/pages are opened which are belongs to the same contexts.

    """
        

