from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

lokator_userName="input#username"

seach_userName=driver.find_element(By.CSS_SELECTOR, lokator_userName)
seach_userName.send_keys("tomsmith")

lokator_password="input#password"
seach_password=driver.find_element(By.CSS_SELECTOR, lokator_password)
seach_password.send_keys("SuperSecretPassword!")

lokator_button="button.radius"
seach_button=driver.find_element(By.CSS_SELECTOR, lokator_button)
seach_button.click()

lokator_message="//div[@id='flash'][@class='flash success']"
seach_message=driver.find_element(By.XPATH, lokator_message)
print(seach_message.text)

sleep(2)
driver.quit()