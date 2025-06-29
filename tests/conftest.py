import pytest
from selenium import webdriver

from data import MAIN_PAGE, POINT_A_ADDRESS, POINT_B_ADDRESS
from pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def add_addresses(driver):
    page = MainPage(driver)
    page.input_address_from(POINT_A_ADDRESS)
    page.input_address_to(POINT_B_ADDRESS)
    return page