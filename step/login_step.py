from src.swag_labs.test.conftest import Conftest
from src.swag_labs.pages.login_page import Login_page
import src.swag_labs.utilities.custom_logger as cl
import logging


class Login_step:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(Login_page.login_locators().uname).send_keys(username)
        self.driver.find_element(Login_page.login_locators().password).send_keys(password)
