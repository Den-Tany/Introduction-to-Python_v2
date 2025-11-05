from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Calc:

    def __init__(self, inTime):
        self.inTime = inTime
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def web(self):
        self.driver.maximize_window()  # Раскрыть окно на весь экран
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # перейти на страницу
        find_waitsSec = self.driver.find_element(By.CSS_SELECTOR, "#delay")  # ищем поле ввода времени задержки
        find_waitsSec.clear()  # очистка поля ввода времени задержки
        find_waitsSec.send_keys(self.inTime)  # ввод времени задержки
        self.driver.find_element(By.CSS_SELECTOR, "span.clear").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][contains(text(),'7')]").click()
        self.driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success'][contains(text(),'+')]").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][contains(text(),'8')]").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning'][contains(text(),'=')]").click()

    def time_Wait(self):
        start_time = time.time()  # начало отсчета времени
        WebDriverWait(self.driver, self.inTime+1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span#spinner[style="display: none;"]')))
        end_time = time.time()  # окончание отсчета времени
        timeWait = int(end_time - start_time)
        return timeWait

    def Quit(self):
        self.driver.quit()
