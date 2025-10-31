from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = input("Выбери браузер: (1-Chrom, 2-Firefox) - ")
while browser not in ['1', '2']:
    print("Ошибка! Нужно выбрать '1' или '2'")
    exit(1)
def select_browser(browser):    
    if browser == '1':        
       return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == '2':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))       
driver = select_browser(browser)
driver.get("http://uitestingplayground.com/textinput")
enter_word = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
enter_word.send_keys("SkyPro")
press_button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton.btn.btn-primary").click()
textButton = driver.find_element(By.CSS_SELECTOR, "button#updatingButton.btn.btn-primary")
print(textButton.text)
driver.quit()
