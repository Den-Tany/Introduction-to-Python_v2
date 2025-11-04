
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def web(data):
# Инициализация веб-драйвера с использованием указанного пути
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))     
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")# Открываем сайт
    for locator in data:
        loc = f"input[name='{locator[0]}']"
        seach_input = driver.find_element(By.CSS_SELECTOR, loc)
        word = locator[1]
        seach_input.send_keys(word)
    
    # Ищем кнопку Submit и кликаем на неё
    search_buttot = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
    #Перематываем страницу вниз
    ActionChains(driver).move_to_element(search_buttot).perform()

    #Нажимаем на кнопку
    search_buttot.click()

    # Запрашиваем цвет текста:
    color_list = []
    for locator in data:
        loc = f"div#{locator[0]}"
        seach_color = driver.find_element(By.CSS_SELECTOR, loc).value_of_css_property("color")
        color_list.append(seach_color)
    return color_list
    driver.quit()
   