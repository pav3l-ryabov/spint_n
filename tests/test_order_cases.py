import pytest
import allure

import locators.main_page_locators
from tests.conftest import add_addresses


class TestOrderCases:
    @allure.title('Проверка открытия окна ожидания машины')
    def test_open_wait_car_window(self, driver, add_addresses):
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)
        add_addresses.click_to_element(locators.main_page_locators.DROPDOWN_BUTTON_REQUIREMENTS)
        add_addresses.click_to_element(locators.main_page_locators.CHECKBOX_TABLE_FOR_NOTEBOOK)
        add_addresses.click_to_element(locators.main_page_locators.GET_ORDER_BUTTON)

        assert add_addresses.find_element_with_wait(locators.main_page_locators.FIND_AUTO_HEADER), 'Заголовок отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.CLOSE_BUTTON), 'Кнопка закрытия отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.MENU_BUTTON), 'Кнопка "меню" отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.ORDER_TIMER), 'Таймер заказа отсутствует'

    @allure.title('Проверка открытия окна совершенного заказа')
    def test_open_done_order(self, driver, add_addresses):
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)
        add_addresses.click_to_element(locators.main_page_locators.DROPDOWN_BUTTON_REQUIREMENTS)
        add_addresses.click_to_element(locators.main_page_locators.CHECKBOX_TABLE_FOR_NOTEBOOK)
        add_addresses.click_to_element(locators.main_page_locators.GET_ORDER_BUTTON)

        assert add_addresses.find_element_with_wait(locators.main_page_locators.TIME_TO_COME), 'Время до прибытия отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.CAR_NUMBER), 'Номер машины отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.WORK_CAR_ICON), 'Иконка тарифа отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.DRIVER_ICON), 'Иконка водителя отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.CLOSE_BUTTON), 'Кнопка закрытия отсутствует'
        assert add_addresses.find_element_with_wait(locators.main_page_locators.MENU_BUTTON), 'Кнопка "меню" отсутствует'

    @allure.title('Проверка совпадения изначальной и конечной стоимости заказа')
    def test_order_price(self, driver, add_addresses):
        price = add_addresses.get_order_price()
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)
        add_addresses.click_to_element(locators.main_page_locators.DROPDOWN_BUTTON_REQUIREMENTS)
        add_addresses.click_to_element(locators.main_page_locators.CHECKBOX_TABLE_FOR_NOTEBOOK)
        add_addresses.click_to_element(locators.main_page_locators.GET_ORDER_BUTTON)
        add_addresses.click_to_element_with_actionchains(locators.main_page_locators.MENU_BUTTON)
        final_price = add_addresses.get_order_final_price()
        assert final_price == price, (f'Цена не совпадает, получили итоговую цену {final_price}'
                                                              f'начальную цену: {price}')

    @allure.title('Проверка закрытия окна заказа')
    @pytest.mark.xfail(reason='Кнопка закрыть не работает')
    def test_close_button(self, driver, add_addresses):
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)
        add_addresses.click_to_element(locators.main_page_locators.DROPDOWN_BUTTON_REQUIREMENTS)
        add_addresses.click_to_element(locators.main_page_locators.CHECKBOX_TABLE_FOR_NOTEBOOK)
        add_addresses.click_to_element(locators.main_page_locators.GET_ORDER_BUTTON)
        add_addresses.click_to_element(locators.main_page_locators.CLOSE_BUTTON)
        assert not add_addresses.find_element_with_wait(locators.main_page_locators.CLOSE_BUTTON), 'Окно заказа все еще отображается'