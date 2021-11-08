# Role Variables

## Main Variables

| Variable Name | Default Value | Description |
|---|---|---|
| `graylog_version` | | **Required**. Should be in `X.Y` format (e.g, `4.2`) |
| `graylog_full_version` | | Optional. If not provided, the latest revision of `graylog_version` will be installed. Should be in `X.Y.Z-rev` format (e.g, `4.2.0-3`) |
| `graylog_install_java` | True | Whether to install Java on the instance.|
| `graylog_install_elasticsearch` | True | Whether to install Elasticsearch on the instance. |
| `graylog_install_mongodb` | True | Whether to install MongoDB on the instance. |
| `graylog_install_enterprise_plugins` | False | Whether to install the [graylog-enterprise-plugins](https://docs.graylog.org/docs/intro) package. |
| `graylog_install_integrations_plugins` | False | Whether to install the [graylog-integrations-plugins](https://docs.graylog.org/docs/integrations) package. |
| `graylog_install_enterprise_integrations_plugins` | False | Whether to install the [graylog-enterprise-integrations-plugins](https://docs.graylog.org/docs/intro) package. |


## Java Variables

| Ansible Variable | Default Value | Description |
|---|---|---|
| `graylog_server_java` | /usr/bin/java | Sets the `JAVA` environment variable on the instance.  |
| `graylog_server_heap_size` | 1500m | Sets the Java heap size for Graylog. |
| `graylog_server_java_opts` | -Djava.net.preferIPv4Stack=true -Xms{{ graylog_server_heap_size }} -Xmx{{ graylog_server_heap_size }} -XX:NewRatio=1 -server -XX:+ResizeTLAB -XX:-OmitStackTraceInFastThrow {{graylog_server_java_opts_extra}} | Sets the `GRAYLOG_SERVER_JAVA_OPTS` environment variable on the instance. | {{graylog_server_java_opts_extra}} |
| `graylog_server_java_opts_extra` | | Any Java arguments you want to append to the Graylog startup command can be set here.
| `graylog_server_args` | | Sets the `GRAYLOG_SERVER_ARGS` environment variable on the instance. |
| `graylog_server_wrapper` | | Sets the `GRAYLOG_COMMAND_WRAPPER` environment variable on the instance. |


## Server.conf Variables

These variables let you configure the properties in `server.conf`. See the [offical Graylog documentation](https://docs.graylog.org/v1/docs/server-conf) for details on these setings.

| Variable Name | Default Value |
|---|---|
| `graylog_is_master` | True |
| `graylog_node_id_file` | /etc/graylog/server/node-id |
| `graylog_password_secret` |   |
| `root_username`  | admin  |
| `graylog_root_password_sha2` |  |
| `graylog_root_email` | |
| `graylog_root_timezone` | UTC |
| `graylog_bin_dir` | /usr/share/graylog-server/bin |
| `graylog_data_dir` | /var/lib/graylog-server |
| `graylog_plugin_dir` | /usr/share/graylog-server/plugin |
| `graylog_http_bind_address` | 0.0.0.0:9000 |
| `graylog_http_publish_uri` | http://0.0.0.0:9000/ |
| `graylog_http_external_uri` | http://0.0.0.0:9000/ |
| `graylog_http_enable_cors` | True |
| `graylog_http_enable_gzip` | True |
| `graylog_http_max_header_size` | 8192 |
| `graylog_http_thread_pool_size` | 16 |
| `graylog_http_enable_tls` | False |
| `graylog_http_tls_cert_file` | /path/to/graylog.crt |
| `graylog_http_tls_key_file` | /path/to/graylog.key |
| `graylog_http_tls_key_password` | |
| `graylog_trusted_proxies` | |
| `graylog_elasticsearch_hosts` | http://127.0.0.1:9200 |
| `graylog_elasticsearch_connect_timeout` | 10s |
| `graylog_elasticsearch_socket_timeout` | 60s |
| `graylog_elasticsearch_max_total_connections` | 20 |
| `graylog_elasticsearch_max_total_connections_per_route` | 2 |
| `graylog_elasticsearch_max_retries` | 2 |
| `graylog_elasticsearch_discovery_enabled` | False |
| `graylog_elasticsearch_discovery_frequency` | 30s |
| `graylog_elasticsearch_compression_enabled` | False |
| `graylog_rotation_strategy` | count |
| `graylog_elasticsearch_max_docs_per_index` | 20000000 |
| `graylog_elasticsearch_max_size_per_index` | 1073741824 |
| `graylog_elasticsearch_max_time_per_index` | 1d |
| `graylog_elasticsearch_disable_version_check` | True |
| `graylog_no_retention` | False |
| `graylog_elasticsearch_max_number_of_indices` | 20 |
| `graylog_retention_strategy` | delete |
| `graylog_elasticsearch_shards` | 4 |
| `graylog_elasticsearch_replicas` | 0 |
| `graylog_elasticsearch_index_prefix` | graylog |
| `graylog_elasticsearch_template_name` | graylog-internal |
| `graylog_allow_leading_wildcard_searches` | False |
| `graylog_allow_highlighting` | False |
| `graylog_elasticsearch_analyzer` | standard |
| `graylog_elasticsearch_request_timeout` | 1m |
| `graylog_elasticsearch_index_optimization_timeout` | 1h |
| `graylog_elasticsearch_index_optimization_jobs` | 20 |
| `graylog_index_ranges_cleanup_interval` | 1h |
| `graylog_index_field_type_periodical_interval` | 1h |
| `graylog_elasticsearch_output_batch_size` | 500 |
| `graylog_elasticsearch_output_flush_interval` | 1 |
| `graylog_output_fault_count_threshold` | 5 |
| `graylog_output_fault_penalty_seconds` | 30 |
| `graylog_processbuffer_processors` | 5 |
| `graylog_outputbuffer_processors` | 3 |
| `graylog_outputbuffer_processor_keep_alive_time` | 5000 |
| `graylog_outputbuffer_processor_threads_core_pool_size` | 3 |
| `graylog_outputbuffer_processor_threads_max_pool_size` | 30 |
| `graylog_udp_recvbuffer_sizes` | 1048576 |
| `graylog_processor_wait_strategy` | blocking |
| `graylog_inputbuffer_ring_size` | 65536 |
| `graylog_inputbuffer_processors` | 2 |
| `graylog_inputbuffer_wait_strategy` | blocking |
| `graylog_message_journal_enabled` | True |
| `graylog_message_journal_dir` | /var/lib/graylog-server/journal |
| `graylog_message_journal_max_age` | 12h |
| `graylog_message_journal_max_size` | 5gb |
| `graylog_message_journal_flush_age` | 1m |
| `graylog_message_journal_flush_interval` | 1000000 |
| `graylog_message_journal_segment_age` | 1h |
| `graylog_message_journal_segment_size` | 100mb |
| `graylog_async_eventbus_processors` | 2 |
| `graylog_lb_recognition_period_seconds` | 3 |
| `graylog_lb_throttle_threshold_percentage` | 95 |
| `graylog_stream_processing_timeout` | 2000 |
| `graylog_stream_processing_max_faults` | 3 |
| `graylog_alert_check_interval` | 60 |
| `graylog_output_module_timeout` | 10000 |
| `graylog_stale_master_timeout` | 2000 |
| `graylog_shutdown_timeout` | 30000 |
| `graylog_mongodb_uri` | mongodb://127.0.0.1:27017/graylog |
| `graylog_mongodb_max_connections` | 100 |
| `graylog_mongodb_threads_allowed_to_block_multiplier` | 5 |
| `graylog_transport_email_enabled` | False |
| `graylog_transport_email_hostname` | |
| `graylog_transport_email_port` | 587 |
| `graylog_transport_email_use_auth` | True |
| `graylog_transport_email_auth_username` | |
| `graylog_transport_email_auth_password` | |
| `graylog_transport_email_subject_prefix` | [graylog] |
| `graylog_transport_email_from_email` | |
| `graylog_transport_email_use_tls` | True |
| `graylog_transport_email_use_ssl` | True |
| `graylog_transport_email_web_interface_url` | |
| `graylog_http_connect_timeout` | 5s |
| `graylog_http_read_timeout` | 10s |
| `graylog_http_write_timeout` | 10s |
| `graylog_http_proxy_uri` | |
| `graylog_non_proxy_hosts` | |
| `graylog_disable_index_optimization` | True |
| `graylog_index_optimization_max_num_segments` | 1 |
| `graylog_gc_warning_threshold` | 1s |
| `graylog_ldap_connection_timeout` | 2000 |
| `graylog_disable_sigar` | False |
| `graylog_dashboard_widget_default_cache_time` | 10s |
| `graylog_proxied_requests_thread_pool_size` | 32 |


If you need to add a property to `server.conf` that is not listed above, you can add it via the `graylog_additonal_config` property.

    graylog_additional_config:
      elasticsearch_discovery_default_user: my_username
      elasticsearch_discovery_default_password: "{{ my_password }}"

These settings will be added to the end of the `server.conf` file.

## Package Variables

These settings allow you to customise where MongoDB and Graylog are installed from. You shouldn't need these, but they are there in case you do.

| Variable Name | Default Value |
|---|---|
| `graylog_manage_apt_repo` | True |
| `graylog_mongodb_package_name` | mongodb-org |
| `graylog_mongodb_service_name` | mongod |
| `graylog_mongodb_ubuntu_repo` | deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu {{ ansible_distribution_release }}/mongodb-org/{{ graylog_mongodb_version }} multiverse |
| `graylog_mongodb_ubuntu_key` | https://www.mongodb.org/static/pgp/server-{{ graylog_mongodb_version }}.asc |
| `graylog_mongodb_debian_repo` | deb http://repo.mongodb.org/apt/debian {{ ansible_distribution_release }}/mongodb-org/{{ graylog_mongodb_version }} main |
| `graylog_mongodb_debian_key` | https://www.mongodb.org/static/pgp/server-{{ graylog_mongodb_version }}.asc |
| `graylog_mongodb_redhat_repo` | https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/{{ graylog_mongodb_version }}/x86_64/ |
| `graylog_mongodb_redhat_key` | https://www.mongodb.org/static/pgp/server-{{ graylog_mongodb_version }}.asc |
| `graylog_apt_deb_url` | https://packages.graylog2.org/repo/packages/graylog-{{ graylog_version }}-repository_latest.deb |
| `graylog_yum_rpm_url` | https://packages.graylog2.org/repo/packages/graylog-{{ graylog_version }}-repository_latest.rpm |



## MongoDB Variables

| Variable Name | Default Value |
|---|---|
| `graylog_mongodb_version` | 4.4 |
| `graylog_mongodb_data_path` |  |
| `graylog_mongodb_bind_port` | 27017 |
| `graylog_mongodb_bind_ip` | 127.0.0.1 |

## Misc Variables

| Variable Name | Default Value |
|---|---|
| `graylog_es_debian_pin_version` | 6.* |
