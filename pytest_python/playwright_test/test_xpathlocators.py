import pytest

from playwright.sync_api import Page,expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # 1. Abaolute xpath(full form)
    # //html/body/div[4]/div[1]/div[1]/div[1]/a/img -- It starts from the root node (not reliable) !! Not Recommednded
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    # 2. Relative xpath: //tagname[@attribute='value'] -- direct jumps to the locator (most reliable)

    # //img[@alt="Tricentis Demo Web Shop"]
    expect(page.locator('//img[@alt="Tricentis Demo Web Shop"]')).to_be_visible()
    

    expect(page.locator('//img[@alt="Tricentis Demo Web Shop"]')).to_be_visible()
    page.wait_for_timeout(5000)

    # 3. xpath with contains()  used mostly to handle dynamic pages/locators
    products = page.locator("//h2//a[contains(@href,'computer')]")  # locator never return anything as collection
    print("Products count:", products.count())
    expect(products).to_have_count(4) # if you know no of counts then put concrete value or product.count() 
    page.wait_for_timeout(4000)

    # capture 1st element
    # print("First Computer Product",products.first.text_content())

    # capture last element 
    # print("Last Computer product:",products.last.text_content())

    # capture nth element
    # print("Nth computer product:", products.nth(2).text_content()) #nth() starts from 0

    # all_text_contents()
    # product_titles = products.all_text_contents()   # all_text_contents() returns list
    # print("Product titles --->",product_titles)

    # print("Printing Product Titles........")
    # for i in product_titles:
    #     print(i)

    # 4. xpath with starts-with()
    # buld_products = page.locator("//h2//a[starts-with(@href,'/build')]")  --- refers to the attribute name
    # print("Count of Bulid products:", buld_products.count())

    # expect(buld_products).to_have_count(buld_products.count())

    # 5. xpath with text()  --- represents the innertext  

    registration_link = page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()

    # 6. xpath with last()
    gplus_link= page.locator("//div[@class='column follow-us']//li[last()]")
    expect(gplus_link).to_have_text("Google+")


    # 7. xpath wiht position()

    twiter_link =page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twiter_link).to_have_text("Twitter")



