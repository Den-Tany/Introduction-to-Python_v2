from selenium import webdriver # импортировать веб драйвер
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()# Раскрыть окно на весь экран
driver.get("http://uitestingplayground.com/dynamicid")# перейти на страницу
find_button = ".btn-primary" #задать локатор
search_button = driver.find_element(By.CSS_SELECTOR, find_button)# найти локатор
search_button.click()# кликнуть левой кнопкой мышки по элемету
sleep(5)

