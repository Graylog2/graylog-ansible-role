import pytest
import os
import socket
import time
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def test_service_elasticsearch_running(host):
    print("\nEnsure Elasticsearch is running...")
    assert host.service("elasticsearch").is_running is True

def test_service_mongodb_running(host):
    print("Ensure MongoDB is running...")
    if host.system_info.distribution == 'ubuntu' and host.system_info.codename == 'focal':
        mongodb_service_name = 'mongodb'
    else:
        mongodb_service_name = 'mongod'

    assert host.service(mongodb_service_name).is_running is True

def test_is_graylog_installed(host):
    print("Ensure graylog-server package is installed...")
    assert host.package('graylog-server').is_installed

def test_service_graylog_running(host):
    print("Ensure graylog-server service is running...")
    assert host.service("graylog-server").is_running is True

def test_service_graylog_started(host):
    print("Waiting for Graylog to start up...")
    end_time = time.time() + 90
    server_up = 1

    while server_up != 0 and time.time() < end_time:
        time.sleep(2)
        server_up = host.run_test("cat /var/log/graylog-server/server.log | grep 'Graylog server up and running.'").exit_status

    assert server_up == 0

def test_service_graylog_plugins_loaded(host):
    print("Checking if plugins loaded...")
    results = host.run_test('curl -u admin:admin http://' + host.interface('eth0').addresses[0] + ':9000/api/system/plugins')
    plugins = json.loads(results.stdout)

    enterprise_plugin_loaded = False
    integrations_plugin_loaded = False
    enterprise_integrations_plugin_loaded = False

    for plugin in plugins['plugins']:
      if plugin['name'] == 'Graylog Enterprise':
        enterprise_plugin_loaded = True
        assert plugin['version'] == os.environ['GRAYLOG_VERSION']

      if plugin['name'] == 'Integrations':
        integrations_plugin_loaded = True
        assert plugin['version'] == os.environ['GRAYLOG_VERSION']

      if plugin['name'] == 'Graylog Enterprise':
        enterprise_integrations_plugin_loaded = True
        assert plugin['version'] == os.environ['GRAYLOG_VERSION']

    assert enterprise_plugin_loaded is True
    assert integrations_plugin_loaded is True
    assert enterprise_integrations_plugin_loaded is True


class TestUI():
    url = 'http://localhost:9000'

    def test_title(self, chromedriver):
        print("\nVerifying title text...")
        assert "Getting started" in chromedriver.title

    def test_version(self, chromedriver):
        print('Checking if version is ' + os.environ['GRAYLOG_VERSION'] + '...')
        chromedriver.get(self.url + "/system/overview")

        footer = WebDriverWait(chromedriver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//footer"))).text
        assert os.environ['GRAYLOG_VERSION'] in footer

    def test_input_udp(self, chromedriver):
        print('Testing GELF UDP Input...')
        chromedriver.get(self.url + "/system/inputs")

        #Wait for dropdown to load
        WebDriverWait(chromedriver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'form-group')))

        #Click input dropdown
        chromedriver.find_element_by_css_selector(".form-group").click()

        #Click GELF UDP option
        gelf_udp_option = WebDriverWait(chromedriver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[text()="GELF UDP"]')))
        gelf_udp_option.click()
        #chromedriver.find_element_by_xpath('//div[text()="GELF UDP"]').click()

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

        retries = 1
        element = None
        while retries <= 3:
            try:
                element = WebDriverWait(chromedriver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[text()="Hello Graylog!"]')))
                break
            except TimeoutException:
                chromedriver.refresh()
                retries += 1
        assert 'Hello Graylog!' == element.text
