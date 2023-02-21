import pytest

from src.swag_labs import settings
from src.swag_labs.pages.login_page import Login_page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Conftest:

    def __init__(self):
        self.driver = None

    @pytest.fixture
    def set_up(self, request):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        request.cls.login_page = Login_page(self.driver)
        self.driver.get(settings.url)

    @pytest.fixture
    def tear_down(self):
        yield self.driver
        self.driver.quit()

    # def pytest_addoption(self, parser):
    #     parser.addoption(
    #         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    #     )
    #
    # @pytest.fixture
    # def cmdopt(request):
    #     return request.config.getoption("--cmdopt")

    # def input_data(self):
