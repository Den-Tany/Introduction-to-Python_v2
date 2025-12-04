# test файл
import pytest
import allure
from shop.shop_03 import Shop
from shop.browser_Firefox import bro_Firefox
from shop.auth import Auth
from shop.choice import Choice
from shop.form import Form
from allure_commons.types import Severity

Username = 'standard_user'
Password = 'secret_sauce'

firstName = 'Den'
lastName = 'Tany'
ZipCode = '689000'


@allure.title("Загрузка и закрытие браузера")
@pytest.fixture(scope='module')
def test_openBrowser():
    bro = bro_Firefox()
    with allure.step("Загружается драйвер Firefox"):
        driver = bro.web()
    yield driver
    with allure.step("Закрытие браузера Firefox"):
        driver.quit()


@allure.title("""Автотест для проверки функциональности интернет-магазина
              на сайте https://www.saucedemo.com/,
              используя паттерн Page Object
              и браузер FireFox.""")
@allure.description("""
Написать тест, который использует PageObject
для выполнения следующих действий:
Открыть сайт магазина.
Авторизоваться как пользователь standard_user.
Добавить в корзину товары:
Sauce Labs Backpack.
Sauce Labs Bolt T-Shirt.
Sauce Labs Onesie.
Перейти в корзину.
Нажать кнопку Checkout.
Заполнить форму своими данными:
Имя.
Фамилия.
Почтовый индекс.
Прочитать со страницы итоговую стоимость (Total).
Закрыть браузер.
Проверить что итоговая сумма равна $58.29.
""")
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('result', [("$58.29")])
def test_time_wait(test_openBrowser, result):

    auth = Auth(test_openBrowser, Username, Password)
    auth.start_Web()

    choice = Choice(test_openBrowser)
    choice.choice()

    form = Form(test_openBrowser, firstName, lastName, ZipCode)
    form.filling_out_the_form()

    with allure.step("Проверить что итоговая сумма равна $58.29."):
        shop = Shop(test_openBrowser)
        total_coast = shop.total_cost()

        with allure.step("Сравниваем полученное значение с заданным"):
            assert result == total_coast
