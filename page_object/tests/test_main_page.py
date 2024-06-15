import allure
import pytest

from page_object.data import Answers
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


class TestMainPage():

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Answers.ANSWER_0),
            (1, Answers.ANSWER_1),
            (2, Answers.ANSWER_2),
            (3, Answers.ANSWER_3),
            (4, Answers.ANSWER_4),
            (5, Answers.ANSWER_5),
            (6, Answers.ANSWER_6),
            (7, Answers.ANSWER_7)
        ]
    )
    @allure.title('Открытие вопросов-ответов на главной странице')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result

    @allure.title('Кнопка <Заказать в блоке <Как это работает>>')
    def test_check_set_order_button_low(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_set_order_button_low()
        assert order_page.get_text_to_element(OrderPageLocators.HEADER_NAME) == "Для кого самокат"
