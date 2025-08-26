from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    #Methods

    def finish(self):
        Logger.add_start_step(method='finish')
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='finish')





