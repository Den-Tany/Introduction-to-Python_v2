# shop_03.py
from selenium.webdriver.common.by import By
class Shop:
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    def startWeb(self):
        
        self.driver.maximize_window()# Раскрыть окно на весь экран

        self.driver.get("https://www.saucedemo.com")# перейти на страницу
    def auth(self):
        # Авторизация
        field_UserName = self.driver.find_element(By.CSS_SELECTOR, 'input.input_error.form_input#user-name')
        field_UserName.send_keys('standard_user')

        field_Password = self.driver.find_element(By.CSS_SELECTOR, 'input.input_error.form_input#password')
        field_Password.send_keys('secret_sauce')

        button_login = self.driver.find_element(By.CSS_SELECTOR, 'input.submit-button.btn_action#login-button').click()
    def choice(self):
        # Выбор Sauce Labs Backpack
        button_SauceLabsBackpack = self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
        # Выбор Labs Bolt T-Shirt
        button_LabsBoltTShirt = self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
        # Выбор Sauce  Labs Onesie
        button_SauceLabsOnesie = self.driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()

        #Переход в корзину
        button_basket = self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link[data-test="shopping-cart-link"]').click()

        #Переход в оформление
        button_checkout = self.driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button')
        self.driver.execute_script("arguments[0].scrollIntoView();", button_checkout)
        button_checkout.click()
    def filling_out_the_form(self):
        #Заполнение формы
        field_firstName = self.driver.find_element(By.CSS_SELECTOR, 'input#first-name')
        field_firstName.send_keys('Den')

        field_lastName = self.driver.find_element(By.CSS_SELECTOR, 'input#last-name')
        field_lastName.send_keys('Tany')

        field_ZipCode = self.driver.find_element(By.CSS_SELECTOR, 'input#postal-code')
        field_ZipCode.send_keys('689000')

        #Нажать кнопку Сontinue
        button_continue = self.driver.find_element(By.CSS_SELECTOR, 'input#continue')
        button_continue.click()
    def total_cost(self):
        # Прочитать итоговую стоимость
        # total_cost = self.driver.find_element(By.XPATH, "//div[@class='summary_total_label' and @data-test='total-label']").text
        # return total_cost

        total_cost_element = self.driver.find_element(By.XPATH, "//div[@class='summary_total_label' and @data-test='total-label']")
        text = total_cost_element.text
        price = text.split(':')[-1].strip()  # Отсекаем слово "Total:" и получаем чистую стоимость
        return price
    def quit(self):
        self.driver.quit()