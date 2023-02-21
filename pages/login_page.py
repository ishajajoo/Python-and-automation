from selenium.webdriver.common.by import By

#from src.swag_labs.test.Testbase import BaseTest


class Login_page():
    def __init__(self, driver):
        #super().__init__(driver)
        self.driver = driver
        self.submit = None
        self.password = None
        self.uname = None
        self.driver = None

    def login_locators(self):
        """
        Given
        When
        then

        :return:
        """
        self.uname = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.submit = (By.ID, "login-button")

    # @pytest.mark.parametrize('initials, country', [('UY', 'Uruguay'), ('CL', 'Chile')])
    # def test_validate_link_to_country_works(self, initials, country):
    #     """
    #     Given I amm on the Select Country Page
    #     When I select a Country
    #     Then I must be redirected to the Home Page of <country>
    #     """
    #     self.country_page.select_country(initials)
    #     assert country in self.country_page.get_title()
