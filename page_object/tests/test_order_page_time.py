import allure

from page_object.data import ORDER_INFO_DICT
from page_object.locators.order_page_time_locators import OrderPageTimeLocators
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_object.pages.order_page_time import OrderPageTime


class TestOrderPageTime():

    @allure.title('Завершение заказа')
    def test_finish_order(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_page_time = OrderPageTime(driver)
        main_page.page_transition_order()
        order_page.create_order(ORDER_INFO_DICT)
        order_page_time.finish_order()
        assert order_page.get_text_to_element(OrderPageTimeLocators.MODAL_APPROVE_YES) == "Да"

