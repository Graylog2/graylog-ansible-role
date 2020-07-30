import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

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
