from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class bro_Firefox:

    def web(brow) -> webdriver:
        """
        Запуск утилиты webdriver.
        Установка драйвера Firefox
        """
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
            )
        return driver
