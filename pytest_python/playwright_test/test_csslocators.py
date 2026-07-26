'''
    > tag id ----> tag#id
    > tag class ---->  tag.class
    > tag attribute  -----> tag[attribute=value]
    > tag class attribute  ---->tag.class[attribute==value]

    !!!! Note -- '#' => "id", '.' => "class", '[]' => attributes !!!! All the above tag is optional !!!!

'''
# selector hub plugin install to browser



from playwright.sync_api import Page,expect

def test_verify_cssLocators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # tag id
    # page.locator("input#small-searchterms").fill("T-Shirts")
    # page.wait_for_timeout(4000)
    # or page.locator("#small-searchterms").fill("T-Shirts")  <---  You can also use this one

    # tag class 
    # page.locator("input.search-box-text").fill("FootBall")
    # or page.locator(".search-box-text").fill("FootBall")
    # page.wait_for_timeout(7000)

    # tag attribute
    page.locator("input[name=q]").fill("FootBall")
    # page.locator("[name=q]").fill("FootBall")
    page.wait_for_timeout(4000)

    # tag class attribute  ----> Sometimes if we select class it locates multiple attributes so to locate specific attribute we use this 
    page.locator("input.search-box-text[value='Search store']").fill("Car Toy")   # if you have space or multiple value the use single '' inside "" or viceversa
    # page.locator(".search-box-text[value='Search store']").fill("Car Toy") 
    page.wait_for_timeout(4000)





 
