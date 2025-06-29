from selenium.webdriver.common.by import By

INPUT_ADDRESS_FROM = (By.ID, 'from')
INPUT_ADDRESS_TO = (By.ID, 'to')

MAP_POINT_A = [By.XPATH, '//ymaps[contains(@class, "___ff3333_20x26")]']
MAP_POINT_B = [By.XPATH, '//ymaps[contains(@class, "___4296ea_20x26")]']

TAXI_ICON = [By.XPATH, '//img[@alt="Taxi"]']

PRICE_TEXT = [By.XPATH, '//div[@class="text" and text()="Авто Бесплатно"]']
DURATION_TEXT = [By.XPATH, '//div[@class="duration" and contains(text(), "В пути")]']
OPTIMAL_PRICE_TEXT = [By.XPATH, '//div[@class="text" and text()="Авто ~ 40 руб."]']
OPTIMAL_DURATION_TEXT = [By.XPATH, '//div[@class="duration" and contains(text(), "В пути 4 мин.")]']

TAB_OPTIMAL = [By.XPATH, '//div[text()="Оптимальный"]']
TAB_OPTIMAL_ACTIVE = [By.XPATH, '//div[@class="mode active" and text()="Оптимальный"]']
TAB_CUSTOM = [By.XPATH, '//div[text()="Свой"]']
TAB_CUSTOM_ACTIVE = [By.XPATH, '//div[@class="mode active" and text()="Свой"]']
CALL_TAXI_BUTTON = [By.XPATH, '//button[@class="button round" and text()="Вызвать такси"]']
RESERV_BUTTON = [By.XPATH, '//button[@class="button round" and text()="Забронировать"]']
TYPE_DRIVE_BUTTON = [By.XPATH, '//div[contains(@class, "type") and contains(@class, "drive")]']

ACTIVE_TARIFF_TAXI = [By.XPATH, '//div[@class="tcard active"]/child::div[@class="tcard-title"]']
TAXI_TARIFF_WORK = [By.XPATH, '//div[contains(text(), "Рабочий")]']
TAXI_TARIFF_SLEEP = [By.XPATH, '//div[contains(text(), "Сонный")]']
TAXI_TARIFF_WEEKEND = [By.XPATH, '//div[contains(text(), "Отпускной")]']
TAXI_TARIFF_TALK = [By.XPATH, '//div[contains(text(), "Разговорчивый")]']
TAXI_TARIFF_COMFORT = [By.XPATH, '//div[contains(text(), "Утешительный")]']
TAXI_TARIFF_GLOSSY = [By.XPATH, '//div[contains(text(), "Глянцевый")]']

BUTTON_I = [By.XPATH, '//div[@class="tcard active"]/child::button[@class="i-button tcard-i active"]']
TEXT_ABOUT_TARIFF = [By.XPATH, '//div[@class="tcard active"]/descendant::div[@class="i-dPrefix"]']

FIELD_PHONE = [By.XPATH, '//div[@class="form"]/descendant::div[text()="Телефон"]']
FIELD_PAY = [By.XPATH, '//div[@class="form"]/descendant::div[text()="Способ оплаты"]']
FIELD_COMMENT = [By.XPATH, '//div[@class="form"]/descendant::label[text()="Комментарий водителю..."]']
FIELD_ORDER_REQUIREMENTS = [By.XPATH, '//div[@class="form"]/descendant::div[text()="Требования к заказу"]']

DROPDOWN_BUTTON_REQUIREMENTS = [By.XPATH, '//div[@class="reqs-arrow"]']
CHECKBOX_TABLE_FOR_NOTEBOOK = [By.XPATH, '//div[@class="switch"]']
GET_ORDER_BUTTON = [By.XPATH, '//button[contains(@class, "smart-button")]']
FIND_AUTO_HEADER = [By.XPATH, '//div[@class="order-header-title" and text()="Поиск машины"]']
CLOSE_BUTTON = [By.XPATH, '//button[@class="order-button" and .//img[contains(@src, "plus.") and contains(@style, "rotate(45deg)")]]']
MENU_BUTTON = [By.XPATH, '//button[@class="order-button" and .//img[contains(@src, "burger.") and @alt="burger"]]']
ORDER_TIMER = [By.XPATH, '//div[@class="order-header-time" and contains(text(), ":")]']

TIME_TO_COME = [By.XPATH, '//div[contains(@class, "order-header-title") and contains(text(), "мин. и приедет") and ./img]']
CAR_NUMBER = [By.XPATH, '//div[@class="number"]']
WORK_CAR_ICON = [By.XPATH, '//img[contains(@src, "economy.") and @alt="Car" and contains(@style, "width: 52px") and contains(@style, "bottom: -16px")]']
DRIVER_ICON = [By.XPATH, '//div[@class="order-button" and .//div[@class="order-btn-rating" and contains(text(), ",") and .//img[contains(@src, "bender.") and @alt="close"]]']
GET_PRICE_TEXT = [By.XPATH, '//div[@class="text"]']
GET_FINAL_PRICE_TEXT = [By.XPATH, '//div[contains(text(), "Стоимость")]']