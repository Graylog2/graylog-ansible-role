import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import testinfra.utils.ansible_runner

@pytest.mark.usefixtures("chromedriver")
class TestGraylog():
    def test_title(self, chromedriver):
        print("Verify title...")
        assert "Graylog - Getting started" in chromedriver.title
