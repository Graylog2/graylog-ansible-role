Description
-----------

Ansible role which installs and configures Graylog log management.

Dependencies
------------

- Ansible 2.0 or higher.
- [MongoDB](https://github.com/UnderGreen/ansible-role-mongodb)
- [Elasticsearch](https://github.com/f500/ansible-elasticsearch)
- [Nginx](https://github.com/jdauphant/ansible-role-nginx)
- Tested on Ubuntu 14.04 and Debian 7

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
    elasticsearch_version: '2.x'
    elasticsearch_cluster_name: 'graylog'
    elasticsearch_network_host: '0.0.0.0'
    elasticsearch_gateway_type: ''
    elasticsearch_gateway_expected_nodes: 1
    graylog_web_endpoint_uri: 'http://127.0.0.1:9000/api/'

  roles:
    - role: Graylog2.graylog-ansible-role
      tags: graylog
```

- Fetch this role `ansible-galaxy install -p ./roles Graylog2.graylog-ansible-role`
- Install role's dependencies `ansible-galaxy install -r roles/Graylog2.graylog-ansible-role/requirements.yml -p ./roles`
- Run the playbook with `ansible-playbook your_playbook.yml -i "127.0.0.1,"`
- Login to Graylog by opening `http://<host IP>:9000` in your browser. Default username and password is `admin`

Variables
--------

```yaml
    # Basic server settings
    graylog_is_master:          'true'
    graylog_password_secret:    '2jueVqZpwLLjaWxV' # generate with: pwgen -s 96 1
    graylog_root_password_sha2: '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918' # generate with: echo -n yourpassword | shasum -a 256

    # Elasticsearch message retention
    graylog_elasticsearch_max_docs_per_index:    20000000
    graylog_elasticsearch_max_number_of_indices: 20
    graylog_elasticsearch_shards:                4
    graylog_elasticsearch_replicas:              0

    graylog_rest_listen_uri:  'http://0.0.0.0:9000/api/'
    graylog_web_listen_uri:   'http://0.0.0.0:9000/'
    graylog_web_endpoint_uri: 'http://127.0.0.1:9000/api/'
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
    elasticsearch_cluster_name: 'graylog'
    elasticsearch_timezone: 'UTC'
    elasticsearch_version: '2.x'
    elasticsearch_discovery_zen_ping_unicast_hosts: '127.0.0.1:9300'
    elasticsearch_gateway_type: ''
    elasticsearch_network_host: '0.0.0.0'
    elasticsearch_network_bind_host: ''
    elasticsearch_network_publish_host: ''
    elasticsearch_index_number_of_shards: '4'
    elasticsearch_index_number_of_replicas: '0'
    elasticsearch_gateway_recover_after_nodes: '1'
    elasticsearch_gateway_expected_nodes: '1'
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

  roles:
    - role: 'Graylog2.graylog-ansible-role'
      tags: graylog
```

- Run the playbook with `ansible-playbook -i inventory_file your_playbook.yml`
- Login to Graylog by opening `http://<host IP>` in your browser, default username and password is `admin`

License
-------

Author: Marius Sturm (<marius@graylog.com>) and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

License: Apache 2.0
