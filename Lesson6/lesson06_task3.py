from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# driver.implicitly_wait(16)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
element = WebDriverWait (driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p#text.lead'),'Done!'))
waiting_picture = driver.find_element(By.CSS_SELECTOR, "img#award").get_attribute("src")

print(waiting_picture)
driver.quit()