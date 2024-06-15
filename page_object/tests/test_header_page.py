from datetime import time

import allure

from page_object.data import Urls
from page_object.locators.header_page_locators import HeaderPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages import header_page
from page_object.pages.base_page import BasePage
from page_object.pages.header_page import HeaderPage
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


class TestHeaderPage():
    @allure.title('Переход по лого <Самокат>')
    def test_page_transition_samokat(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.page_transition_order()
        order_page.page_transition_samokat()
        assert main_page.switch_page() == 'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

    @allure.title('Переход по лого <Яндекс>')
    def test_page_transition_yandex(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.page_transition_order()
        assert order_page.page_transition_yandex() == Urls.URL_DZEN

