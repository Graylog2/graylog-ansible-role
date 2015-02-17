Description
-----------

Ansible role which installs and configures Graylog log management.


Dependencies
------------

- Ansible 1.6 or higher.
- [Elasticsearch](https://github.com/Traackr/ansible-elasticsearch.git)
  - Set `elasticsearch_cluster_name: "graylog2"`
- [MongoDB](https://github.com/lesmyrmidons/ansible-role-mongodb)


Variables
--------

```yaml
# Basic server settings
is_master: 'true'
password_secret: 2jueVqZpwLLjaWxV # generate with pwgen -s 96 1
root_password_sha2: 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918

# Elasticsearch
elasticsearch_max_docs_per_index: 20000000
elasticsearch_max_number_of_indices: 20
elasticsearch_shards: 4
elasticsearch_replicas: 0

mongodb_*:

# Basic web interface settings
web_server_uri: http://127.0.0.1:12900
web_secret: 2jueVqZpwLLjaWxV # generate with pwgen -s 96 1
```

Take a look into `defaults/main.yml` to get an overview of all configuration parameters

License
-------

Author: Marius Sturm (<marius@graylog.com>) and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

License: Apache 2.0
