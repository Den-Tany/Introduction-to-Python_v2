import pytest
from form_01 import web

# Данные для теста
# локатор, вносимые данные, результат (подсветки)
data = [
            ["first-name", 'Иван', 'rgba(15, 81, 50, 1)'],# позитив
            ["last-name", 'Петров', 'rgba(15, 81, 50, 1)'],# позитив
            ["address", 'Ленина, 55-3', 'rgba(15, 81, 50, 1)'],# позитив
            ["e-mail",'test@skypro.com', 'rgba(15, 81, 50, 1)'],# позитив
            ["phone", '+7985899998787', 'rgba(15, 81, 50, 1)'],# позитив
            ["zip-code", '', 'rgba(132, 32, 41, 1)'],# негатив
            ["city", 'Москва', 'rgba(15, 81, 50, 1)'],# позитив
            ["country", 'Россия', 'rgba(15, 81, 50, 1)'],# позитив
            ["job-position", 'QA', 'rgba(15, 81, 50, 1)'],# позитив
            ["company", 'SkyPro', 'rgba(15, 81, 50, 1)']# позитив
        ]
color_list = web(data)
print(color_list)
print(data)
# Основной тест
@pytest.mark.parametrize('index', range(len(data)))
def test_color_comparison(index):
   
    # Берем третий элемент из data (сам цвет)
    current_color = data[index][2]
    
    # Берем цвет из color_list
    expected_color = color_list[index]
    
    # Проверяем совпадение цветов
    assert current_color == expected_color


