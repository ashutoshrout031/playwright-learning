from playwright.sync_api import sync_playwright,Page,expect


def select_date(page,trgt_yr,trgt_mnth,trgt_dt,is_ft):

    # select month and date from the date picker
    while True:
        cur_mnth = page.locator('.ui-datepicker-month').text_content()
        cur_yr = page.locator('.ui-datepicker-year').text_content()
        if cur_mnth == trgt_mnth  and cur_yr == trgt_yr:
            break
        if is_ft == True:
            page.locator(".ui-datepicker-next").click()  # for future date
        else :
            page.locator('.ui-datepicker-prev').click()
    all_dates = page.locator(".ui-datepicker-calendar td").all()
                                                                                                                              
    # select date from date picker
    for d in all_dates:
        dt_txt= d.inner_text()
        if (dt_txt == trgt_dt):
            d.click()
            page.wait_for_timeout(3000)
            break
    


        


def test_jquery_datepicker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    dt_inpt = page.locator("#datepicker")

    # 1. Approach 1 :
    # dt_inpt.fill("06/14/2026")

    # expect(dt_inpt).to_have_value("06/14/2026")  #mm/dd/yyyy

    # page.wait_for_timeout(4000)


    # 2. Approach 2: Use of function

    # is_future = True
    is_future = False
    yr = "2023"
    mth = "October"
    day = "15"
    dt_inpt.click()  # opens datepicker
    select_date(page,yr,mth,day,is_future)
    print("Selected Date ====>",dt_inpt.input_value())

    # expect(dt_inpt).to_have_value("10/15/2025")



