from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class bro_Chrome:

    def web(brow) -> webdriver:
        """
            Устанавливает драйвер webdriver.Chrome
        """
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver
