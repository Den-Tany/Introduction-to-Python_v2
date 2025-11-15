from selenium.webdriver.common.by import By


class Form:

    def __init__(self, driver, firstName, lastName, ZipCode):
        self.driver = driver
        self.firstName = firstName
        self.lastName = lastName
        self.ZipCode = ZipCode

    def filling_out_the_form(self):
        # Заполнение формы
        field_firstName = self.driver.find_element(By.CSS_SELECTOR, 'input#first-name')
        field_firstName.send_keys(self.firstName)

        field_lastName = self.driver.find_element(By.CSS_SELECTOR, 'input#last-name')
        field_lastName.send_keys(self.lastName)

        field_ZipCode = self.driver.find_element(By.CSS_SELECTOR, 'input#postal-code')
        field_ZipCode.send_keys(self.ZipCode)

        button_continue = self.driver.find_element(By.CSS_SELECTOR, 'input#continue')
        button_continue.click()
