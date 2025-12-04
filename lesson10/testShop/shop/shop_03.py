# shop_03.py
from selenium.webdriver.common.by import By
import allure


class Shop:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Читаем со страницы итоговую стоимость (Total)")
    def total_cost(self) -> str:
        """
            Читаем со страницы итоговую стоимость (Total)
        """
        total_cost_element = self.driver.find_element(By.XPATH, "//div[@class='summary_total_label' and @data-test='total-label']")
        text = total_cost_element.text
        price = text.split(':')[-1].strip()  # Отсекаем слово "Total:" и получаем чистую стоимость
        return price
