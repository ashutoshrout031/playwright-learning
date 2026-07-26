from playwright.sync_api import expect, Page
import pytest

@pytest.mark.skip
def test_upload_single_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # Add your file upload test logic here
    page.locator("#singleFileInput").set_input_files("uploads\sample1.txt")
    page.wait_for_timeout(4000)
    page.locator("button:has-text('Upload Single File')").click()
    page.wait_for_timeout(4000)
    msg = page.locator('#singleFileStatus')

    expect(msg).to_contain_text('sample1.txt')

    print("File uploaded Successfully..............")
    page.wait_for_timeout(4000)


def test_upload_multiple_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # Add your file upload test logic here
    files = ["uploads\sample1.txt","uploads\samp2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.wait_for_timeout(4000)
    page.locator("button:has-text('Upload Multiple File')").click()
    page.wait_for_timeout(4000)
    

    # validation
    msg = page.locator('#multipleFilesStatus')

    expect(msg).to_contain_text('sample1.txt')
    expect(msg).to_contain_text('samp2.txt')

    print("Files uploaded Successfully..............")
    page.wait_for_timeout(4000)



# Assignment - https://davidwalsh.name/demo/multiple-file-upload.php


    