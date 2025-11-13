from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Page:
    def __init__(self, driver, data):
        self.driver = driver
        self.data = data

    def open_web(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")  # Открываем сайт

    def input_form(self):
        for locator in self.data:
            loc = f"input[name='{locator[0]}']"
            seach_input = self.driver.find_element(By.CSS_SELECTOR, loc)
            word = locator[1]
            seach_input.send_keys(word)

    def search_Submit(self):
        # Ищем кнопку Submit и кликаем на неё
        search_buttot = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
        # Перематываем страницу вниз
        ActionChains(self.driver).move_to_element(search_buttot).perform()
        # Нажимаем на кнопку
        search_buttot.click()

    def get_color_list(self):
        # Запрашиваем цвет текста:
        color_list = []
        for locator in self.data:
            loc = f"div#{locator[0]}"
            seach_color = self.driver.find_element(By.CSS_SELECTOR, loc).value_of_css_property("color")
            color_list.append(seach_color)
        return color_list
