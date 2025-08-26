import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.checkout_page import CheckoutPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

# @pytest.mark.order(3)
def test_buy_product_1(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_1()

    cp = CheckoutPage(driver)
    cp.click_checkout_button()

    cip = ClientInfoPage(driver)
    cip.input_client_info()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    print("Finish Test 1")
    driver.quit()

# @pytest.mark.order(1)
def test_buy_product_2(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 2")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_2()

    cp = CheckoutPage(driver)
    cp.click_checkout_button()

    print("Finish Test 2")
    driver.quit()

# @pytest.mark.order(2)
def test_buy_product_3(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 3")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_3()

    cp = CheckoutPage(driver)
    cp.click_checkout_button()

    print("Finish Test 3")
    driver.quit()
