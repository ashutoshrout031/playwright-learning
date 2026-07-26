from playwright.async_api import Page

from playwright.sync_api import expect

def test_comparison_of_methods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")

    # 1. inner_text() vs test_content()

    # print("Using iiner_text()====>",products.nth(1).inner_text())   # Gets exact text
    # print("Using text_content====>",products.nth(1).text_content())  # Captures the content but includes hidden items, blank spaces/ so we use strip

    # count = products.count()

    # for i in range(count):
        # print("Using iiner_text()====>",products.nth(1).inner_text())   
        # prd_nm = products.nth(i).text_content()
        # prd_nm = products.nth(i).inner_text()
        # print(prd_nm.strip())


    # 2. all_inner_text() vs all_text_contents()

    # prd_nm = products.all_inner_texts()
    # prd_nm = products.all_text_contents()   # captured all things alongs with special caharctes, hidden items
    # trimmed_prd = [text.strip() for text in prd_nm]
    # print(trimmed_prd)

    # 3. all()
    prd_lc = products.all()
    print(prd_lc)
    print(prd_lc[0].inner_text())