
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Полный путь до драйвера Edge (msedgedriver.exe)
driver_path = r"C:\Users\Папа\Desktop\SkyPro\edgedriver_win64\msedgedriver.exe"

# Создаем объект сервиса, передавая путь до драйвера
service = Service(driver_path)

def web(data):
# Инициализация веб-драйвера с использованием указанного пути
    driver = webdriver.Edge(service=service)
    #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()       
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
   