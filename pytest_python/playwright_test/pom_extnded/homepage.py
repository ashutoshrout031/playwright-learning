from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page = page

        #css selector targeting all the product links under the product cards
        self.products_list_locator = "div#tbodyid div.card h4.card-title a"
        
        # 'Add to cart' button (exact match using text)
        self.add_to_cart_button = self.page.locator('a:has-text("Add to cart")')

        # Cart link in the top menu
        self.cart_link = page.locator('#cartur')

    def add_product_to_cart(self,product_name:str):
        target_product = self.page.locator(self.products_list_locator).filter(has_text=product_name)
        
        # 2. Click karein
        target_product.click()

        # 3. Dialog (alert) accept karne ka logic trigger hone se pehle likhein
        self.page.on("dialog", lambda dialog: dialog.accept())  
        
        # 4. Ab "Add to cart" par click karein
        self.add_to_cart_button.click()

    def goto_cart(self):
        self.cart_link.click()