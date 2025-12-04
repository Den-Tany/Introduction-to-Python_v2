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
            self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
        # Выбор Labs Bolt T-Shirt
        with allure.step("Выбор Labs Bolt T-Shirt"):
            self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
        # Выбор Sauce  Labs Onesie
        with allure.step("Выбор Sauce  Labs Onesie"):
            self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
        # Переход в корзину
        with allure.step("Переход в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link[data-test="shopping-cart-link"]').click()
        # Переход в оформление
        with allure.step("Переход в оформление"):
            button_checkout = self.driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button')
            self.driver.execute_script("arguments[0].scrollIntoView();", button_checkout)
            button_checkout.click()
