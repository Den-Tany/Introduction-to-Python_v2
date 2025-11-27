import pytest
from lesson10 import SQL

user_id = 6854
user_email = 'd@db.nat'
subject_id = 12
new_user_email = 'fff@db.com'

@pytest.mark.create_user
def test_add_user():
    sql = SQL()
    sql.add_user(user_id, user_email, subject_id)
    res = sql.get_user(user_id)
    try:
        assert len(res)>0, f'Даннных нет'
        assert res[0]['user_id'] == user_id, f'Что-то пошло не так'
    except AssertionError as err:
            pytest.fail(str(err))
    sql.delete_user(user_id)

@pytest.mark.patch_user
def test_patch():
    sql = SQL()
    sql.add_user(user_id, user_email, subject_id)
    sql.change_user(new_user_email, user_id)
    res = sql.get_user(user_id)
    try:
        assert len(res)>0, f'Даннных нет'
        assert res[0]['user_email'] == new_user_email, f'Что-то пошло не так'
    except AssertionError as err:
            pytest.fail(str(err))
    sql.delete_user(user_id)

@pytest.mark.delete_user
def test_delete_user():
    sql = SQL()
    sql.add_user(user_id, user_email, subject_id)
    sql.delete_user(user_id)
    res = sql.get_user(user_id)
    try:
        assert len(res)==0, f'Не удалилось'
    except AssertionError as err:
            pytest.fail(str(err))
