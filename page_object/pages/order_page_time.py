import allure

from page_object.locators.order_page_time_locators import OrderPageTimeLocators
from page_object.pages.base_page import BasePage


class OrderPageTime(BasePage):

    @allure.step("Завершить заказ")
    def finish_order(self):
        self.click_to_element(OrderPageTimeLocators.INPUT_TIME_ARRIVE)
        self.click_to_element(OrderPageTimeLocators.DATAPICKER_DAY)
        self.click_to_element(OrderPageTimeLocators.RENT_TIME)
        self.click_to_element(OrderPageTimeLocators.NUMBER_OF_DAYS)
        self.click_to_element(OrderPageTimeLocators.BUTTON_SET_ORDER)
        self.find_element_with_wait(OrderPageTimeLocators.MODAL_APPROVE_ORDER)



