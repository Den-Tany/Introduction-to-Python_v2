from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
locator_unput = "input[type='number']"
seach_input = driver.find_element(By.CSS_SELECTOR, locator_unput)
seach_input.send_keys("Sky.")
sleep(2)
seach_input.clear()
seach_input.send_keys("Pro.")

sleep(3)
driver.quit()