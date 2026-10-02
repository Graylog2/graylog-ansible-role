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

def test_is_graylog_installed(host):
    print("Ensure graylog-server package is installed...")
    assert host.package('graylog-server').is_installed