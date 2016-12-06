[![Build Status](https://travis-ci.org/Graylog2/graylog-ansible-role.svg?branch=master)](https://travis-ci.org/Graylog2/graylog-ansible-role)

Description
-----------

Ansible role which installs and configures Graylog log management.

Dependencies
------------

- Ansible 2.0 or higher.
- [MongoDB](https://github.com/UnderGreen/ansible-role-mongodb)
- [Elasticsearch](https://github.com/elastic/ansible-elasticsearch)
- [Nginx](https://github.com/jdauphant/ansible-role-nginx)
- Tested on Ubuntu 14.04 / Debian 7 / Centos 7

Quickstart
----------

- You need at least 4GB of memory to run Graylog
- Here is an example of a playbook targeting Vagrant box(es):

```yaml
---
- hosts: all
  remote_user: vagrant
  become: True

  vars:
    es_instance_name: 'graylog'
    es_scripts: False
    es_templates: False
    es_version_lock: False
    es_heap_size: 1g

    es_config: {
      node.name: "graylog",
      cluster.name: "graylog",
      discovery.zen.ping.unicast.hosts: "localhost:9301",
      http.port: 9200,
      transport.tcp.port: 9300,
      network.host: 0.0.0.0,
      node.data: true,
      node.master: true,
      bootstrap.mlockall: false,
      discovery.zen.ping.multicast.enabled: false
    }
    graylog_web_endpoint_uri: 'http://127.0.0.1:9000/api/'

  roles:
    - role: 'Graylog2.graylog-ansible-role'
      tags: graylog
```

- Create a playbook file with that content, e.g. `your_playbook.yml`
- Fetch this role `ansible-galaxy install -n -p ./roles Graylog2.graylog-ansible-role`
- Install role's dependencies `ansible-galaxy install -r roles/Graylog2.graylog-ansible-role/requirements.yml -p ./roles`
- Apply the playbook to a Vagrant box `ansible-playbook your_playbook.yml -i "127.0.0.1:2222,"`
- Login to Graylog by opening `http://127.0.0.1:9000` in your browser. Default username and password is `admin`

Variables
--------

```yaml
# Basic server settings
graylog_is_master:          'True'
graylog_password_secret:    '2jueVqZpwLLjaWxV' # generate with: pwgen -s 96 1
graylog_root_password: 'pwd'

# Elasticsearch message retention
graylog_elasticsearch_max_docs_per_index:    20000000
graylog_elasticsearch_max_number_of_indices: 20
graylog_elasticsearch_shards:                4
graylog_elasticsearch_replicas:              0

graylog_rest_listen_uri:  'http://0.0.0.0:9000/api/'
graylog_web_listen_uri:   'http://0.0.0.0:9000/'
graylog_web_endpoint_uri: 'http://127.0.0.1:9000/api/'

# Plugins
# Permet de passer l'étape
graylog_skip_plugins_installation: false
# Name pour le nom du jar, url pour l'url de téléchargememnt, toDelete pour retirer le plugin
graylog_plugins:
  - name: 'graylog-plugin-pagerduty-1.3.0.jar'
    url: https://github.com/Graylog2/graylog-plugin-pagerduty/releases/download/1.3.0/graylog-plugin-pagerduty-1.3.0.jar
    toDelete: false
```

Take a look into `defaults/main.yml` to get an overview of all configuration parameters.

More detailed example
---------------------

- Set up `roles_path = ./roles` in `ansible.cfg` (`[defaults]` block)
- Install role `ansible-galaxy install Graylog2.graylog-ansible-role`
- Install role's dependencies `ansible-galaxy install -r roles/Graylog2.graylog-ansible-role/requirements.yml`
- Set up playbook (see example below):

```yaml
# your_playbook.yml
---
- hosts: server
  become: True
  vars:
    es_instance_name: 'graylog'
    es_scripts: False
    es_templates: False
    es_version_lock: False
    es_heap_size: 1g

    es_config: {
      node.name: "graylog",
      cluster.name: "graylog",
      discovery.zen.ping.unicast.hosts: "localhost:9301",
      http.port: 9200,
      transport.tcp.port: 9300,
      network.host: 0.0.0.0,
      node.data: true,
      node.master: true,
      bootstrap.mlockall: false,
      discovery.zen.ping.multicast.enabled: false
    }
    graylog_web_endpoint_uri: 'http://127.0.0.1:9000/api/'

    nginx_sites:
      graylog:
        - listen 80
        - server_name graylog
        - location / {
          proxy_pass http://localhost:9000/;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_pass_request_headers on;
          proxy_connect_timeout 150;
          proxy_send_timeout 100;
          proxy_read_timeout 100;
          proxy_buffers 4 32k;
          client_max_body_size 8m;
          client_body_buffer_size 128k; }

    graylog_inputs:
      - type: 'org.graylog2.inputs.syslog.tcp.SyslogTCPInput'
        port: 8514
        title: 'Syslog TCP 8514'
  roles:
    - role: 'Graylog2.graylog-ansible-role'
      tags: graylog
```

- Run the playbook with `ansible-playbook -i inventory_file your_playbook.yml`
- Login to Graylog by opening `http://<host IP>` in your browser, default username and password is `admin`

# Tests

One can test the role on the supported distributions (see `meta/main.yml` for the complete list),
by using the Docker images provided.

Example for Debian Wheezy and Ubuntu Trusty:

```
$ cd graylog-ansible-role
$ docker build -t graylog-ansible-role-wheezy -f tests/support/wheezy.Dockerfile tests/support
$ docker run -it -v $PWD:/role graylog-ansible-role-wheezy
```

For Trusty, just replace `wheezy` with `trusty` in the above commands.

Example for CentOS 7:

Due to how `systemd` works with Docker, the following approach is suggested:

```
$ cd graylog-ansible-role
$ docker build -t graylog-ansible-role-centos7 -f tests/support/centos7.Dockerfile tests/support
$ docker run -d --privileged -it -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $PWD:/role:ro graylog-ansible-role-centos7 /usr/sbin/init
$ DOCKER_CONTAINER_ID=$(docker ps | grep centos | awk '{print $1}')
$ docker logs $DOCKER_CONTAINER_ID
$ docker exec -it $DOCKER_CONTAINER_ID /bin/bash -xec "bash -x run-tests.sh"
$ docker ps -a
$ docker stop $DOCKER_CONTAINER_ID
$ docker rm -v $DOCKER_CONTAINER_ID
```

License
-------

Author: Marius Sturm (<marius@graylog.com>) and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

License: Apache 2.0
