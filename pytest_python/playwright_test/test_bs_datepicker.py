from playwright.sync_api import Page,expect


def select_chkin_date(page,trgt_yr,trgt_mnth,trgt_dt):
    while True:
        chkin_mnth_yr = page.locator("h3[class='e7addce19e af236b7586']").nth(0).inner_text()
        cur_mnth,cur_yr = chkin_mnth_yr.split(" ")
        if cur_mnth ==trgt_mnth and cur_yr ==trgt_yr:
            break
        else:
            page.locator('button[aria-label="Next month"]').click()  # go to the next month
            page.wait_for_timeout(2000)

    all_dates = page.locator("table.b8fcb0c66a").nth(0).locator('td').all()

    for dts in all_dates:
        if dts.inner_text() == trgt_dt:
            dts.click()
            page.wait_for_timeout(2000)
            break

def select_chkout_date(page,trgt_yr,trgt_mnth,trgt_dt):
    while True:
        chkout_mnth_yr = page.locator("h3[class='e7addce19e af236b7586']").nth(1).inner_text()
        cur_mnth,cur_yr = chkout_mnth_yr.split(" ")
        if cur_mnth ==trgt_mnth and cur_yr ==trgt_yr:
            break
        else:
            page.locator('button[aria-label="Next month"]').click()  # go to the next month
            page.wait_for_timeout(2000)

    all_dates = page.locator("table.b8fcb0c66a").nth(1).locator('td').all()

    for dts in all_dates:
        if dts.inner_text() == trgt_dt:
            dts.click()
            page.wait_for_timeout(2000)
            break       


def test_booking_datepicker(page:Page):
    page.goto("https://www.booking.com/")
    page.locator("button[aria-label='Select dates']").click()  # clicked on date picker
    page.wait_for_timeout(3000)


    select_chkin_date(page,"2026","October","10")
    page.wait_for_timeout(3000)
    select_chkout_date(page,"2026","Decemebr","15")


    slct_dt = "button[aria-label='Select dates'] span[class='SearchBoxTrigger_label SearchBoxTrigger_truncate']"
    chkin_out =page.locator(slct_dt).inner_text()
    print("Chek-i and Check-out Date ====>",chkin_out)

    page.wait_for_timeout(5000)




