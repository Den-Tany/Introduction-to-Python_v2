from selenium.webdriver.common.by import By


class Choice:

    def __init__(self, driver):
        self.driver = driver

    def choice(self):
        # Выбор Sauce Labs Backpack
        self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
        # Выбор Labs Bolt T-Shirt
        self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
        # Выбор Sauce  Labs Onesie
        self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
        # Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link[data-test="shopping-cart-link"]').click()
        # Переход в оформление
        button_checkout = self.driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button')
        self.driver.execute_script("arguments[0].scrollIntoView();", button_checkout)
        button_checkout.click()
