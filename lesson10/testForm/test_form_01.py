import pytest
import allure
from allure_commons.types import Severity
from form.browser_Edge import bro_Edg
from form.form_01 import Page

"""
Скачать драйвер для браузера Edge.
В строку вместо <Путь> подставить путь расположения драйвера.
"""
path: str = r"<Путь>"
# Данные для теста
# локатор, вносимые данные, результат (подсветки)
data = [
            ["first-name", 'Иван', 'rgba(15, 81, 50, 1)'],  # позитив
            ["last-name", 'Петров', 'rgba(15, 81, 50, 1)'],  # позитив
            ["address", 'Ленина, 55-3', 'rgba(15, 81, 50, 1)'],  # позитив
            ["e-mail", 'test@skypro.com', 'rgba(15, 81, 50, 1)'],  # позитив
            ["phone", '+7985899998787', 'rgba(15, 81, 50, 1)'],  # позитив
            ["zip-code", '', 'rgba(132, 32, 41, 1)'],  # негатив
            ["city", 'Москва', 'rgba(15, 81, 50, 1)'],  # позитив
            ["country", 'Россия', 'rgba(15, 81, 50, 1)'],  # позитив
            ["job-position", 'QA', 'rgba(15, 81, 50, 1)'],  # позитив
            ["company", 'SkyPro', 'rgba(15, 81, 50, 1)']  # позитив
        ]

@pytest.fixture(scope='module')
def color_get() -> list:
    color_list = []
    bro = bro_Edg(path)
    driver = bro.web()
    page = Page(driver, data)
    page.open_web()
    page.input_form()
    page.search_Submit()
    color_list = page.get_color_list()
    driver.quit()
    return color_list

@allure.title("Заполнение формы")
@allure.severity(Severity.CRITICAL)
@allure.description(f"""Заполнение формы регистрации значениями
                    поле: '{data[0][0]}', значение - '{data[0][1]}' (позитивная проверка),
                    поле: '{data[1][0]}', значение - '{data[1][1]}' (позитивная проверка),
                    поле: '{data[2][0]}', значение - '{data[2][1]}' (позитивная проверка),
                    поле: '{data[3][0]}', значение - '{data[3][1]}' (позитивная проверка),
                    поле: '{data[4][0]}', значение - '{data[4][1]}' (позитивная проверка),
                    поле: '{data[5][0]}', значение - '{data[5][1]}' (негативная проверка),
                    поле: '{data[6][0]}', значение - '{data[6][1]}' (позитивная проверка),
                    поле: '{data[7][0]}', значение - '{data[7][1]}' (позитивная проверка),
                    поле: '{data[8][0]}', значение - '{data[8][1]}' (позитивная проверка),
                    поле: '{data[9][0]}', значение - '{data[9][1]}' (позитивная проверка).
                    При нажатии кнопки "Submit" поля заполненные валидными значениями 
                    подсвечиваются зеленым, поля заполненные невалидными значением - красным.
""")
# Основной тест
@pytest.mark.parametrize('index', range(len(data)))
def test_color_comparison(index, color_get):
    with allure.step(f"""Заданный цвет '{data[index][2]}' поля '{data[index][0]}' со значением '{data[index][1]}'
                     записываем в переменную current_color"""):
        current_color = data[index][2]
    with allure.step(f"""Полученный цвет '{color_get[index]}' поля '{data[index][0]}' со значением '{data[index][1]}'
                     записываем в переменную expected_color"""):
        expected_color = color_get[index]
    with allure.step("Проверяем совпадение цветов"):
        assert current_color == expected_color
