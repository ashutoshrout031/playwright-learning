import pytest
from playwright.sync_api import sync_playwright,expect,Page

@pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    pointme = page.locator(".dropbtn")

    pointme.hover()
    # approch1
    mob = page.locator(".dropdown-content a").nth(0)
    mob.hover()
    page.wait_for_timeout(3000)

    # approach2
    lap = page.locator('.dropdown-content a:nth-child(2)')
    lap.hover()
    page.wait_for_timeout(3000)
    lap.click()

    page.wait_for_timeout(3000)
    
@pytest.mark.skip
def test_mouse_rightclick(page:Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    btn = page.locator(".context-menu-one")
    btn.click(button="right")  # performs right click action - right,left, middle
    page.wait_for_timeout(3000)

def test_mouse_double_click(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    fld1 = page.locator("#field1")
    fld1.clear()
    page.wait_for_timeout(2000)
    fld1.fill("I am Ashutosh")
    page.wait_for_timeout(3000)

    btncpy = page.locator('button[ondblclick="myFunction1()"]')
    btncpy.dblclick()   # performs double click action

    page.wait_for_timeout(3000)

    field2 = page.locator('#field2')
    expect(field2).to_have_value('I am Ashutosh')

    page.wait_for_timeout(4000)

def test_mouse_drag_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    source = page.locator('#draggable')
    target = page.locator('#droppable')

    # Approach 1: Manual Drag using hover() Not recomended

    #stp 1 hover on source
    # source.hover()
    # page.wait_for_timeout(3000)
    # stp 2 mouse down( hold the click)
    # page.mouse.down()
    # page.wait_for_timeout(3000)
    # stp 3 hover on target
    # target.hover()
    # page.wait_for_timeout(3000)
    # stp 4  mouse up
    # page.mouse.up()
    # page.wait_for_timeout(3000)


    # Approach 2 drag_to()  most preferable action

    source.drag_to(target)
    page.wait_for_timeout(3000)


