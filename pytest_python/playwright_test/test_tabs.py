from playwright.sync_api import Playwright, expect,Page

def test_handle_tabs(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    # pqge = browser.new_page()  # optional
    context = browser.new_context()
    parent_page = context.new_page()
    parent_page.goto("https://testautomationpractice.blogspot.com/")

    # register an event for handle tabs

    parent_page.on("page", lambda page: page.wait_for_load_state())
    parent_page.locator("button:has-text('New Tab')").click()

    parent_page.wait_for_timeout(4000)

    all_pages = context.pages   # all pages are belong to context so no of tabs opened in the same context
    print(f"Total tabs opened: {len(all_pages)}")

    print("Title of parent page==>", all_pages[0].title())
    print("Title of child page==>", all_pages[1].title())

    child_page = all_pages[1]

    print("URL of child page==>", child_page.url)



    """
    type of events
    -----------------
    alerts/dialogs -----> dialog
    downloads files -----> download
    popups -----> popup
    tabs -----> page

    page.on()

    Assignment: go to opensource-demo.orangehrmlive.com and in bottom OrangeHRM.Inc and handle the new tab along with parent page 
    login with username and password and verify the title of the page and close the child tab and parent tab
    """

