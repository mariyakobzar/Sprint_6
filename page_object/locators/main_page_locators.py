from selenium.webdriver.common.by import By

class MainPageLocators():

    COOKIE = By.XPATH, '//button[@id="rcc-confirm-button"]'
    QUESTION_LOCATOR = By.XPATH, '//div[@aria-controls="accordion__panel-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@aria-labelledby="accordion__heading-{}"]'

    BUTTON_ORDER = By.XPATH, '//button[@class="Button_Button__ra12g"]'

    BUTTON_ORDER_LOW = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    HEAD_TEXT = '//div[@class="Home_Header__iJKdX"]'