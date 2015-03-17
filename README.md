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
- Download dependencies `ansible-galaxy install -r requirements.yml`
- Edit `inventory.ini` file, put your server IP and username in
- run ansible with `ansible-playbook -i inventory.ini main.yml`
- Login to Graylog by opening `http://<host IP>:9000` in your browser, default username and password is `admin`

License
-------

Author: Marius Sturm (<marius@graylog.com>) and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

License: Apache 2.0
