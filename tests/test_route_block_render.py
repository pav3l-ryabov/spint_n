from data import POINT_A_ADDRESS, POINT_B_ADDRESS
from locators.main_page_locators import TAXI_ICON, DURATION_TEXT, PRICE_TEXT
from pages.main_page import MainPage
import allure
import  pytest


class TestRouteBlockRender:
    @allure.title('Проверка отрисовки блока выбора маршрута при двух разных точках')
    @pytest.mark.parametrize(
        'point_a, point_b',
        [
            [POINT_A_ADDRESS, POINT_B_ADDRESS],
            [POINT_B_ADDRESS, POINT_A_ADDRESS]
        ]
    )
    def test_rout_block_render(self, driver, point_a, point_b):
        main_page = MainPage(driver)
        main_page.input_address_from(point_a)
        main_page.input_address_to(point_b)

        assert main_page.find_element_with_wait(TAXI_ICON), 'Отобразился некорректный блок выбора маршрута'

    @allure.title('Проверка отрисовки блока выбора маршрута при двух одинаковых точках')
    def test_rout_block_render(self, driver):
        main_page = MainPage(driver)
        main_page.input_address_from(POINT_A_ADDRESS)
        main_page.input_address_to(POINT_A_ADDRESS)

        assert main_page.find_element_with_wait(DURATION_TEXT), 'Неверный текст времени в пути'
        assert main_page.find_element_with_wait(PRICE_TEXT), 'Неверный текст цены'
