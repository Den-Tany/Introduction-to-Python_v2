import pytest
import allure
from calc.calc_02 import Calc
from calc.browser_Chrome import bro_Chrome
from allure_commons.types import Severity


@allure.title("Загрузка и закрытие браузера")
@pytest.fixture(scope='module')
def test_openBrowser():
    bro = bro_Chrome()
    with allure.step("Загрузка драйвера \"Chrome\""):
        driver = bro.web()
    yield driver
    with allure.step("Закрытие браузера \"Chrome\""):
        driver.quit()


@allure.title("""Aвтотест для проверки функциональности калькулятора
              на сайте
              https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html,
              используя браузер Google Chrome.""")
@allure.description("""
Написать тест для выполнения следующих действий:
Открыть страницу калькулятора.
Ввести значение
45 в поле задержки.
Нажать кнопки:
7, +, 8, =.
Проверить (assert), что в окне отобразится результат
15 через 45 секунд.
                    """)
@allure.severity(Severity.MINOR)
@pytest.mark.parametrize('inTime, result', [(45, 45)])
def test_time_wait(test_openBrowser, inTime, result):
    calc = Calc(test_openBrowser, inTime)
    with allure.step("Ввод данных"):
        calc.web()
    with allure.step("Расчет времени ожидания"):
        res = calc.time_Wait()
    with allure.step("Сравнение полученного результата с заданным"):
        assert result == res
