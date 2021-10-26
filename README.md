[![Galaxy](https://img.shields.io/badge/galaxy-graylog--ansible--role-blue)](https://galaxy.ansible.com/Graylog2/graylog) ![Ansible](https://img.shields.io/ansible/role/d/56392.svg) ![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F56392%2F&query=$.min_ansible_version) ![Ansible](https://img.shields.io/ansible/quality/56392)

# Graylog Ansible Role

## Requirements

- Ansible (> 2.5.0)


## Dependencies

Graylog requires Java, [Elasticsearch][1], and MongoDB. See the official [Graylog documentation][8] for the correct versions of each of these dependencies.

If you need Nginx installed, you can include the official [Nginx][2] role in your playbook.


> **NOTE**
> For Elasticsearch, be sure to set `es_version` to 7.10 or lower. Graylog does not support Elasticsearch 7.11 and up!



## Example Playbook



## Role Variables

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
| graylog_inputbuffer_ring_size | |
| graylog_inputbuffer_processors | |
| graylog_inputbuffer_wait_strategy | |
| graylog_message_journal_enabled | |
| graylog_message_journal_dir | |
| graylog_message_journal_max_age | |
| graylog_message_journal_max_size | |
| graylog_message_journal_flush_age | |
| graylog_message_journal_flush_interval | |
| graylog_message_journal_segment_age | |
| graylog_message_journal_segment_size | |
| graylog_async_eventbus_processors | |
| graylog_lb_recognition_period_seconds | |
| graylog_lb_throttle_threshold_percentage | |
| graylog_stream_processing_timeout | 2000 |
| graylog_stream_processing_max_faults | |
| graylog_alert_check_interval | |
| graylog_output_module_timeout | 10000 |
| graylog_stale_master_timeout | 2000 |
| graylog_shutdown_timeout | 30000 |
| graylog_mongodb_uri | |
| graylog_mongodb_max_connections | |
| graylog_mongodb_threads_allowed_to_block_multiplier | |
| graylog_transport_email_enabled | |
| graylog_transport_email_hostname | |
| graylog_transport_email_port | |
| graylog_transport_email_use_auth | |
| graylog_transport_email_auth_username | |
| graylog_transport_email_auth_password | |
| graylog_transport_email_subject_prefix | |
| graylog_transport_email_from_email | |
| graylog_transport_email_use_tls | |
| graylog_transport_email_use_ssl | |
| graylog_transport_email_web_interface_url | |
| graylog_http_connect_timeout | 5s |
| graylog_http_read_timeout | 10s |
| graylog_http_write_timeout | 10s |
| graylog_http_proxy_uri | |
| graylog_non_proxy_hosts | |
| graylog_disable_index_optimization | |
| graylog_index_optimization_max_num_segments | |
| graylog_gc_warning_threshold | |
| graylog_ldap_connection_timeout | 2000 |
| graylog_disable_sigar | |
| graylog_dashboard_widget_default_cache_time | |
| graylog_proxied_requests_thread_pool_size | 32 |


If you need to add a property to `server.conf` that is not listed above, you can add it via the `graylog_additonal_config` property.

    graylog_additional_config:
      example_config1: value1
      example_config2: value2

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
