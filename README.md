[![Build Status](https://travis-ci.org/Graylog2/graylog-ansible-role.svg?branch=master)](https://travis-ci.org/Graylog2/graylog-ansible-role) [![Galaxy](https://img.shields.io/badge/galaxy-graylog--ansible--role-blue)](https://galaxy.ansible.com/graylog2/graylog-ansible-role) ![Ansible](https://img.shields.io/ansible/role/d/11230.svg) ![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F11230%2F&query=$.min_ansible_version) ![Ansible](https://img.shields.io/ansible/quality/11230)

Description
-----------

An Ansible role which installs and configures [Graylog](https://docs.graylog.org) for log management.


Dependencies
------------

- **Only Ansible versions > 2.5.0 are supported.**
- Java 8 - Ubuntu Xenial and up support OpenJDK 8 by default. For other distributions, consider backports accordingly
- [Elasticsearch][1]
- Tested on
  - Ubuntu 16.04
  - Ubuntu 18.04
  - Ubuntu 20.04
  - Debian 9
  - Debian 10
  - Centos 7
  - Centos 8

If you require Nginx to be installed, include the official [Nginx][2] role in your playbook.


Usage
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
    - role: "graylog2.graylog-ansible-role"
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
graylog_version: 4.0     # Required
graylog_full_version: "4.0.6-1" # Optional, if not provided, the latest revision of {{ graylog_version }} will be installed
graylog_is_master: "True"
graylog_password_secret: "2jueVqZpwLLjaWxV" # generate with: pwgen -s 96 1
graylog_root_password_sha2: "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
```

Take a look into `defaults/main.yml` to get an overview of all configuration parameters.

If you need to configure a graylog setting that we haven't set up, you can use `graylog_additional_config` to declare it:

```yaml
graylog_additional_config:
  elasticsearch_discovery_default_user: my_username
  elasticsearch_discovery_default_password: "{{ my_password }}"
```


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
    graylog_version: 4.0
    graylog_install_java: False # Elasticsearch role already installed Java
    graylog_password_secret: "2jueVqZpwLLjaWxV" # generate with: pwgen -s 96 1
    graylog_root_password_sha2: "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
    graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"

  roles:
    - role: "graylog2.graylog-ansible-role"
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

  roles:
    - role: lean_delivery.java
      version: 7.1.0
      when: graylog_install_java

    - role: "elastic.elasticsearch"
      tags:
        - "elasticsearch"
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

If you'd like to run the Molecule tests, you'll need a few things installed:

- [Vagrant](https://www.vagrantup.com/docs/installation)
- [libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt)
- [Molecule](https://molecule.readthedocs.io/en/latest/installation.html)
- [testinfra](https://testinfra.readthedocs.io/en/latest/)

Note that this is ONLY required if you want to run the test harness. You don't need any of this to run the playbook. This is a special setup that allows you to test the Ansible playbook against disposable VMs.

#### Install Notes

Setting up Molecule requires installing a number tools for the VM enviroment. The following are notes from a successful install on Ubuntu 20.04.

Install Virtualenv, Molecule, and testinfra

    sudo apt-get update
    sudo apt-get install -y python3-pip libssl-dev python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    python3 -m pip install "molecule[lint]"
    pip3 install testinfra

Install Vagrant and libvirt

    sudo apt-get install -y bridge-utils dnsmasq-base ebtables libvirt-bin libvirt-dev qemu-kvm qemu-utils ruby-dev
    sudo wget -nv https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
    sudo dpkg -i vagrant_2.2.9_x86_64.deb
    vagrant --version
    sudo apt-get install ruby-libvirt qemu libvirt-daemon-system libvirt-clients ebtables
    sudo apt-get install libxslt-dev libxml2-dev libvirt-dev zlib1g-dev
    vagrant plugin install vagrant-libvirt
    vagrant plugin list
    pip3 install python-vagrant molecule-vagrant

Test that Vagrant works

    vagrant init generic/ubuntu1804
    vagrant up --provider=libvirt
    vagrant ssh
    vagrant halt

Test that Molecule works

    git clone https://github.com/Graylog2/graylog-ansible-role.git
    cd graylog-ansible-role
    molecule create
    molecule converge
    molecule login
    systemctl status graylog-server
    exit
    molecule destroy

#### Commands

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
    export MOLECULE_DISTRO='generic/ubuntu2004'


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
[2]: https://github.com/nginxinc/ansible-role-nginx
[3]: https://github.com/Graylog2/graylog-ansible-role/blob/master/meta/main.yml
[4]: https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors
[5]: https://pablodav.github.io/post/graylog/graylog_ansible
[6]: https://pablodav.github.io/post/graylog/logstash_input
[7]: https://pablodav.github.io/post/graylog/graylog_logstash_nagios_nsca
