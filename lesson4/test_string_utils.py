import pytest
from string_utils import StringUtils


string_utils = StringUtils()

"""
В тексте делает первую букву заглавной.
Позитивные проверки:
Символы на латинице:
1. Слово начинается с прописной буквы.
2. Два слова разделены пробелом, ничанаются с прописной буквы.
3. Слово начинается с заглавной буквы.
Символы на кириллице
1. Символ строчный
"""
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",
                          [
                            ("skypro", "Skypro"),
                            ("hello world", "Hello world"),
                            ("Skypro", "Skypro"),
                            ("а", "А")
                            ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

"""
Негативные проверки.
Символы на латинице:
1. Слово начинается с цифры.
2.Не заполненная строка.
3. Слово начинается со спецсимвола.
4. Содержит только пробел.
"""
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    (".word", ".word"),
    ("   ", "   "),
    ])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

"""
Удаляет пробелы в начале, если они есть.
Позитивные проверки.
1. Пробел, слово начинается с прописной буквы.
2. Два пробела, два слова начинаются с прописной буквы.
3. Пробел, слово начинается с заглавной буквы.
4. Пробел, слово начинается с цифры.
6. Пробел, слово начинается со спецсимвола.
7. Пробел и кириллический символ.
8. Только два пробела.
"""
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",
                          [
                            (" skypro", "skypro"),
                            ("  hello world", "hello world"),
                            (" Skypro", "Skypro"),
                            (" 123abc", "123abc"),
                            (" .word", ".word"),
                            (" а", "а"),
                            ("  ", "")
                            ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected
"""
Негативные проверки.
1. Слово начинается с прописной буквы, пробел в конце.
2. Два слова начинаются с прописной буквы.
3. Слово начинается с заглавной буквы.
4. Слово начинается с цифры.
6. Слово начинается со спецсимвола.
7. Пустая строка.
8. Кириллический символ.
"""
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",
                          [
                            ("skypro ", "skypro "),
                            ("hello world", "hello world"),
                            ("Skypro", "Skypro"),
                            ("123abc", "123abc"),
                            (".word", ".word"),
                            ("", ""),
                            ("а", "а")
                            ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

"""
Поиск символа в слове.
Позитивные проверки.
1. Поиск одного существующего символа в слове.
2. Поиск существующего слова в предложении.
3. Поиск двух существующих символов в слове.
4. Поиск существующих цифр в слове.
5. Поиск существующего спецсимвола в слове.
6. Поиск кириллического символа в слове.
7. Поиск пробела.
"""
@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_simbol, expected",
                          [
                            ("skypro", "s", True),
                            ("Hello world. Its word", "word", True),
                            ("Skypro", "Sk", True),
                            ("123abc", "23", True),
                            (" .word", ".", True),
                            (" Pаpa", "а", True),
                            (" word", " ", True)
                            ])
def test_contains_positive(input_str, input_simbol, expected):
    assert string_utils.contains(input_str, input_simbol) == expected

"""
Негативные проверки.
1. Поиск одного несуществующего символа в слове.
2. Поиск несуществующего слова в предложении.
3. Поиск двух несуществующих символов в слове.
4. Поиск несуществующих цифр в слове.
5. Поиск несуществующего спецсимвола в слове.
6. Поиск несуществующего кириллического символа в слове.
7. Поиск несуществующего пробела.
"""
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_simbol, expected",
                          [
                            ("skypro", "d", False),
                            ("Hello world. Its word", "WORD", False),
                            ("Skypro", "Cdf", False),
                            ("123abc", "56", False),
                            (" .word", ",", False),
                            (" Pаpa", "А", False),
                            ("", " ", False)
                            ])
def test_contains_negative(input_str, input_simbol, expected):
    assert string_utils.contains(input_str, input_simbol) == expected

"""
Удаление символа в слове.
Позитивные проверки.
1. Удаление одного существующего символа в слове.
2. Удаление существующего слова в предложении.
3. Удаление двух существующих символов в слове.
4. Удаление существующих цифр в слове.
5. Удаление существующего спецсимвола в слове.
6. Удаление кириллического символа в слове.
7. Удаление пробела.
"""
@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_simbol, expected",
                          [
                            ("skypro", "s", "kypro"),
                            ("Hello world. Its word", "word", "Hello world. Its "),
                            ("Skypro", "Sk", "ypro"),
                            ("123abc", "23", "1abc"),
                            (" .word", ".", " word"),
                            (" Pаpa", "а", " Ppa"),
                            (" ", " ", "")
                            ])
def test_delete_symbol_positive(input_str, input_simbol, expected):
    assert string_utils.delete_symbol(input_str, input_simbol) == expected

"""
Негативные проверки.
1. Удаление одного несуществующего символа в слове.
2. Удаление несуществующего слова в предложении.
3. Удаление двух несуществующих символов в слове.
4. Удаление несуществующих цифр в слове.
5. Удаление несуществующего спецсимвола в слове.
6. Удаление несуществующего кириллического символа в слове.
7. Удаление несуществующего пробела в пустой строке.
"""
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_simbol, expected",
                           [
                             ("skypro", "d", "skypro"),
                             ("Hello world. Its word", "WORD", "Hello world. Its word"),
                             ("Skypro", "Cd", "Skypro"),
                             ("123abc", "56", "123abc"),
                             (" .word", ",", " .word"),
                             (" Pаpa", "А", " Pаpa"),
                             ("", " ", "")
                             ])
def test_delete_symbol_negative(input_str, input_simbol, expected):
     assert string_utils.delete_symbol(input_str, input_simbol) == expected