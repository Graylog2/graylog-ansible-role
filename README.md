[![Galaxy](https://img.shields.io/badge/galaxy-graylog--ansible--role-blue)](https://galaxy.ansible.com/Graylog2/graylog) ![Ansible](https://img.shields.io/ansible/role/d/56392.svg) ![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F56392%2F&query=$.min_ansible_version) ![Ansible](https://img.shields.io/ansible/quality/56392)

# Graylog Ansible Role

## Requirements

- Ansible (> 2.5.0)
- At least 4gb of memory on the target instance.
- Linux
  - Currently tested against Ubuntu 20.04 and Centos 8

To install the role, run:

    ansible-galaxy install graylog2.graylog



## Dependencies

Graylog has the following dependencies:
  - Java
  - [Elasticsearch](https://github.com/elastic/ansible-elasticsearch)
  - MongoDB

See the official [Graylog documentation](https://docs.graylog.org/docs/installing) for more details on these requirements.

Be certain you are running a supported version of Elasticsearch. You can configure what version of Elasticsearch Ansible will install with the `es_version` variable. Running Graylog against an unsupported version of Elasticsearch can break your instance!

**Compatibility Matrix**

| Graylog version   | 3.x | 4.x |
|:--------------|:-------------:|:-------------:|
| Elasticsearch | 5-6 | 6.8 - 7.10 |


You will need to these Ansible role dependencies:
  - [Java](https://github.com/lean-delivery/ansible-role-java)
  - [Elasticsearch](https://github.com/elastic/ansible-elasticsearch).

To install them, run:

    ansible-galaxy install -r <GRAYLOG ROLE_DIRECTORY>/requirements.yml





## Example Playbook

Here is an example playbook that uses this role. This is a single-instance configuration. It installs Java, MongoDB, Elasticsearch, and Graylog onto the same server.

```yaml
- hosts: "all"
  remote_user: "ubuntu"
  become: True
  vars:
    #Elasticsearch vars
    es_major_version: "7.x"
    es_version: "7.10.2"
    es_enable_xpack: False
    es_instance_name: "graylog"
    es_heap_size: "1g"
    es_config:
      node.name: "graylog"
      cluster.name: "graylog"
      http.port: 9200
      transport.tcp.port: 9300
      network.host: "127.0.0.1"
      discovery.seed_hosts: "localhost:9300"
      cluster.initial_master_nodes: "graylog"
    oss_version: True
    es_action_auto_create_index: False

    #Graylog vars
    graylog_version: 4.2
    graylog_install_java: True
    graylog_password_secret: "" # Insert your own here. Generate with: pwgen -s 96 1
    graylog_root_password_sha2: "" # Insert your own root_password_sha2 here.
    graylog_http_bind_address: "{{ ansible_default_ipv4.address }}:9000"
    graylog_http_publish_uri: "http://{{ ansible_default_ipv4.address }}:9000/"
    graylog_http_external_uri: "http://{{ ansible_default_ipv4.address }}:9000/"

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


## Role Variables

A list of all available role variables is documented [here](docs/Variables.md).

## Testing

We run smoke tests for Graylog using this role. Documentation on that can be found [here](docs/Testing.md)

## Author Information

Author: Marius Sturm (<marius@graylog.com>) and [contributors](https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors)

## License

Apache 2.0
