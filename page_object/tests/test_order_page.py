import allure

from page_object.data import ORDER_INFO_DICT
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_object.pages.order_page_time import OrderPageTime


class TestOrderPage():

    @allure.title('Заполнение формы заказа <Для кого самокат>')
    def test_create_order(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_page_time = OrderPageTime(driver)
        main_page.page_transition_order()
        order_page.create_order(ORDER_INFO_DICT)
        assert order_page_time.button_back() == "Назад"
