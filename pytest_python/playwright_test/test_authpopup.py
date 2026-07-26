from playwright.sync_api import Page, expect,Playwright
import pytest

# Direct Approach - injectuserlogin with url

# https://the-internet.herokuapp.com/basic_auth/

#  https://admin:admin@the-internet.herokuapp.com/basic_auth  syntax for inject user login with url (not recomended)

@pytest.mark.skip
def test_authpopup(page: Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()  # wait for page to load completely
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(4000)


# using context - we can pass user name and password along with the context

def test_authpage_context(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    page= context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(4000)

def test_authpage_context_cancel(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    
    # 1. Yahan se http_credentials hata diya gaya hai
    context = browser.new_context()
    page = context.new_page()

    # 2. Route interceptor function banayein jo Auth ko cancel karega
    def cancel_auth(route):
        # 401 status return karne se popup trigger nahi hoga (Cancel jaisa behavior)
        route.fulfill(status=401, body="Not authorized")

    # 3. URL match hone par us request ko intercept karein
    page.route("**/basic_auth", cancel_auth)

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()

    # ⚠️ DHYAN DEIN: 
    # Kyunki aapne authentication cancel kar diya hai, page successfully load nahi hoga.
    # Isliye aapka purana expect statement fail ho jayega. 
    # Aap isey comment kar sakte hain ya nayi state ke hisaab se assert kar sakte hain:
    
    # expect(page.locator("div[class='example'] p")).to_be_visible() # Ye fail hoga
    
    # Check karein ki page par 'Not authorized' text aagaya hai (Optional)
    expect(page.locator("body")).to_contain_text("Not authorized")

    page.wait_for_timeout(4000)
    browser.close()

"""
from playwright.sync_api import Playwright, expect

def test_authpage_context(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Lambda function ka use karke route ko ek hi line mein intercept aur fulfill kar diya
    page.route("**/basic_auth", lambda route: route.fulfill(status=401, body="Not authorized"))

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()

    # Assertion check: Verify ki popup cancel hone ke baad page par 'Not authorized' aaya hai
    expect(page.locator("body")).to_contain_text("Not authorized")

    page.wait_for_timeout(4000)
    browser.close()

"""

def test_authpage_wrong_creds(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    
    # Jaanbuch kar galat credentials daale hain
    context = browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    page = context.new_page()

    # Interceptor function jo popup ko wapas aane se rokega
    def block_auth_reprompt(route):
        # 1. Server tak request jaane dein aur uska response fetch karein
        response = route.fetch()
        headers = dict(response.headers) 
        
        # 2. 'www-authenticate' header ko delete karein (yahi popup trigger karta hai)
        headers.pop("www-authenticate", None)
            
        # 3. Modified headers browser ko pass kar dein
        route.fulfill(response=response, headers=headers)

    # Route interceptor apply karein
    page.route("**/basic_auth", block_auth_reprompt)

    # Ab jab aap visit karenge, toh wrong credentials send honge par popup wapas nahi aayega
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()