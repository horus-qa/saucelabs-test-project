from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    #Locators
    checkout_button = "//button[@id='checkout']"


    #Getters

    def get_checkout_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout Button")


    #Methods

    def confirm_product(self):
        Logger.add_start_step(method='confirm_product')
        self.get_current_url()
        self.click_checkout_button()
        Logger.add_end_step(url=self.driver.current_url, method='confirm_product')





