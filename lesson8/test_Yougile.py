import pytest
from auth_Yougile import Auth
from add_Projekt_Yougile import addProjekt
from get_Projekt_Yougile import getProjekt
from change_Projekt_Yougile import changeProjekt

"""
Для выполения теста необходимо пройти процедуру регистрации на сайте
https://ru.yougile.com.

"""
data = {
        'login': ' ',  # Ввести логин, указанный при регистрации
        'password': ' ',  # Ввести пароль, указанный при регистрации
        'name': ' '  # Ввести название компании, указанное при регистрации
    }
basUrl = 'https://ru.yougile.com/api-v2/'


# Аутентификация
@pytest.fixture(scope='module')
def result_auth():
    auth = Auth(data, basUrl)

    # получение ID компании
    res = auth.auth()
    idCompani = res.json()['content'][0]['id']

    # Получение API ключа
    res = auth.get_Keys(idCompani)
    apiKey = res.json()[3]['key']

    # Получение ID администратора
    id_Admin = auth.get_List_Employees(apiKey)
    idAdmin = id_Admin.json()['content'][0]['id']
    return {'apiKey': apiKey, 'idAdmin': idAdmin, 'idCompani': idCompani}


"""
Запрос проектов
"""


@pytest.mark.positiv_test
def test_getProgekt_positiv(result_auth):
    nameProjekt = 'Кошки'
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)
    res_add = projekt.add_Projekt()

    try:
        # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 201, f"Что то пошло не так: {res_add.status_code}"
        idProjekt = res_add.json()['id']  # Запрос id проекта
    except AssertionError as err:
        pytest.fail(str(err))

    # Отправка запроса на наличие проектов
    apiKey = result_auth['apiKey']
    get_projekt = getProjekt(basUrl, apiKey, idProjekt)
    res_getProgekt = get_projekt.getProgekt()

    try:

        # Проверяем, что запрос выполнен верно
        assert res_getProgekt.status_code == 200, f"Что то пошло не так: {res_getProgekt.status_code}"
        get_idProjekt = res_getProgekt.json()['id']
        assert idProjekt == get_idProjekt, f"Вызван неверный id проекта. Должен быть {res_getProgekt}"
    except AssertionError as err:
        pytest.fail(str(err))


"""
Тест добавление проекта
"""


@pytest.mark.positiv_test
def test_addProjekt_positiv(result_auth):
    nameProjekt = 'Кошки'
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)  # Проверяем успешное создание нового проекта.
    res_add = projekt.add_Projekt()

    try:
        # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 201, f"Что то пошло не так: {res_add.status_code}"
        idProjekt = res_add.json()['id']  # Запрос id проекта
    except AssertionError as err:
        pytest.fail(str(err))

    # Отправка запроса на окончательное наличие проектов
    apiKey = result_auth['apiKey']
    get_projekt = getProjekt(basUrl, apiKey, idProjekt)
    res_getProgekt = get_projekt.getProgekt()

    try:
        # Проверяем, что запрос выполнен верно
        assert res_getProgekt.status_code == 200, f"Что то пошло не так: {res_getProgekt.status_code}"
        get_idProjekt = res_getProgekt.json()['id']
        assert idProjekt == get_idProjekt, f"Вызван неверный id проекта. Должен быть {idProjekt}"
    except AssertionError as err:
        pytest.fail(str(err))


"""
Тест изменение проекта
"""


@pytest.mark.positiv_test
def test_changeProjekt_positiv(result_auth):
    nameProjekt = 'Кошки'
    new_nameProjekt = 'Собаки'
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)
    res_add = projekt.add_Projekt()
    try:
        # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 201, f"Что то пошло не так: {res_add.status_code}"
        idProjekt = res_add.json()['id']  # Запрос id проекта
    except AssertionError as err:
        pytest.fail(str(err))
    # Изменение названия проекта
    change_projekt = changeProjekt(basUrl, new_nameProjekt, result_auth, idProjekt)
    res_change = change_projekt.change_Projekt()

    # Проверяем успешность операции
    try:

        assert res_change.status_code == 200, f"Проект не создан. Статус-код: {res_change.status_code}"
        new_idProjekt = res_change.json()['id']
        assert idProjekt == new_idProjekt, f"Проект не изменен. Id проекта должен быть {new_idProjekt}"
    except AssertionError as err:
        pytest.fail(str(err))


"""
Запрос проектов
"""


@pytest.mark.negativ_test
def test_getProgekt_negativ(result_auth):
    nameProjekt = 'Кошки'
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)
    res_add = projekt.add_Projekt()
    try:
        # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 201, f"Что то пошло не так: {res_add.status_code}"
    except AssertionError as err:
        pytest.fail(str(err))
    # Отправка запроса на наличие проектов
    apiKey = result_auth['apiKey']
    get_projekt = getProjekt(basUrl, apiKey, apiKey)  # Неверное значение id проекта
    res_getProgekt = get_projekt.getProgekt()
    try:
        # Проверяем, что запрос выполнен верно
        assert res_getProgekt.status_code == 404, f"Что то пошло не так: {res_getProgekt.status_code}"
    except AssertionError as err:
        pytest.fail(str(err))


@pytest.mark.negativ_test
def test_addProjekt_negativ(result_auth):
    nameProjekt = ''  # Название проекта не содержит значений
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)  # Проверяем успешное создание нового проекта.
    res_add = projekt.add_Projekt()

    try:
        # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 400, f"Что то пошло не так: {res_add.status_code}"
    except AssertionError as err:
        pytest.fail(str(err))


"""
Тест изменение проекта
"""


@pytest.mark.negativ_test
def test_changeProjekt_negativ(result_auth):
    nameProjekt = 'Кошки'
    new_nameProjekt = ''  # Название проекта не содержит значений
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)
    res_add = projekt.add_Projekt()
    try:
        # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 201, f"Что то пошло не так: {res_add.status_code}"
        idProjekt = res_add.json()['id']  # Запрос id проекта

    except AssertionError as err:
        pytest.fail(str(err))
    # Изменение названия проекта
    change_projekt = changeProjekt(basUrl, new_nameProjekt, result_auth, idProjekt)
    res_change = change_projekt.change_Projekt()
    # Проверяем успешность операции

    try:
        assert res_change.status_code == 400, f"Проект не создан. Статус-код: {res_change.status_code}"
    except AssertionError as err:
        pytest.fail(str(err))
