from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    options.add_argument("--guest")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_link_about()

    print("Finish Test")
    driver.quit()

