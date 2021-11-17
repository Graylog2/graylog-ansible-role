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
from selenium.common.exceptions import NoSuchElementException

def test_service_elasticsearch_running(host):
    print("\nEnsure Elasticsearch is running...")
    assert host.service("elasticsearch").is_running is True

def test_service_mongodb_running(host):
    print("Ensure MongoDB is running...")
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
        assert os.environ['GRAYLOG_VERSION'] in plugin['version']

      if plugin['name'] == 'Integrations':
        integrations_plugin_loaded = True
        assert os.environ['GRAYLOG_VERSION'] in plugin['version']

      if plugin['name'] == 'Graylog Enterprise':
        enterprise_integrations_plugin_loaded = True
        assert os.environ['GRAYLOG_VERSION'] in plugin['version']

    assert enterprise_plugin_loaded is True
    assert integrations_plugin_loaded is True
    assert enterprise_integrations_plugin_loaded is True
