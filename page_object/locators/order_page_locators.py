from selenium.webdriver.common.by import By

class OrderPageLocators():

    HEADER_NAME = By.XPATH, '//div[@class="Order_Header__BZXOb"]'

    NAME = By.XPATH, '//div[@class="Input_InputContainer__3NykH"][1]/input[1][@placeholder="* Имя"]'
    LAST_NAME = By.XPATH, '//div[@class="Input_InputContainer__3NykH"][2]/input'
    ADDRESS = By.XPATH, '//div[@class="Input_InputContainer__3NykH"][3]/input'
    STATION = By.XPATH, '//input[@class="select-search__input"]'
    STATION_CHOICE = By.XPATH, '//li/button[@value="1"]'
    TELEPHONE = By.XPATH, '//div[@class="Input_InputContainer__3NykH"][4]/input'

    BUTTON_NEXT = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    LOGO_SAMOKAT = By.XPATH, '//img[@src="/assets/scooter.svg"]'
    LOGO_YANDEX = By.XPATH, '//img[@src="/assets/ya.svg"]'

