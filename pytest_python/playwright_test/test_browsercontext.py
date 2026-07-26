from playwright.sync_api import Playwright, Page, expect

# Browser -----> context(Own userprofile ) ----> page(s)
# When we use our own browser context we have to use Playwright Fixture not Page Fixture
def test_browsercontext(playwright:Playwright):

    # 1. Create Browser ----> chromium, firefox, webkit etc...
    # chromium = playwright.chromium 
    # browser = chromium.lunch() # this is browesr

    # in a single line
    # browser = playwright.chromium.launch() # ------> this is chromium browser google/edge
    browser = playwright.chromium.launch(headless=False) # browser created. Bydefault it is True. We need to configure to run headed mode
    # 2. Create Context
    context = browser.new_context()  # created context. we can create multiple context
    # 3. Create Page
    page1= context.new_page() # page created. we can create multiple pages
    page2 = context.new_page()
    # advantage of creating multiple page is to working parallely at a single time

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")






