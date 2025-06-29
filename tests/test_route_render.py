from data import POINT_A_ADDRESS, POINT_B_ADDRESS
from locators.main_page_locators import MAP_POINT_A, MAP_POINT_B
from pages.main_page import MainPage
import allure
import  pytest


class TestRouteRender:
    @allure.title('Проверка отрисовки точек маршрута')
    @pytest.mark.parametrize(
        'point_a, point_b',
        [
            [POINT_A_ADDRESS, POINT_B_ADDRESS],
            [POINT_B_ADDRESS, POINT_A_ADDRESS]
        ]
    )
    def test_rout_render(self, driver, point_a, point_b):
        main_page = MainPage(driver)
        main_page.input_address_from(point_a)
        main_page.input_address_to(point_b)

        assert main_page.find_element_with_wait(MAP_POINT_A), 'Точка А не отобразилась на карте'
        assert main_page.find_element_with_wait(MAP_POINT_B), 'Точка Б не отобразилась на карте'