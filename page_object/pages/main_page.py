import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element(MainPageLocators.COOKIE)
        self.click_to_element(locator_q_formatted)
        return self.get_text_to_element(locator_a_formatted)

    @allure.step("Проверка открытия формы заказа через кнопку <Заказать> в блоке <Как это работает>")
    def check_set_order_button_low(self):
        self.click_to_element(MainPageLocators.COOKIE)
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_LOW)
        self.click_to_element(MainPageLocators.BUTTON_ORDER_LOW)

    @allure.title("Переход на страницу заказа")
    def page_transition_order(self):
        self.click_to_element(MainPageLocators.COOKIE)
        self.click_to_element(MainPageLocators.BUTTON_ORDER)

    @allure.title("Получаем название заголовка на главной странице")
    def switch_page(self):
        return self.get_text_to_element(MainPageLocators.HEAD_TEXT)







