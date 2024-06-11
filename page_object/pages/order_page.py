import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.locators.order_page_time_locators import OrderPageTimeLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполение персональных данных в заказе")
    def create_order(self, order_dict):
        self.click_to_element(MainPageLocators.COOKIE)
        self.click_to_element(MainPageLocators.BUTTON_ORDER)
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
        assert self.get_text_to_element(OrderPageTimeLocators.BUTTON_BACK) == "Назад"




