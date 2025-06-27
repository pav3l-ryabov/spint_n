import pytest
import allure

import data
import locators.main_page_locators


class TestOrder:
    @allure.title('Проверка открытия формы заказа и отображения 6 тарифов')
    @pytest.mark.parametrize(
        'tariff',
        [
            [locators.main_page_locators.TAXI_TARIFF_WORK],
            [locators.main_page_locators.TAXI_TARIFF_SLEEP],
            [locators.main_page_locators.TAXI_TARIFF_WEEKEND],
            [locators.main_page_locators.TAXI_TARIFF_TALK],
            [locators.main_page_locators.TAXI_TARIFF_COMFORT],
            [locators.main_page_locators.TAXI_TARIFF_GLOSSY]
        ]
    )
    def test_open_order_form_and_tariffs(self, driver, add_addresses, tariff):
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)

        assert add_addresses.find_element_with_wait(*tariff), f'Кнопка тарифа {tariff} не отобразилась'

    @allure.title('Проверка отображения всплывающего окна "О тарифе" и проверка текста описания')
    @pytest.mark.parametrize(
        'tariff, text',
        [
            [locators.main_page_locators.TAXI_TARIFF_WORK, data.TEXT_WORK],
            [locators.main_page_locators.TAXI_TARIFF_SLEEP, data.TEXT_SLEEP],
            [locators.main_page_locators.TAXI_TARIFF_WEEKEND, data.TEXT_WEEKEND],
            [locators.main_page_locators.TAXI_TARIFF_TALK, data.TEXT_TALK],
            [locators.main_page_locators.TAXI_TARIFF_COMFORT, data.TEXT_COMFORT],
            [locators.main_page_locators.TAXI_TARIFF_GLOSSY, data.TEXT_GLOSSY]
        ]
    )
    @pytest.mark.xfail(reason='Описания тарифов "Сонный" и "Разговорчивый" не соответствуют ТЗ')
    def test_displayed_modal_window_and_text(self, driver, add_addresses, tariff, text):
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)

        add_addresses.click_to_element(tariff)
        add_addresses.click_to_element(locators.main_page_locators.BUTTON_I)

        assert add_addresses.get_text_from_element(locators.main_page_locators.TEXT_ABOUT_TARIFF) == text, (f'Текст описания'
                                                                          f'тарифа не соответствует {text}')

    @allure.title('Проверка отображения блока с полями с полями Телефон, Способ оплаты, Комментарий водителю,'
                  ' Требования к заказу Заказ тарифа Такси')
    @pytest.mark.parametrize(
        'field',
        [
            [locators.main_page_locators.FIELD_PHONE],
            [locators.main_page_locators.FIELD_PAY],
            [locators.main_page_locators.FIELD_COMMENT],
            [locators.main_page_locators.FIELD_ORDER_REQUIREMENTS]
        ]
    )
    def test_displayed_order_fields(self, driver, add_addresses, field):
        add_addresses.click_to_element(locators.main_page_locators.CALL_TAXI_BUTTON)

        assert add_addresses.find_element_with_wait(*field), f'Поле {field} на странице не найдено'
