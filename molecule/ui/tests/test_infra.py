import time

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
