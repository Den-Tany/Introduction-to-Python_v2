from selenium.webdriver.common.by import By
import allure


class Form:

    def __init__(self, driver, firstName, lastName, ZipCode):
        self.driver = driver
        self.firstName = firstName
        self.lastName = lastName
        self.ZipCode = ZipCode

    @allure.step("Заполнение формы своими данными")
    def filling_out_the_form(self):
        """
        Заполнение формы с данными
        Имя
        Фамилие
        Индекс
        """
        # Заполнение формы
        with allure.step(
            f"Ввод значения '{self.firstName}' в поле \"firstName\""
                ):
            field_firstName = self.driver.find_element(
                By.CSS_SELECTOR, 'input#first-name'
                )
            field_firstName.send_keys(self.firstName)

        with allure.step(
            f"Ввод значения '{self.lastName}' в поле \"lastName\""
                ):
            field_lastName = self.driver.find_element(
                By.CSS_SELECTOR, 'input#last-name'
                )
            field_lastName.send_keys(self.lastName)

        with allure.step(
            f"Ввод значения '{self.ZipCode}' в поле \"self.ZipCode\""
                ):
            field_ZipCode = self.driver.find_element(
                By.CSS_SELECTOR, 'input#postal-code'
                )
            field_ZipCode.send_keys(self.ZipCode)

        with allure.step("Нажать кнопку продолжить"):
            button_continue = self.driver.find_element(
                By.CSS_SELECTOR, 'input#continue'
                )
            button_continue.click()
