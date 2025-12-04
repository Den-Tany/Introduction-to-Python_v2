from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure


class Page:
    def __init__(self, driver, data):
        self.driver = driver
        self.data: list = data

    def open_web(self):
        """
            Открываем сайт
        """
        with allure.step("Открываем сайт"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def input_form(self):
        """
        Поиск полей.
        Заполнение полей значениями из списка data
        """
        with allure.step("Заполняем поля данными"):
            for locator in self.data:
                loc = f"input[name='{locator[0]}']"
                seach_input = self.driver.find_element(By.CSS_SELECTOR, loc)
                word = locator[1]
                seach_input.send_keys(word)

    def search_Submit(self):
        """
            Поиск и нажатие на кнопку Submit
        """
        with allure.step("Ищем кнопку Submit"):
            M = "button.btn.btn-outline-primary.mt-3"
            search_buttot = self.driver.find_element(By.CSS_SELECTOR, M)
        with allure.step("Перематываем страницу вниз"):
            ActionChains(self.driver).move_to_element(search_buttot).perform()
        with allure.step("Нажимаем на кнопку"):
            search_buttot.click()

    def get_color_list(self) -> list:
        """
            Запрашиваем цвет текста
            Составляем список значений цвета каждого поля
        """
        with allure.step("""
            Запрашиваем цвет текста
            Составляем список значений цвета каждого поля
        """):
            color_list = []
            for locator in self.data:
                loc = f"div#{locator[0]}"
                seach_color = self.driver.find_element(
                    By.CSS_SELECTOR, loc).value_of_css_property("color")
                color_list.append(seach_color)
            return color_list
