import pytest
from playwright.sync_api import Page, expect
# IMPORT THE CORRECT FUNCTION: stealth_sync
from undetected_playwright import stealth_sync  

# @pytest.fixture(scope="function")  
# def stealth_page(page: Page, context):
#     """
#     Takes Pytest's default page and browser context, applies undetected 
#     patches via stealth_sync, and hands it over to the tests.
#     """
#     # Apply anti-bot signatures to the browser context
#     stealth_sync(context)
    
#     yield page

# --- Your Tests Remain Completely Clean ---

def test_verifyPageUrl(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    expect(page).to_have_url("https://demo.nopcommerce.com/")


def test_verify_pwlocators(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(700000) 
    
    # Locate the logo via its alt text
    logo = page.get_by_alt_text("nopCommerce demo store")
    
    # Allow 15 seconds for Cloudflare to evaluate the undetected fingerprint
    expect(logo).to_be_visible()