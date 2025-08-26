from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from base.base_class import Base
from utilities.logger import Logger


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.faker = Faker()


    #Locators
    first_name_field = "//input[@id='first-name']"
    last_name_field = "//input[@id='last-name']"
    postal_code_field = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    #Getters

    def get_first_name_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_postal_code_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.postal_code_field)))

    def get_continue_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    #Actions

    def input_first_name(self, first_name=None):
        if first_name is None:
            first_name = self.faker.first_name()
        self.get_first_name_field().send_keys(first_name)
        print(f'Input First Name: {first_name}')
        return first_name

    def input_last_name(self, last_name=None):
        if last_name is None:
            last_name = self.faker.last_name()
        self.get_last_name_field().send_keys(last_name)
        print(f'Input Last Name: {last_name}')
        return last_name

    def input_postal_code(self, postal_code=None):
        if postal_code is None:
            postal_code = self.faker.postalcode()
        self.get_postal_code_field().send_keys(postal_code)
        print(f'Input Postal Code: {postal_code}')
        return postal_code

    def click_continue_button(self):
        self.get_continue_button().click()
        print(f'Continue Button Clicked')


    #Methods

    def input_client_info(self):
        Logger.add_start_step(method='input_client_info')
        self.get_current_url()
        self.input_first_name()
        self.input_last_name()
        self.input_postal_code()
        self.click_continue_button()
        Logger.add_end_step(url=self.driver.current_url, method='input_client_info')