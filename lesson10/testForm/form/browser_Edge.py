from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


class bro_Edg:
    def __init__(self, path: str):
        self.path = path

    def web(self) -> webdriver:
        """
            Установка драйвера из сети.
            Если драйвер не установился,
            то запускается преустановленный драйвер.
        """
        try:

            brow = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            return brow
        except Exception as ex:
            print(
                f"""Автоматическое обновление
                драйвера Edge завершилось неудачей: {ex}"""
                )
            driver_path = self.path
            service = Service(driver_path)
            brow = webdriver.Edge(service=service)
            return brow
