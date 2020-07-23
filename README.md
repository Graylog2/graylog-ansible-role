[![Build Status](https://travis-ci.org/Graylog2/graylog-ansible-role.svg?branch=master)](https://travis-ci.org/Graylog2/graylog-ansible-role) [![Galaxy](https://img.shields.io/badge/galaxy-graylog--ansible--role-blue)](https://galaxy.ansible.com/graylog2/graylog-ansible-role) ![Ansible](https://img.shields.io/ansible/role/d/11230.svg) ![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F11230%2F&query=$.min_ansible_version) ![Ansible](https://img.shields.io/ansible/quality/11230)

Description
-----------

An Ansible role which installs and configures [Graylog](https://docs.graylog.org) for log management.

Changelog
---
####  v3.3

- **Breaking changes**:
  - The `graylog_version` variable must now be explicitly declared.
  - Renamed the optional `graylog_server_version` variable to `graylog_full_version`. If not set, it will pull the latest `graylog_version` defined.
  - Increased the minimum Ansible version from 2.2 to 2.5.
  - No longer testing the Ansible role against Debian Jessie.
- New stuff:
  - Added ability to supply arbitrary key/values for server config [PR #142](https://github.com/Graylog2/graylog-ansible-role/pull/142)

    Example:

    ```
    graylog_additional_config:
      test: value   
    ```
- Fixes:
  - Only enable permission if SELInux is actually enabled - [PR #121](https://github.com/Graylog2/graylog-ansible-role/pull/121)
  - Make sure graylog-server directories exist - [PR #134](https://github.com/Graylog2/graylog-ansible-role/pull/134)
  - Fixed missing policycoreutils-python package on Centos 7 - [Issue #119](https://github.com/Graylog2/graylog-ansible-role/issues/119)



Dependencies
------------

- **Only Ansible versions > 2.5.0 are supported.**
- Java 8 - Ubuntu Xenial and up support OpenJDK 8 by default. For other distributions consider backports accordingly
- [Elasticsearch][1]
- [NGINX][2]
- Tested on Ubuntu 16.04 / Ubuntu 18.04 / Debian 9 / Debian 10 / Centos 7 / Centos 8
- This role is for Graylog-3.X only!
  - For older versions, use the graylog-2.X branch.

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
    graylog_version: 3.3
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
graylog_version: 3.3     # Required
graylog_full_version: "3.3.2-1" # Optional, if not provided, the latest revision of {{ graylog_version }} will be installed
graylog_is_master: "True"
graylog_password_secret: "2jueVqZpwLLjaWxV" # generate with: pwgen -s 96 1
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
    graylog_version: 3.3
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
    - role: lean_delivery.java
      version: 7.1.0
      when: graylog_install_java

    - role: "elastic.elasticsearch"
      tags:
        - "elasticsearch"
        - "graylog_servers"

    - role: "jdauphant.nginx"
      tags:
        - "nginx"
        - "graylog_servers"

    - role: "graylog2.graylog-ansible-role"
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

If you'd like to test the role out using our test suite, you'll need a few things installed:

- [Vagrant](https://www.vagrantup.com/docs/installation)
- [libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt)
- [Molecule](https://molecule.readthedocs.io/en/latest/installation.html)
- [testinfra](https://testinfra.readthedocs.io/en/latest/)

To spin up a test VM:

    export MOLECULE_DISTRO='generic/ubuntu1804'
    molecule create

To run the Ansible playbook:

    molecule converge

To login to the VM:

    molecule login

To destroy the VM:

    molecule destroy

To test against other distros, you can also set the MOLECULE_DISTRO environment variable to one of these:

    export MOLECULE_DISTRO='centos/7'
    export MOLECULE_DISTRO='centos/8'
    export MOLECULE_DISTRO='debian/jessie64'
    export MOLECULE_DISTRO='debian/stretch64'
    export MOLECULE_DISTRO='debian/buster64'
    export MOLECULE_DISTRO='generic/ubuntu1604'
    export MOLECULE_DISTRO='generic/ubuntu1804'


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
