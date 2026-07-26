from playwright.sync_api import Playwright, expect,Page
import time
import datetime

def test_screenshot_demo(page:Page):

    page.goto("https://demowebshop.tricentis.com/")
    # timestamp = str(int(time.time()))
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


    # Page Screenshot(partialy/visible)
    # page.screenshot(path=f"screenshots/homepage_{timestamp}.png")
    

    # Full page screenshot
    # page.screenshot(path=f"screenshots/fullhomepage_{timestamp}.png",full_page=True)

    # Elemnt/Specific section of the page screenshot
    # For this we need to use locator and then screenshot method

    # logo = page.locator("img[alt='Tricentis Demo Web Shop']")
    # logo.screenshot(path=f"screenshots/logo_{timestamp}.png")

    #specific section of the page screenshot
    fprod = page.locator(".product-grid.home-page-product-grid")
    fprod.screenshot(path=f"screenshots/featured_products_{timestamp}.png")
