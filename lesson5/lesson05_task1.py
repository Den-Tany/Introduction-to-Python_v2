from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Создаем объект сервиса, передавая путь до драйвера
#service = Service(driver_path)

# Инициализация веб-драйвера с использованием указанного пути
#driver = webdriver.Edge(service=service)

driver.maximize_window()# Раскрыть окно на весь экран
driver.get("http://uitestingplayground.com/classattr")# перейти на страницу
find_button = ".btn-primary"
search_button = driver.find_element(By.CSS_SELECTOR, find_button)
search_button.click()
sleep(5)

