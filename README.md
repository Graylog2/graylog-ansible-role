Description
-----------

Ansible role which installs and configures Graylog log management.


Dependencies
------------

- Ansible 1.6 or higher.
- [MongoDB](https://github.com/lesmyrmidons/ansible-role-mongodb)
- [Elasticsearch](https://github.com/f500/ansible-elasticsearch)
- Tested on Ubuntu 14.04 and Debian 7

Variables
--------

```yaml
# Basic server settings
is_master: 'true'
password_secret: 2jueVqZpwLLjaWxV # generate with pwgen -s 96 1
root_password_sha2: 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918

# Elasticsearch
graylog_elasticsearch_max_docs_per_index: 20000000
graylog_elasticsearch_max_number_of_indices: 20
graylog_elasticsearch_shards: 4
graylog_elasticsearch_replicas: 0

# Basic web interface settings
web_server_uri: http://127.0.0.1:12900
web_secret: 2jueVqZpwLLjaWxV # generate with pwgen -s 96 1
```

Take a look into `defaults/main.yml` to get an overview of all configuration parameters

# Single host example
- Set up `roles_path = ./roles` in `ansible.cfg` (`[defaults]` block)
- Install role and dependencies `ansible-galaxy install graylog2.graylog`
- Set up playbook (see example below):

 ```yaml
 # main.yml
 ---
 - hosts: web
   sudo: yes
   vars:
    elasticsearch_cluster_name: 'graylog2'
    elasticsearch_timezone: 'UTC'
    elasticsearch_version: '1.4'
    elasticsearch_discovery_zen_ping_multicast_enabled: 'false'
    elasticsearch_discovery_zen_ping_unicast_hosts: '127.0.0.1:9300'
    elasticsearch_network_host: ''
    elasticsearch_network_bind_host: ''
    elasticsearch_network_publish_host: ''
    elasticsearch_index_number_of_shards: '4'
    elasticsearch_index_number_of_replicas: '0'
    elasticsearch_gateway_recover_after_nodes: '1'
    elasticsearch_gateway_expected_nodes: '1'

   roles:
     - { role: 'graylog2.graylog', tags: 'graylog' }
 ```
- Run the playbook with `ansible-playbook -i inventory_file main.yml`
- Login to Graylog by opening `http://<host IP>:9000` in your browser, default username and password is `admin`

License
-------

Author: Marius Sturm (<marius@graylog.com>) and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

License: Apache 2.0
