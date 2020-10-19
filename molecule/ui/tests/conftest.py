import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

@pytest.fixture(scope="module")
def chromedriver(host):
    print("\nWaiting for Graylog to start up...")
    end_time = time.time() + 90
    server_up = 1

    while server_up != 0 and time.time() < end_time:
        time.sleep(2)
        server_up = host.run_test("cat /var/log/graylog-server/server.log | grep 'Graylog server up and running.'").exit_status

    assert server_up == 0

    try:
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-gpu");

        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 10)
        url = 'http://localhost:9000'
        driver.get(url + "/gettingstarted")

        element = wait.until(expected_conditions.title_contains('Sign in'))

        #Login to Graylog
        uid_field = driver.find_element_by_name("username")
        uid_field.clear()
        uid_field.send_keys("admin")
        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys("admin")
        password_field.send_keys(Keys.RETURN)

        element = wait.until(expected_conditions.title_contains('Getting started'))

        #Run tests
        yield driver
    finally:
        driver.quit()
