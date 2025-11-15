import pytest
from calc.calc_02 import Calc
from calc.browser_Chrome import bro_Chrome


@pytest.fixture(scope='module')
def test_openBrowser():
    bro = bro_Chrome()
    driver = bro.web()
    yield driver
    driver.quit()


@pytest.mark.parametrize('inTime, result', [(45, 45)])
def test_time_wait(test_openBrowser, inTime, result):
    calc = Calc(test_openBrowser, inTime)
    calc.web()
    res = calc.time_Wait()
    assert result == res
