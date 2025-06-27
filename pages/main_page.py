from pages.base_page import BasePage
import locators.main_page_locators
import allure

class MainPage(BasePage):
    @allure.step('Вводим адрес "откуда"')
    def input_address_from(self, address):
        self.add_text_to_element(locators.main_page_locators.INPUT_ADDRESS_FROM, address)

    @allure.step('Вводим адрес "Куда"')
    def input_address_to(self, address):
        self.add_text_to_element(locators.main_page_locators.INPUT_ADDRESS_TO, address)

    @allure.step('Получить стоимость заказа')
    def get_order_price(self):
        price = self.get_text_from_element(locators.main_page_locators.GET_PRICE_TEXT)
        int_price = int(price.split()[-2])
        return int_price

    @allure.step('Получить финальную стоимость заказа')
    def get_order_final_price(self):
        price = self.get_text_from_element(locators.main_page_locators.GET_FINAL_PRICE_TEXT)
        final_price = ''.join(filter(str.isdigit, price))
        return int(final_price)