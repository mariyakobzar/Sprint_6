from selenium.webdriver.common.by import By


class OrderPageTimeLocators():

    BUTTON_BACK = By.XPATH, '//button[ @class ="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]'

    INPUT_TIME_ARRIVE = By.XPATH, '//div[@class="react-datepicker__input-container"]/input[@class ="Input_Input__1iN_Z Input_Responsible__1jDKN"]'
    DATAPICKER_DAY = By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--016 react-datepicker__day--weekend"]'
    RENT_TIME = By.XPATH, '//div[@class="Dropdown-placeholder"]'
    NUMBER_OF_DAYS = By.XPATH, '//div[@class="Dropdown-option"]'

    BUTTON_SET_ORDER = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    MODAL_APPROVE_ORDER = By.XPATH, '//div[@class ="Order_ModalHeader__3FDaJ"]'
    MODAL_APPROVE_YES = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][text()="Да"]'