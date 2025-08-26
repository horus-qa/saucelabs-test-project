from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    #Locators
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"


    #Getters

    def get_select_product_1(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.link_about)))



    #Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Select Product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click Select Product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click Select Product 3")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart Button")

    def click_menu(self):
        self.get_menu().click()
        print("Click Menu Button")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click About Link")

    #Methods

    def select_products_1(self):
        Logger.add_start_step(method='select_products_1')
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_products_1')

    def select_products_2(self):
        Logger.add_start_step(method='select_products_2')
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_products_2')

    def select_products_3(self):
        Logger.add_start_step(method='select_products_3')
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_products_3')

    def select_menu_about(self):
        Logger.add_start_step(method='select_menu_about')
        self.get_current_url()
        self.click_menu()
        Logger.add_end_step(url=self.driver.current_url, method='select_menu_about')

    def select_link_about(self):
        Logger.add_start_step(method='select_link_about')
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url("https://saucelabs.com/")
        Logger.add_end_step(url=self.driver.current_url, method='select_link_about')





