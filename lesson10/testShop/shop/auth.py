from selenium.webdriver.common.by import By
import allure


class Auth:

    def __init__(self, driver, Username, Password):
        self.driver = driver
        self.Username = Username
        self.Password = Password

    @allure.step("Открытие сайта")
    def start_Web(self):
        """
        Раскрыть окно на весь экран.
        Перейти на страницу.
        """
        self.driver.maximize_window()  # Раскрыть окно на весь экран
        self.driver.get("https://www.saucedemo.com")  # перейти на страницу
        self.auth()

    @allure.step("Авторизация на сайте")
    def auth(self):
        """
        Авторизация.
        Ввод логина.
        Ввод пароля.
        Нажать кнопку \"Login\".
        """
        # Авторизация
        with allure.step(f"Ввод логина '{self.Username}'"):
            field_UserName = self.driver.find_element(By.CSS_SELECTOR, 'input.input_error.form_input#user-name')
            field_UserName.send_keys(self.Username)

        with allure.step(f"Ввод пароля '{self.Password}'"):
            field_Password = self.driver.find_element(By.CSS_SELECTOR, 'input.input_error.form_input#password')
            field_Password.send_keys(self.Password)

        with allure.step(f"Нажать кнопку \"Login\""):
            self.driver.find_element(By.CSS_SELECTOR, 'input.submit-button.btn_action#login-button').click()
