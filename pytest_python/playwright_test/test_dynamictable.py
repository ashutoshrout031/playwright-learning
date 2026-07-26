from playwright.sync_api import sync_playwright,Page,expect


def test_dynamic_web_table(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table/")

    # Locating the table
    tble = page.locator("table.table tbody")

    # Get all rows from the table
    rows = tble.locator('tr').all()

    cpu_load = ''
    for r in rows:
        pname = r.locator('td').nth(0).inner_text() #browser_nane
        if pname=='Chrome':
            cpu_load = r.locator("td:has-text('%')").inner_text()
            print("CPU Load of Chrome:",cpu_load)
            break

    expect(page.locator('#chrome-cpu')).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)


# Assignment of testautomationpractice.blogspot.com Dynamic table



