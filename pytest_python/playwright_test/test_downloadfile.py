import pytest
import os

from playwright.sync_api import expect, Page

def test_download_file(page:Page):

    page.goto('https://testautomationpractice.blogspot.com/p/download-files_25.html')
    data = 'Hello!\n Welcome to python playwright'
    page.locator('#inputText').fill(data)
    page.wait_for_timeout(2000)
    # page.locator('#inputText').clear()

    
    page.locator('#generateTxt').click()   # this will generate a link to download text file
    page.wait_for_timeout(2000)

    # registering the download event
    
    # Approach1
    # def handle_download(download):
        # Save the downloaded file to a specific path
    #     download.save_as('downloads/sampledwn_file1.txt')
    #     print(f"File downloaded to: {download.path()}")

    # page.on('download', handle_download)


    # Approach 2: lambda
    page.on('download',lambda download: download.save_as('download_files/samp1_dwn.txt'))
    page.locator('#txtDownloadLink').click()
    page.wait_for_timeout(4000)

    if os.path.exists("download_files/samp1_dwn.txt"):
        print("File is exists")
    else:
        print("File doesn't Exist")






    # Direct Approach (File may/ may not be downloaded)
    # page.locator('#txtDownloadLink').click()
    # page.wait_for_timeout(4000)
