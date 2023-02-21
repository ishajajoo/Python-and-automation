from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_multiple_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def get_count_elements(self, locator):
        return len(self.find_multiple_elements(locator))

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    def explicit_wait(self, element, locator, timeout):
        web_driver_wait = WebDriverWait(self.drv, timeout)
        web_driver_wait.until(EC.presence_of_element_located(By.ID, element))


    # def select_by_value(self):
