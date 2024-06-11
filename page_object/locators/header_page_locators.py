from selenium.webdriver.common.by import By


class HeaderPageLocators():

    LOGO_YANDEX = By.XPATH, '//img[@src="/assets/ya.svg"]'
    LOGO_SAMOKAT = By.XPATH, '//img[@src="/assets/scooter.svg"]'

    DZEN_REDIRECT = By.CSS_SELECTOR, '[class="desktop-base-header__logo-2H"]'