[![Galaxy](https://img.shields.io/badge/galaxy-graylog--ansible--role-blue)](https://galaxy.ansible.com/Graylog2/graylog) ![Ansible](https://img.shields.io/ansible/role/d/56392.svg) ![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F56392%2F&query=$.min_ansible_version) ![Ansible](https://img.shields.io/ansible/quality/56392)

# Graylog Ansible Role

## Requirements

- Ansible (> 2.5.0)

To install the role, run:

    ansible-galaxy install graylog2.graylog



## Dependencies

Graylog requires Java, [Elasticsearch][1], and MongoDB. See the official [Graylog documentation][8] for the correct versions of each of these dependencies.

If you need Nginx installed, you can include the official [Nginx][2] role in your playbook.

To install dependencies, run:

    ansible-galaxy install -r roles/graylog2.graylog/requirements.yml

> **NOTE**
> For Elasticsearch, be sure to set `es_version` to 7.10 or lower. Graylog does not support Elasticsearch 7.11 and up!



## Example Playbook



## Role Variables


## Main Variables

| Variable Name | Default Value | Description |
|---|---|---|
| graylog_version | | Required. Should be in `X.Y` format (e.g, `4.2`) |
| graylog_full_version | | Optional, if not provided, the latest revision of `graylog_version` will be installed. Should be in `X.Y.Z-rev` format (e.g, `4.2.0-3`) |
| graylog_install_java | | Whether to install Java on the instance.|
| graylog_install_elasticsearch | | Whether to install Elasticsearch on the instance. |
| graylog_install_mongodb | | Whether to install MongoDB on the instance. |



### Server.conf Variables

These variables let you configure the properties in `server.conf`. See the [offical Graylog documentation][9] for details on these setings.

| Variable Name | Default Value |
|---|---|
| graylog_is_master | True |
| graylog_node_id_file | /etc/graylog/server/node-id |
| graylog_password_secret |   |
| root_username  | admin  |
| graylog_root_password_sha2 |  |
| graylog_root_email | |
| graylog_root_timezone | UTC |
| graylog_bin_dir | /usr/share/graylog-server/bin |
| graylog_data_dir | /var/lib/graylog-server |
| graylog_plugin_dir | /usr/share/graylog-server/plugin |
| graylog_http_bind_address | 0.0.0.0:9000 |
| graylog_http_publish_uri | http://0.0.0.0:9000/ |
| graylog_http_external_uri | http://0.0.0.0:9000/ |
| graylog_http_enable_cors | True |
| graylog_http_enable_gzip | True |
| graylog_http_max_header_size | 8192 |
| graylog_http_thread_pool_size | 16 |
| graylog_http_enable_tls | False |
| graylog_http_tls_cert_file | /path/to/graylog.crt |
| graylog_http_tls_key_file | /path/to/graylog.key |
| graylog_http_tls_key_password | |
| graylog_trusted_proxies | |
| graylog_elasticsearch_hosts | http://127.0.0.1:9200 |
| graylog_elasticsearch_connect_timeout | 10s |
| graylog_elasticsearch_socket_timeout | 60s |
| graylog_elasticsearch_max_total_connections | 20 |
| graylog_elasticsearch_max_total_connections_per_route | 2 |
| graylog_elasticsearch_max_retries | 2 |
| graylog_elasticsearch_discovery_enabled | False |
| graylog_elasticsearch_discovery_frequency | 30s |
| graylog_elasticsearch_compression_enabled | False |
| graylog_rotation_strategy | count |
| graylog_elasticsearch_max_docs_per_index | 20000000 |
| graylog_elasticsearch_max_size_per_index | 1073741824 |
| graylog_elasticsearch_max_time_per_index | 1d |
| graylog_elasticsearch_disable_version_check | True |
| graylog_no_retention | False |
| graylog_elasticsearch_max_number_of_indices | 20 |
| graylog_retention_strategy | delete |
| graylog_elasticsearch_shards | 4 |
| graylog_elasticsearch_replicas | 0 |
| graylog_elasticsearch_index_prefix | graylog |
| graylog_elasticsearch_template_name | graylog-internal |
| graylog_allow_leading_wildcard_searches | False |
| graylog_allow_highlighting | False |
| graylog_elasticsearch_analyzer | standard |
| graylog_elasticsearch_request_timeout | 1m |
| graylog_elasticsearch_index_optimization_timeout | 1h |
| graylog_elasticsearch_index_optimization_jobs | 20 |
| graylog_index_ranges_cleanup_interval | 1h |
| graylog_index_field_type_periodical_interval | 1h |
| graylog_elasticsearch_output_batch_size | 500 |
| graylog_elasticsearch_output_flush_interval | 1 |
| graylog_output_fault_count_threshold | 5 |
| graylog_output_fault_penalty_seconds | 30 |
| graylog_processbuffer_processors | 5 |
| graylog_outputbuffer_processors | 3 |
| graylog_outputbuffer_processor_keep_alive_time | 5000 |
| graylog_outputbuffer_processor_threads_core_pool_size | 3 |
| graylog_outputbuffer_processor_threads_max_pool_size | 30 |
| graylog_udp_recvbuffer_sizes | 1048576 |
| graylog_processor_wait_strategy | blocking |
| graylog_inputbuffer_ring_size | 65536 |
| graylog_inputbuffer_processors | 2 |
| graylog_inputbuffer_wait_strategy | blocking |
| graylog_message_journal_enabled | True |
| graylog_message_journal_dir | /var/lib/graylog-server/journal |
| graylog_message_journal_max_age | 12h |
| graylog_message_journal_max_size | 5gb |
| graylog_message_journal_flush_age | 1m |
| graylog_message_journal_flush_interval | 1000000 |
| graylog_message_journal_segment_age | 1h |
| graylog_message_journal_segment_size | 100mb |
| graylog_async_eventbus_processors | 2 |
| graylog_lb_recognition_period_seconds | 3 |
| graylog_lb_throttle_threshold_percentage | 95 |
| graylog_stream_processing_timeout | 2000 |
| graylog_stream_processing_max_faults | 3 |
| graylog_alert_check_interval | 60 |
| graylog_output_module_timeout | 10000 |
| graylog_stale_master_timeout | 2000 |
| graylog_shutdown_timeout | 30000 |
| graylog_mongodb_uri | mongodb://127.0.0.1:27017/graylog |
| graylog_mongodb_max_connections | 100 |
| graylog_mongodb_threads_allowed_to_block_multiplier | 5 |
| graylog_transport_email_enabled | False |
| graylog_transport_email_hostname | |
| graylog_transport_email_port | 587 |
| graylog_transport_email_use_auth | True |
| graylog_transport_email_auth_username | |
| graylog_transport_email_auth_password | |
| graylog_transport_email_subject_prefix | [graylog] |
| graylog_transport_email_from_email | |
| graylog_transport_email_use_tls | True |
| graylog_transport_email_use_ssl | True |
| graylog_transport_email_web_interface_url | |
| graylog_http_connect_timeout | 5s |
| graylog_http_read_timeout | 10s |
| graylog_http_write_timeout | 10s |
| graylog_http_proxy_uri | |
| graylog_non_proxy_hosts | |
| graylog_disable_index_optimization | True |
| graylog_index_optimization_max_num_segments | 1 |
| graylog_gc_warning_threshold | 1s |
| graylog_ldap_connection_timeout | 2000 |
| graylog_disable_sigar | False |
| graylog_dashboard_widget_default_cache_time | 10s |
| graylog_proxied_requests_thread_pool_size | 32 |


If you need to add a property to `server.conf` that is not listed above, you can add it via the `graylog_additonal_config` property.

    graylog_additional_config:
      elasticsearch_discovery_default_user: my_username
      elasticsearch_discovery_default_password: "{{ my_password }}"

These settings will be added to the end of the `server.conf` file.


### Environment Variables

| Environment Variable | Ansible Variable | Default Value |
|---|---|---|
| JAVA | graylog_server_java | |
| GRAYLOG_SERVER_JAVA_OPTS | graylog_server_java_opts |
| GRAYLOG_SERVER_ARGS | graylog_server_args |
| GRAYLOG_COMMAND_WRAPPER | graylog_server_wrapper |


### MongoDB Variables

| Variable Name | Default Value |
|---|---|
| graylog_mongodb_data_path |  |
| graylog_mongodb_bind_port | |
| graylog_mongodb_bind_ip | |





## Author Information

Author: Marius Sturm (<marius@graylog.com>) and [contributors][4]

## License

Apache 2.0

[1]: https://github.com/elastic/ansible-elasticsearch
[2]: https://github.com/nginxinc/ansible-role-nginx
[3]: https://github.com/Graylog2/graylog-ansible-role/blob/master/meta/main.yml
[4]: https://github.com/Graylog2/graylog2-ansible-role/graphs/contributors
[5]: https://pablodav.github.io/post/graylog/graylog_ansible
[6]: https://pablodav.github.io/post/graylog/logstash_input
[7]: https://pablodav.github.io/post/graylog/graylog_logstash_nagios_nsca
[8]: https://docs.graylog.org/docs/installing
[9]: https://docs.graylog.org/v1/docs/server-conf
