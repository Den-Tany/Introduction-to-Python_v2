from selenium.webdriver.common.by import By
import allure


class Choice:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Выбор товаров, переход в карзину")
    def choice(self):
        """
            Выбор товаров, переход в карзину.
        """
        # Выбор Sauce Labs Backpack
        with allure.step("Выбор Sauce Labs Backpack"):
            D = 'button#add-to-cart-sauce-labs-backpack'
            self.driver.find_element(By.CSS_SELECTOR, D).click()
        # Выбор Labs Bolt T-Shirt
        with allure.step("Выбор Labs Bolt T-Shirt"):
            G = 'button#add-to-cart-sauce-labs-bolt-t-shirt'
            self.driver.find_element(By.CSS_SELECTOR, G).click()
        # Выбор Sauce  Labs Onesie
        with allure.step("Выбор Sauce  Labs Onesie"):
            H = 'button#add-to-cart-sauce-labs-onesie'
            self.driver.find_element(By.CSS_SELECTOR, H).click()
        # Переход в корзину
        with allure.step("Переход в корзину"):
            K = 'a.shopping_cart_link[data-test="shopping-cart-link"]'
            self.driver.find_element(By.CSS_SELECTOR, K).click()
        # Переход в оформление
        with allure.step("Переход в оформление"):
            L = 'button#checkout.btn.btn_action.btn_medium.checkout_button'
            button_checkout = self.driver.find_element(By.CSS_SELECTOR, L)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", button_checkout
                )
            button_checkout.click()
