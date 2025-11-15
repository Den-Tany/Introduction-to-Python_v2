from selenium.webdriver.common.by import By


class Auth:

    def __init__(self, driver, Username, Password):
        self.driver = driver
        self.Username = Username
        self.Password = Password

    def start_Web(self):
        self.driver.maximize_window()  # Раскрыть окно на весь экран
        self.driver.get("https://www.saucedemo.com")  # перейти на страницу
        self.auth()

    def auth(self):
        # Авторизация
        field_UserName = self.driver.find_element(By.CSS_SELECTOR, 'input.input_error.form_input#user-name')
        field_UserName.send_keys(self.Username)

        field_Password = self.driver.find_element(By.CSS_SELECTOR, 'input.input_error.form_input#password')
        field_Password.send_keys(self.Password)

        self.driver.find_element(By.CSS_SELECTOR, 'input.submit-button.btn_action#login-button').click()
