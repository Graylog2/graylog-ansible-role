[![Galaxy](https://img.shields.io/badge/galaxy-graylog--ansible--role-blue)](https://galaxy.ansible.com/Graylog2/graylog) [![CI](https://github.com/Graylog2/graylog-ansible-role/actions/workflows/ci.yml/badge.svg)](https://github.com/Graylog2/graylog-ansible-role/actions/workflows/ci.yml) ![Ansible](https://img.shields.io/ansible/role/d/56392.svg) ![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F56392%2F&query=$.min_ansible_version) ![Ansible](https://img.shields.io/ansible/quality/56392)


# Graylog Ansible Role

## Requirements

- Ansible 11.2.0
- Python 3.12
- At least 4gb of memory on the target instance.
  - Linux
    - Currently tested against:
        - Ubuntu 18.04
        - Ubuntu 20.04
        - Ubuntu 22.04
        - Ubuntu 24.04
        - Centos 7
        - Centos 8
        - Centos 9

To install the role, run:

    ansible-galaxy install graylog2.graylog



## Dependencies

Graylog has the following dependencies:
  - Java
  - OpenSearch
  - MongoDB

See the official [Graylog documentation](https://docs.graylog.org/docs/installing) for more details on these requirements.

Be certain you are running a supported version of OpenSearch.

**Compatibility Matrix**

| Graylog version   | 3.x |    4.x     | 5.x | 6.x |
|:--------------|:-------------:|:----------:|:-------------:|:-------------:|
| Elasticsearch | 5-6 | 6.8 - 7.10 | 6.8 - 7.10 | n/a |
 | OpenSearch | |    1.x*    | 1.x - 2.x | 1.x - 2.x |
*Graylog 4.3.x introduces support for OpenSearch.

Refer to the [Software Interoperability Chart](https://go2docs.graylog.org/5-0/planning_your_deployment/planning_your_upgrade_to_opensearch.htm)

You will need to these Ansible role dependencies:
  - [Java](https://github.com/lean-delivery/ansible-role-java)

To install it, run:

    ansible-galaxy install -r <GRAYLOG ROLE_DIRECTORY>/requirements.yml





## Example Playbook

Here is an example playbook that uses this role. This is a single-instance configuration. It installs Java, MongoDB, Elasticsearch, and Graylog onto the same server.

```yaml
    # Graylog vars
    graylog_version: 6.1
    graylog_install_java: True
    graylog_password_secret: "" # Insert your own here. Generate with: pwgen -s 96 1
    graylog_root_password_sha2: "" # Insert your own root_password_sha2 here.
    graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
    graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_install_open_package: True
    graylog_install_enterprise_package: False

  roles:
    - role: "graylog2.graylog"
      tags:
        - "graylog"
```

Remember to generate a unique `password_secret` and `root_password_sha2` for your instance.

To generate `password_secret`:

    pwgen -s 96 1

To generate `root_password_sha2`:

      echo -n "Enter Password: " && head -1 </dev/stdin | tr -d '\n' | sha256sum | cut -d" " -f1


## Example Playbook - Cluster

Here is an example that deploys a Graylog cluster, like the one mentioned on the [architecture page](https://docs.graylog.org/docs) of our documentation.

In our Ansible hosts file, we have 3 instances for a Graylog cluster:

```
[graylog]
graylog01
graylog02
graylog03
```

First, deploy an [OpenSearch](https://opensearch.org/) cluster.

Next, deploy three MongoDB instances and configure them as a Replica Set. This can be done with the [MongoDB community collection](https://github.com/ansible-collections/community.mongodb).

These MongoDB instances can live on the Graylog servers, as they are not expected to consume much resources.

Again, this doesn't configure authentication in MongoDB. You may want that for a production cluster.

```yaml
- hosts: "graylog"
  vars:
    mongodb_version: "4.4"
    bind_ip: "0.0.0.0"
    repl_set_name: "rs0"
    authorization: "disabled"
  roles:
    - community.mongodb.mongodb_repository
    - community.mongodb.mongodb_mongod
  tasks:
    - name: "Start MongoDB"
      service:
        name: "mongod"
        state: "started"
        enabled: "yes"

- hosts: "graylog01"
  tasks:
    - name: "Install PyMongo"
      apt:
        update_cache: yes
        name: "python3-pymongo"
        state: "latest"
    - name: Configure replicaset
      community.mongodb.mongodb_replicaset:
        login_host: "localhost"
        replica_set: "rs0"
        members:
        - graylog01
        - graylog02
        - graylog03
```

Finally, install Graylog.

```yaml
- hosts: "graylog"
  vars:
    graylog_is_master: "{{ True if ansible_hostname == 'graylog01' else False }}"
    graylog_version: 6.1
    graylog_install_java: False
    graylog_password_secret: "" # Insert your own here. Generate with: pwgen -s 96 1
    graylog_root_password_sha2: "" # Insert your own root_password_sha2 here.
    graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
    graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_elasticsearch_hosts: "http://elasticsearch01:9200,http://elasticsearch02:9200,http://elasticsearch03:9200"
    graylog_mongodb_uri: "mongodb://graylog01:27017,graylog02:27017,graylog03:27017/graylog"

  roles:
    - role: "graylog2.graylog"
```

The full example can be seen [here](molecule/example2/converge.yml). Our [documentation](https://docs.graylog.org/v1/docs/multinode-setup) has more in-depth advice on configuring a multi-node Graylog setup.


## Role Variables

A list of all available role variables is documented [here](docs/Variables.md).

## Testing

We run smoke tests for Graylog using this role. Documentation on that can be found [here](docs/Testing.md)

## Author Information

Author: Graylog and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

## License

Apache 2.0
