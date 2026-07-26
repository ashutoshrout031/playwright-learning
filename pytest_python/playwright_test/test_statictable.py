from playwright.sync_api import sync_playwright,Page,expect

def test_static_web_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # 1. count the number of rows in a table

    # rows = page.locator("table[name='BookTable'] tbody tr") instead of writing whole css we have already used locator in table and we can reuse that
    rows = table.locator("tr")   # table[name='BookTable'] tbody tr
    expect(rows).to_have_count(7)
    print("Nos of rows in table is:", rows.count())

    # 2. count total nos of cols/headers in a table

    cols= rows.locator("th")  # table[name='BookTable'] tbody tr th
    expect(cols).to_have_count(4)

    print("Nos of cols in table is:", cols.count())


    # 3. Read all the data from 2nd row of this table

    # second_row_cells = rows.nth(1).locator('td')
    # second_row_text = second_row_cells.all_inner_texts()

    # print("2nd row data====>",second_row_text) #['Learn Selenium', 'Amit', 'Selenium', '300']]

    # expect(second_row_cells).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])


    # 4. Read all the data from the table (Excluding header)
    all_rows_data = rows.all()

    # print(all_rows_data)


    for r in all_rows_data[1:]:
        cols = r.locator('td').all_inner_texts()
        print(cols)

    # 5. print book names whose authore is 'Mukesh'

    # for r in all_rows_data[1:]:
    #     auth_name = r.locator('td').nth(1).inner_text()
    #     if auth_name=='Mukesh':
    #         book_name = r.locator('td').nth(0).inner_text()
    #         print(f"{auth_name}: {book_name}")

    # 6. Calculate the total price of the books

    total_price = 0
    for r in all_rows_data[1:]:
        bk_price = r.locator('td').nth(3).inner_text()
        total_price += int(bk_price)
    print("Total Price is ===>",total_price)
        







