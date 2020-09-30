import os

import testinfra.utils.ansible_runner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_basic_login(host):
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_arguments("--disable-gpu");
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    url = 'http://' + host.interface('eth0').addresses[0] + ':9000'

    driver.get(url + "/gettingstarted")

    element = wait.until(EC.title_is(('Graylog - Sign in')))

    #login
    uid_field = driver.find_element_by_name("username")
    uid_field.clear()
    uid_field.send_keys("admin")
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys("admin")
    password_field.send_keys(Keys.RETURN)

    element = wait.until(EC.title_is(('Graylog - Getting started')))

    driver.close()

def test_service_elasticsearch_running(host):
    assert host.service("elasticsearch").is_running is True

def test_service_mongodb_running(host):
    if host.system_info.distribution == 'ubuntu' and host.system_info.codename == 'focal':
        mongodb_service_name = 'mongodb'
    else:
        mongodb_service_name = 'mongod'

    assert host.service(mongodb_service_name).is_running is True

def test_is_graylog_installed(host):
    assert host.package('graylog-server').is_installed

def test_service_graylog_running(host):
    assert host.service("graylog-server").is_running is True
