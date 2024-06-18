import allure

from page_object.locators.header_page_locators import HeaderPageLocators
from page_object.pages.base_page import BasePage

class HeaderPage(BasePage):

    @allure.step("Переход по лого <Яндекс>")
    def switch_page_dzen(self):
        self.get_text_to_element(HeaderPageLocators.DZEN_REDIRECT)