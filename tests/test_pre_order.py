from locators.main_page_locators import TAB_OPTIMAL, TAB_OPTIMAL_ACTIVE, \
    OPTIMAL_PRICE_TEXT, OPTIMAL_DURATION_TEXT, TAB_CUSTOM, TAB_CUSTOM_ACTIVE, CALL_TAXI_BUTTON, TYPE_DRIVE_BUTTON, \
    RESERV_BUTTON
import allure


class TestPreOrder:
    @allure.title('Проверка смены таба и перерасчета заказа при смене вида маршрута с оптимального на быстрый')
    def test_change_tab_from_optimal_to_fast(self, driver, add_addresses):
        add_addresses.click_to_element(TAB_OPTIMAL)

        assert add_addresses.find_element_with_wait(TAB_OPTIMAL_ACTIVE), 'Таб "Оптимальный" не стал активным'
        assert add_addresses.find_element_with_wait(OPTIMAL_PRICE_TEXT), 'Цена не пересчиталась'
        assert add_addresses.find_element_with_wait(OPTIMAL_DURATION_TEXT), 'Время в пути не пересчиталось'

    @allure.title('Проверка смены таба на свой')
    def test_change_tab_to_custom(self, driver, add_addresses):
        add_addresses.click_to_element(TAB_CUSTOM)

        assert add_addresses.find_element_with_wait(TAB_CUSTOM_ACTIVE), 'Таб "Свой" не стал активным'

    @allure.title('Проверка кнопки "Вызвать такси" в табе "Быстрый')
    def test_call_taxi_button(self, driver, add_addresses):

        assert add_addresses.find_element_with_wait(CALL_TAXI_BUTTON), 'Кнопка "Вызвать такси" не отобразилась'

    @allure.title('Проверка кнопки "Забронировать" в табе "Свой"')
    def test_call_taxi_button(self, driver, add_addresses):
        add_addresses.click_to_element(TAB_CUSTOM)
        add_addresses.click_to_element(TYPE_DRIVE_BUTTON)

        assert add_addresses.find_element_with_wait(RESERV_BUTTON), 'Кнопка "Забронировать" не отобразилась'
