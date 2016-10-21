#!/bin/bash
set -e

ansible-galaxy install -r role/requirements.yml -p /

cd /role/tests
ansible-playbook graylog.yml

# running a second time to verify playbook's idempotence
set +e
ansible-playbook graylog.yml > /tmp/second_run.log
{
    cat /tmp/second_run.log | tail -n 5 | grep 'changed=0' &&
    echo 'Playbook is idempotent'
} || {
    cat /tmp/second_run.log
    echo 'Playbook is **NOT** idempotent'
    exit 1
}
