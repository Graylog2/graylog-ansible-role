[![Build Status](https://travis-ci.org/Graylog2/graylog-ansible-role.svg?branch=master)](https://travis-ci.org/Graylog2/graylog-ansible-role)

Description
-----------

Ansible role which installs and configures Graylog log management.

**THIS ROLE IS FOR GRAYLOG-3.X ONLY! FOR OLDER VERSIONS USE THE `GRAYLOG-2.X` BRANCH!**

Dependencies
------------

- **Only Ansible versions > 2.2.0 are supported.**
- Java 8 - Ubuntu Xenial and up support OpenJDK 8 by default. For other distributions consider backports accordingly
- [Elasticsearch][1]
- [NGINX][2]
- Tested on Ubuntu 16.04 / Ubuntu 18.04 / Debian 9 / Centos 7

Quickstart
----------

- You need at least 4GB of memory to run Graylog
- Generate the password hash for the admin user:
  - `echo -n yourpassword | sha256sum     # Linux`
  - `echo -n yourpassword | shasum -a 256 # Mac`

Here is an example of a playbook targeting Vagrant (Ubuntu Xenial):

```yaml
- hosts: "all"
  remote_user: "ubuntu"
  become: True
  vars:
    es_enable_xpack: False
    es_instance_name: "graylog"
    es_heap_size: "1g"
    es_config:
      node.name: "graylog"
      cluster.name: "graylog"
      http.port: 9200
      transport.tcp.port: 9300
      network.host: "127.0.0.1"
    graylog_install_java: False # Elasticsearch role already installed Java
    graylog_password_secret: "2jueVqZpwLLjaWxV" # generate with: pwgen -s 96 1
    graylog_root_password_sha2: "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
    graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
  roles:
    - role: "Graylog2.graylog-ansible-role"
      tags:
        - "graylog"
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
graylog_server_version:     "3.0.1-1" # Optional, if not provided the latest version will be installed
graylog_is_master:          "True"
graylog_password_secret:    "2jueVqZpwLLjaWxV" # generate with: pwgen -s 96 1
graylog_root_password_sha2: "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
```

Take a look into `defaults/main.yml` to get an overview of all configuration parameters.

More detailed example
---------------------

- Set up `roles_path = ./roles` in `ansible.cfg` (`[defaults]` block)
- Install role `ansible-galaxy install Graylog2.graylog-ansible-role`
- Install role's dependencies `ansible-galaxy install -r roles/Graylog2.graylog-ansible-role/requirements.yml`
- Set up playbook (see example below):

```yaml
- hosts: "server"
  become: True
  vars:
    es_instance_name: "graylog"
    es_scripts: False
    es_templates: False
    es_version_lock: False
    es_heap_size: "1g"
    es_config:
      node.name: "graylog"
      cluster.name: "graylog"
      http.port: 9200
      transport.tcp.port: 9300
      network.host: "127.0.0.1"
      node.data: True
      node.master: True
    graylog_install_java: False # Elasticsearch role already installed Java
    graylog_password_secret: "2jueVqZpwLLjaWxV" # generate with: pwgen -s 96 1
    graylog_root_password_sha2: "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
    graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"

    nginx_sites:
      graylog:
        - "listen 80"
        - "server_name graylog"
        - |
          location / {
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
            client_body_buffer_size 128k;
          }

  roles:
    - role: "Graylog2.graylog-ansible-role"
      tags:
        - "graylog"
```

- Run the playbook with `ansible-playbook -i inventory_file your_playbook.yml`
- Login to Graylog by opening `http://<host IP>` in your browser, default username and password is `admin`

Explicit playbook of roles
--------------------------

It's good to be explicit, these are all the roles that you need to run for Graylog.

Note: in this example vars are in a more appropriate place at `group_vars/group/vars`

```yaml
- name: "Apply roles for Graylog servers"
  hosts: "graylog_servers"
  become: True
  vars:
    graylog_install_elasticsearch: False
    graylog_install_mongodb:       False
    graylog_install_nginx:         False

  roles:

    - role: "elastic.elasticsearch"
      tags:
        - "elasticsearch"
        - "graylog_servers"

    - role: "jdauphant.nginx"
      tags:
        - "nginx"
        - "graylog_servers"

    - role: "Graylog2.graylog-ansible-role"
      tags:
        - "graylog"
        - "graylog_servers"
```

Conditional role dependencies
-----------------------------

Dependencies can be enabled/disabled with the `host_vars` `graylog_install_*`.
Take look into [meta/main.yml][3] for more information. Keep in mind that you
have to install all dependencies even when they are disabled to prevent errors.

Tests
-----

One can test the role on the supported distributions (see `meta/main.yml` for the complete list),
by using the Docker images provided.

Example for Debian Jessie and Ubuntu Xenial:

    $ cd graylog-ansible-role
    $ docker build -t graylog-ansible-role-jessie -f tests/support/jessie_22.Dockerfile tests/support
    $ docker run -it -v $PWD:/role graylog-ansible-role-jessie

For Xenial, just replace `jessie` with `xenial` in the above commands.

Example for CentOS 7 and Ubuntu Xenial:

Due to how `systemd` works with Docker, the following approach is suggested:

    $ cd graylog-ansible-role
    $ docker build -t graylog-ansible-role-centos7 -f tests/support/centos7_22.Dockerfile tests/support
    $ docker run -d --privileged -it -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $PWD:/role:ro graylog-ansible-role-centos7 /usr/sbin/init
    $ DOCKER_CONTAINER_ID=$(docker ps | grep centos | awk '{print $1}')
    $ docker logs $DOCKER_CONTAINER_ID
    $ docker exec -it $DOCKER_CONTAINER_ID /bin/bash -xec "bash -x run-tests.sh"
    $ docker ps -a
    $ docker stop $DOCKER_CONTAINER_ID
    $ docker rm -v $DOCKER_CONTAINER_ID

Ubuntu Xenial:

    $ cd graylog-ansible-role
    $ docker build -t graylog-ansible-role-xenial -f tests/support/xenial_22.Dockerfile tests/support
    $ docker run -d --privileged -it -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $PWD:/role:ro graylog-ansible-role-xenial /sbin/init
    $ DOCKER_CONTAINER_ID=$(docker ps | grep xenial | awk '{print $1}')
    $ docker logs $DOCKER_CONTAINER_ID
    $ docker exec -it $DOCKER_CONTAINER_ID /bin/bash -xec "bash -x run-tests.sh"
    $ docker ps -a
    $ docker stop $DOCKER_CONTAINER_ID
    $ docker rm -v $DOCKER_CONTAINER_ID

Further Reading
----------------

Great articles by Pablo Daniel Estigarribia Davyt on how to use this role:

- [Install Graylog][5]
- [Receive messages from Logstash][6]
- [Monitor Graylog with NSCA][7]

License
-------

Author: Marius Sturm (<marius@graylog.com>) and [contributors][4]

License: Apache 2.0

[1]: https://github.com/elastic/ansible-elasticsearch
[2]: https://github.com/jdauphant/ansible-role-nginx
[3]: https://github.com/Graylog2/graylog-ansible-role/blob/master/meta/main.yml
[4]: https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors
[5]: https://pablodav.github.io/post/graylog/graylog_ansible
[6]: https://pablodav.github.io/post/graylog/logstash_input
[7]: https://pablodav.github.io/post/graylog/graylog_logstash_nagios_nsca
