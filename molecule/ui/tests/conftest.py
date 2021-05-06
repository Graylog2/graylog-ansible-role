import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

@pytest.fixture(scope="session")
def chromedriver():
    try:
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)

        url = 'http://localhost:9000'
        driver.get(url + "/gettingstarted")

        WebDriverWait(driver, 30).until(expected_conditions.title_contains('Sign in'))

        #Login to Graylog
        uid_field = driver.find_element_by_name("username")
        uid_field.clear()
        uid_field.send_keys("admin")
        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys("admin")
        password_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 30).until(expected_conditions.title_contains('Getting started'))

        #Run tests
        yield driver
    finally:
        driver.quit()
