from page_object.data import ORDER_INFO_DICT
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


class TestOrderPage():

    def test_create_order(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order(ORDER_INFO_DICT)
