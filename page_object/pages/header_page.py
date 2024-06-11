import allure

from page_object.locators.header_page_locators import HeaderPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.title("Переход по лого <Самокат>")
    def page_transition_samokat(self):
        self.click_to_element(MainPageLocators.COOKIE)
        self.click_to_element(MainPageLocators.BUTTON_ORDER)
        self.click_to_element(HeaderPageLocators.LOGO_SAMOKAT)
        assert self.get_text_to_element(MainPageLocators.HEAD_TEXT) == "Самокат "

    @allure.title("Переход по лого <Яндекс>")
    def page_transition_yandex(self):
        self.click_to_element(MainPageLocators.COOKIE)
        self.click_to_element(MainPageLocators.BUTTON_ORDER)
        self.click_to_element(HeaderPageLocators.LOGO_YANDEX)
        assert self.find_element_with_wait(HeaderPageLocators.DZEN_REDIRECT)
