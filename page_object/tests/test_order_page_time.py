from page_object.data import ORDER_INFO_DICT
from page_object.pages.order_page import OrderPage
from page_object.pages.order_page_time import OrderPageTime


class TestOrderPageTime():

    def test_finish_order(self, driver):
        order_page = OrderPage(driver)
        order_page_time = OrderPageTime(driver)
        order_page.create_order(ORDER_INFO_DICT)
        order_page_time.finish_order()

