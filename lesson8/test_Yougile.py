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
        'login': 'internalclarice@freesourcecodes.com',
        'password': '4312Nfnz.',
        'name': 'Поток 107.2'    
    }
basUrl = 'https://ru.yougile.com/api-v2/'
nameProjekt = 'Кошки'
new_nameProjekt = 'Собаки'

# Аутентификация
@pytest.fixture(scope='module')
def result_auth():
    # auth = Auth(data, basUrl)

    # # получение ID компании
    # res = auth.auth()
    # idCompani = res.json()['content'][0]['id']

    # # Получение API ключа
    # res = auth.get_Keys(idCompani)
    # apiKey = res.json()[3]['key']

    # # Получение ID администратора
    # id_Admin = auth.get_List_Employees(apiKey)
    # idAdmin = id_Admin.json()['content'][0]['id']

    idAdmin = '18737704-43c0-4b3a-aca1-8d0606429e3b'
    apiKey = 'zi2slm9JX6GwgDw2MfSMm5ToZJczZyuHnaDKtzA3p5eAU2YlFYsOiReoespjLXJk'
    idCompani = '10e95965-f26a-4496-9a30-2fb981e482fa'

    return {'apiKey': apiKey, 'idAdmin': idAdmin, 'idCompani': idCompani}


"""
Запрос проектов
"""
@pytest.mark.positiv_test
def test_getProgekt_positiv(result_auth):
     # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)
    res_add = projekt.add_Projekt()
    idProjekt = res_add.json()['id'] # Запрос id проекта

    # Отправка запроса на наличие проектов
    apiKey = result_auth['apiKey']
    get_projekt = getProjekt(basUrl, apiKey, idProjekt)
    res_getProgekt = get_projekt.getProgekt()
    get_idProjekt = res_getProgekt.json()['id']
    try:
        
        # Проверяем, что запрос выполнен верно
        assert res_getProgekt.status_code == 200, f"Что то пошло не так: {res_getProgekt.status_code}"
        assert idProjekt == get_idProjekt, f"Вызван неверный id проекта. Должен быть {res_getProgekt}"
    except AssertionError as err:   
        pytest.fail(str(err))

"""
Тест добавление проекта
"""
@pytest.mark.positiv_test
def test_addProjekt_positiv(result_auth):
    
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth) # Проверяем успешное создание нового проекта.
    res_add = projekt.add_Projekt()
    idProjekt = res_add.json()['id'] # Запрос id проекта

    # Отправка запроса на окончательное наличие проектов
    apiKey = result_auth['apiKey']
    get_projekt = getProjekt(basUrl, apiKey, idProjekt)
    res_getProgekt = get_projekt.getProgekt()
    get_idProjekt = res_getProgekt.json()['id']
           
    try:
                # Проверяем, что запрос выполнен верно
        assert res_add.status_code == 201, f"Что то пошло не так: {res_add.status_code}"
        assert idProjekt == get_idProjekt, f"Вызван неверный id проекта. Должен быть {idProjekt}"
    except AssertionError as err:   
        pytest.fail(str(err))
"""
Тест изменение проекта
"""
@pytest.mark.positiv_test
def test_changeProjekt_positiv(result_auth):
    # Создание проекта
    projekt = addProjekt(basUrl, nameProjekt, result_auth)
    res_add = projekt.add_Projekt()
    idProjekt = res_add.json()['id'] # Запрос id проекта

    # Изменение названия проекта
    change_projekt = changeProjekt(basUrl, new_nameProjekt, result_auth, idProjekt)
    res_change = change_projekt.change_Projekt()
    new_idProjekt = res_change.json()['id']

    # Проверяем успешность операции
    try:
        assert res_change.status_code == 200, f"Проект не создан. Статус-код: {res_change.status_code}"
        assert idProjekt ==  new_idProjekt, f"Проект не изменен. Id проекта должен быть {new_idProjekt}"
    except AssertionError as err:
        pytest.fail(str(err))











    




    