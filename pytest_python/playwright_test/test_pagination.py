from playwright.sync_api import expect, Page
import pytest

'''
    pagination Table -  The table which have more numbers of table but we can see a limited number of records
    on a single page. If we want to see other records then we have to move other pages/set no of records dropdown(if present)
'''

@pytest.mark.skip
def test_pagination_table(page:Page):
    page.goto('https://datatables.net/examples/basic_init/zero_configuration.html')
    
    has_more_pages = True

    while has_more_pages:
        # rows = page.locator("#example tbody tr").all()
        # for r in rows:
        #     print(r.inner_text())

        nxt_btn = page.locator("button[aria-label='Next']")
        btn_is_disabled = nxt_btn.get_attribute("class")   # class="dt-paging-button last" -----> the next button is enable /// class="dt-paging-button disabled next"-----> the next button is disabled

        # Check if there is a next page button and if it is enabled
        if "disabled" in btn_is_disabled:
            has_more_pages = False
            print("\n\nAll Records fetched Successfully")
        else:
            nxt_btn.click()
            page.wait_for_timeout(4000)  # Wait for the next page to load

def test_filter_rows(page:Page):
    page.goto('https://datatables.net/examples/basic_init/zero_configuration.html')
    drpdn = page.locator('#dt-length-0')
    drpdn.select_option(label='25')

    rows = page.locator("#example tbody tr")
    expect(rows).to_have_count(25)

            