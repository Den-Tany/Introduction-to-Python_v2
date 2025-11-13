# test файл
import pytest
from shop.shop_03 import Shop
from shop.browser_Firefox import bro_Firefox
from shop.auth import Auth
from shop.choice import Choice
from shop.form import Form

Username = 'standard_user'
Password = 'secret_sauce'

firstName = 'Den'
lastName = 'Tany'
ZipCode = '689000'


@pytest.fixture(scope='module')
def test_openBrowser():
    bro = bro_Firefox()
    driver = bro.web()
    yield driver
    driver.quit()


@pytest.mark.parametrize('result', [("$58.29")])
def test_time_wait(test_openBrowser, result):
    auth = Auth(test_openBrowser, Username, Password)
    auth.start_Web()

    choice = Choice(test_openBrowser)
    choice.choice()

    form = Form(test_openBrowser, firstName, lastName, ZipCode)
    form.filling_out_the_form()

    shop = Shop(test_openBrowser)
    total_coast = shop.total_cost()

    assert result == total_coast
