import pytest

from playwright.sync_api import Page,expect

@pytest.fixture(scope="function")
def url_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(4000)
    yield page


def test_setup(url_page:Page):
    url_page.locator("ul.list a[href='/books']").click()
    url_page.wait_for_timeout(2000)
    
def test_2(url_page:Page):
    url_page.locator('h2.product-title a[href="/computing-and-internet"]').click()
    url_page.wait_for_timeout(3000)

def test_3(url_page:Page):
    mn = url_page.locator("h1[itemprop$='name']").all_inner_texts()
    print(mn)
