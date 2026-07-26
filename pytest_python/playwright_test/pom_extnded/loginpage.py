from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_link = self.page.locator("#login2")
        self.username_input = self.page.locator("#loginusername")
        self.password_input = self.page.locator("#loginpassword")
        self.login_button = self.page.locator("button[onclick='logIn()']")

# action Methods
    def login(self):
        self.login_link.click()

    def enter_username(self, username):
        self.username_input.fill("")  # clears the input field before entering the username
        self.username_input.fill(username)
    
    def enter_password(self,password):
        self.password_input.fill("")
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def perform_login(self,username,password):
         self.username_input.fill("")  # clears the input field before entering the username
         self.username_input.fill(username)
         self.password_input.fill("")
         self.password_input.fill(password)
         self.login_button.click()

    