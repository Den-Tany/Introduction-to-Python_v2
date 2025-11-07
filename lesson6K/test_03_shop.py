# test файл
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from shop_03 import Shop


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


@pytest.mark.parametrize("result", ["$58.29"])  # Исправили аннотацию
def test_time_wait(browser, result):           # Передали browser через фикстуру
    shop = Shop(browser)
    shop.start_Web()
    shop.auth()
    shop.choice()
    shop.filling_out_the_form()
    total_coast = shop.total_cost()
    
    assert result == total_coast
