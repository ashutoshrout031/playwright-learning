# from playwright.sync_api import Page, expect
# to run async in python you have to install below plugins
'''
    --> anyio
    --> pytest-asyncio (most popular)
    --> pytest-tornasync
    --> pytest-trio
    --> pytest-twisted

'''

from playwright.async_api import async_playwright, Page,expect  # Async API
import pytest



# When use async_api must use async keyword before function name
@pytest.mark.asyncio
async def test_verifyPageUrl(): # In async we should not pass page:Page as function parameter
    # we have to create customize async function. can't write statements directly like sync approach
    async with async_playwright() as p:  # p is the asilas you can specify as you like. async_playwright is builtin method

        browser = await p.firefox.launch(headless=False)  #we have to specify the browser with await to fulfil the promise
        context = await browser.new_context()
        mypage = await context.new_page()
        await mypage.goto("https://www.saucedemo.com",wait_until="domcontentloaded")
        myurl = mypage.url
        print(f"Url of the application:{myurl}")
        await expect(mypage).to_have_url("https://www.saucedemo.com/") 
        await context.close()
        await browser.close()




# def test_verifyTitile(page:Page):
#     page.goto("https://www.saucedemo.com")

#     myTitle = page.title()
#     print(f"Title of the page: {myTitle}")
#     expect(page).to_have_title("Swag Labs")
