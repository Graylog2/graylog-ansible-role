import pytest
import os

class TestGraylog():
    url = 'http://localhost:9000'

    def test_title(self, chromedriver):
        print("Verify title...")
        assert "Graylog - Getting started" in chromedriver.title

    def test_version(self, chromedriver):
        print('Checking if version is ' + os.environ['GRAYLOG_VERSION'] + '...')

        chromedriver.get(self.url + "/system/overview")
        assert 'Graylog ' + os.environ['GRAYLOG_VERSION'] in chromedriver.find_element_by_xpath('//footer').text
