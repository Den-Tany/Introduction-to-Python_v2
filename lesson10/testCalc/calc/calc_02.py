from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


class Calc:

    def __init__(self, driver, inTime):
        self.inTime: int = inTime
        self.driver = driver

    def web(self):
        """
            Открывает окно браузера на весь экран.
            Переходит на страницу.
            Ввод времени задержки.
            Нажатие на кнопки 7, +, 8, =.
        """
        with allure.step("Загрузить страницу"):
            self.driver.maximize_window()  # Раскрыть окно на весь экран
            # перейти на страницу
            self.driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
                )
        with allure.step("Поиск поля ввода времени задержки"):
            # ищем поле ввода времени задержки
            find_waitsSec = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        with allure.step("Ввод времени задержки"):
            find_waitsSec.clear()  # очистка поля ввода времени задержки
            find_waitsSec.send_keys(self.inTime)  # ввод времени задержки
            self.driver.find_element(By.CSS_SELECTOR, "span.clear").click()
        with allure.step("Нажать кнопку \"7\""):
            D = """
            //span[@class='btn btn-outline-primary']
            [contains(text(),'7')]
            """
            self.driver.find_element(By.XPATH, D).click()
        with allure.step("Нажать кнопку \"+\""):
            C = """
            //span[@class='operator btn btn-outline-success']
            [contains(text(),'+')]
            """
            self.driver.find_element(By.XPATH, C).click()
        with allure.step("Нажать кнопку \"8\""):
            B = """
            //span[@class='btn btn-outline-primary'][contains(text(),'8')]
            """
            self.driver.find_element(By.XPATH, B).click()
        with allure.step("Нажать кнопку \"=\""):
            A = """
            //span[@class='btn btn-outline-warning'][contains(text(),'=')]
            """
            self.driver.find_element(By.XPATH, A).click()

    def time_Wait(self) -> int:
        """
        Запуск и останов таймера.
        Расчет времени ожидания.
        """
        with allure.step("Старт таймера"):
            start_time = time.time()  # начало отсчета времени
            M = 'span#spinner[style="display: none;"]'
            WebDriverWait(
                self.driver, self.inTime+1
                ).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, M)))
        with allure.step("Стоп таймера"):
            end_time = time.time()  # окончание отсчета времени
        with allure.step("Расчет времени ожидания"):
            timeWait = int(end_time - start_time)
        return timeWait
