
def test_service_elasticsearch_running(host):
    assert host.service("elasticsearch").is_running is True

def test_service_mongodb_running(host):
    assert host.service("mongod").is_running is True

def test_is_graylog_installed(host):
    assert host.package('graylog-server').is_installed

def test_service_graylog_running(host):
    assert host.service("graylog-server").is_running is True
