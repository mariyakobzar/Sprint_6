import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_object.data import Urls


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(Urls.URL_SCOOTER)
    yield driver
    driver.quit()