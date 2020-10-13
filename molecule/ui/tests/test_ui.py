import pytest
import os
import socket
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestGraylog():
    url = 'http://localhost:9000'

    def test_title(self, chromedriver):
        print("\nVerifying title text...")
        assert "Graylog - Getting started" in chromedriver.title

    def test_version(self, chromedriver):
        print('Checking if version is ' + os.environ['GRAYLOG_VERSION'] + '...')

        chromedriver.get(self.url + "/system/overview")
        assert 'Graylog ' + os.environ['GRAYLOG_VERSION'] in chromedriver.find_element_by_xpath('//footer').text

    def test_input_udp(self, chromedriver):
        print('Testing GELF UDP Input...')
        chromedriver.get(self.url + "/system/inputs")

        wait = WebDriverWait(chromedriver, 10)
        element = wait.until(expected_conditions.title_is('Graylog - Inputs'))

        #Click input dropdown
        chromedriver.find_element_by_css_selector(".form-group").click()

        #Click GELF UDP option
        chromedriver.find_element_by_xpath('//div[text()="GELF UDP"]').click()

        #Click "Launch new Input" button
        chromedriver.find_element_by_xpath('//button[text()="Launch new input"]').click()

        #Wait for node dropdown to load
        WebDriverWait(chromedriver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'node-select')))

        #Select node
        chromedriver.find_element_by_xpath("//select[@id='node-select']/option[2]").click()

        #Fill out input field
        title_field = chromedriver.find_element_by_id("title")
        title_field.send_keys('Test UDP Input')

        #Save form
        title_field.send_keys(Keys.RETURN)

        #Check that the input is there and running.
        WebDriverWait(chromedriver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, '//h2[text()="Test UDP Input"]')))
        input_status = WebDriverWait(chromedriver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, '//span[text()="GELF UDP"]')))
        assert 'RUNNING' in input_status.text

        time.sleep(5)

        #Send something through the input
        for x in range(3):
            socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(b'{ "version": "1.1", "host": "localhost", "short_message": "Hello Graylog!", "level": 5 }', ("127.0.0.1", 12201))

        time.sleep(5)

        #Check if Graylog received it
        chromedriver.get(self.url + "/search?q=&rangetype=relative&relative=0")
        WebDriverWait(chromedriver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[text()="Hello Graylog!"]')))
