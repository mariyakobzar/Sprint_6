import allure

from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполение персональных данных в заказе")
    def create_order(self, order_dict):
        self.find_element_with_wait(OrderPageLocators.NAME)
        self.add_text_to_element(OrderPageLocators.NAME, order_dict['name'])
        self.find_element_with_wait(OrderPageLocators.LAST_NAME)
        self.add_text_to_element(OrderPageLocators.LAST_NAME, order_dict['last_name'])
        self.find_element_with_wait(OrderPageLocators.ADDRESS)
        self.add_text_to_element(OrderPageLocators.ADDRESS, order_dict['address'])
        self.click_to_element(OrderPageLocators.STATION)
        self.click_to_element(OrderPageLocators.STATION_CHOICE)
        self.find_element_with_wait(OrderPageLocators.TELEPHONE)
        self.add_text_to_element(OrderPageLocators.TELEPHONE, order_dict['telephone'])
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)


    @allure.step("Переход по лого")
    def page_transition_samokat(self):
        self.click_to_element(OrderPageLocators.LOGO_SAMOKAT)

    @allure.step("Переход по лого <Яндекс>")
    def page_transition_yandex(self):
        self.click_to_element(OrderPageLocators.LOGO_YANDEX)
        window_after = self.window_handlers(1)
        self.switch_to_window(window_after)
        return self.get_current_url()

    @allure.step("Получение заголовка формы заказа")
    def page_forma_head(self):
        return self.get_text_to_element(OrderPageLocators.HEADER_NAME)

