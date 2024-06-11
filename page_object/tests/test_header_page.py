from page_object.pages.header_page import HeaderPage


class TestHeaderPage():
    def test_page_transition_samokat(self, driver):
         header_page = HeaderPage(driver)

    def test_page_transition_yandex(self, driver):
        header_page = HeaderPage(driver)

