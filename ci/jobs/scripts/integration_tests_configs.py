import dataclasses


@dataclasses.dataclass
class TC:
    prefix: str
    is_sequential: bool
    comment: str


TEST_CONFIGS = [
    TC("test_atomic_drop_table/", True, "no idea why i'm sequential"),
    TC("test_attach_without_fetching/", True, "no idea why i'm sequential"),
    TC(
        "test_cleanup_dir_after_bad_zk_conn/",
        True,
        "no idea why i'm sequential",
    ),
    TC(
        "test_consistent_parts_after_clone_replica/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_crash_log/", True, "no idea why i'm sequential"),
    TC("test_cross_replication/", True, "no idea why i'm sequential"),
    TC("test_ddl_worker_non_leader/", True, "no idea why i'm sequential"),
    TC("test_delayed_replica_failover/", True, "no idea why i'm sequential"),
    TC(
        "test_dictionary_allow_read_expired_keys/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_disabled_mysql_server/", True, "no idea why i'm sequential"),
    TC("test_distributed_respect_user_timeouts/", True, "no idea why i'm sequential"),
    TC("test_dns_cache/", True, "no idea why i'm sequential"),
    TC("test_global_overcommit_tracker/", True, "no idea why i'm sequential"),
    TC("test_grpc_protocol/", True, "no idea why i'm sequential"),
    TC("test_host_regexp_multiple_ptr_records/", True, "no idea why i'm sequential"),
    TC("test_http_failover/", True, "no idea why i'm sequential"),
    TC("test_https_replication/", True, "no idea why i'm sequential"),
    TC("test_insert_into_distributed/", True, "no idea why i'm sequential"),
    TC(
        "test_insert_into_distributed_through_materialized_view/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_keeper_map/", True, "no idea why i'm sequential"),
    TC("test_keeper_multinode_simple/", True, "no idea why i'm sequential"),
    TC("test_keeper_two_nodes_cluster/", True, "no idea why i'm sequential"),
    TC("test_limited_replicated_fetches/", True, "no idea why i'm sequential"),
    TC("test_merge_tree_s3/", True, "no idea why i'm sequential"),
    TC("test_mysql_database_engine/", True, "no idea why i'm sequential"),
    TC("test_parts_delete_zookeeper/", True, "no idea why i'm sequential"),
    TC(
        "test_postgresql_replica_database_engine/",
        True,
        "no idea why i'm sequential",
    ),
    TC(
        "test_profile_max_sessions_for_user/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_quorum_inserts_parallel/", True, "no idea why i'm sequential"),
    TC("test_random_inserts/", True, "no idea why i'm sequential"),
    TC("test_replace_partition/", True, "no idea why i'm sequential"),
    TC("test_replicated_database/", True, "no idea why i'm sequential"),
    TC("test_replicated_fetches_timeouts/", True, "no idea why i'm sequential"),
    TC(
        "test_replicated_merge_tree_wait_on_shutdown/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_server_overload/", True, "no idea why i'm sequential"),
    TC("test_server_reload/", True, "no idea why i'm sequential"),
    TC("test_storage_kafka/", True, "no idea why i'm sequential"),
    TC("test_storage_kerberized_kafka/", True, "no idea why i'm sequential"),
    TC("test_storage_rabbitmq/", True, "no idea why i'm sequential"),
    TC("test_storage_s3/", True, "no idea why i'm sequential"),
    TC("test_storage_s3_queue/", True, "no idea why i'm sequential"),
    TC("test_system_flush_logs/", True, "no idea why i'm sequential"),
    TC("test_system_logs/", True, "no idea why i'm sequential"),
    TC("test_system_metrics/", True, "no idea why i'm sequential"),
    TC("test_ttl_move/", True, "no idea why i'm sequential"),
    TC("test_user_ip_restrictions/", True, "no idea why i'm sequential"),
    TC(
        "test_zookeeper_config_load_balancing/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_zookeeper_fallback_session/", True, "no idea why i'm sequential"),
    TC(
        "test_backup_restore_on_cluster/test_concurrency.py",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_database_delta/test.py", True, "no idea why i'm sequential"),
    TC("test_keeper_ipv4_fallback/test.py", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_no_spark/", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_with_spark/", True, "no idea why i'm sequential"),
    TC(
        "test_storage_iceberg_schema_evolution/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_disks_app_interactive/", True, "no idea why i'm sequential"),
    TC("test_storage_delta_disks/", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_disks/", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_concurrent/", True, "no idea why i'm sequential"),
]

IMAGES_ENV = {
    "clickhouse/dotnet-client": "DOCKER_DOTNET_CLIENT_TAG",
    "clickhouse/integration-helper": "DOCKER_HELPER_TAG",
    "clickhouse/integration-test": "DOCKER_BASE_TAG",
    "clickhouse/kerberos-kdc": "DOCKER_KERBEROS_KDC_TAG",
    "clickhouse/mysql-golang-client": "DOCKER_MYSQL_GOLANG_CLIENT_TAG",
    "clickhouse/mysql-java-client": "DOCKER_MYSQL_JAVA_CLIENT_TAG",
    "clickhouse/mysql-js-client": "DOCKER_MYSQL_JS_CLIENT_TAG",
    "clickhouse/arrowflight-server-test": "DOCKER_ARROWFLIGHT_SERVER_TAG",
    "clickhouse/mysql-php-client": "DOCKER_MYSQL_PHP_CLIENT_TAG",
    "clickhouse/nginx-dav": "DOCKER_NGINX_DAV_TAG",
    "clickhouse/postgresql-java-client": "DOCKER_POSTGRESQL_JAVA_CLIENT_TAG",
    "clickhouse/python-bottle": "DOCKER_PYTHON_BOTTLE_TAG",
    "clickhouse/integration-test-with-unity-catalog": "DOCKER_BASE_WITH_UNITY_CATALOG_TAG",
    "clickhouse/integration-test-with-hms": "DOCKER_BASE_WITH_HMS_TAG",
    "clickhouse/mysql_dotnet_client": "DOCKER_MYSQL_DOTNET_CLIENT_TAG",
}

# collected by
# SELECT
#     splitByString('::', test_name)[1] AS test_file,
#     SUM(test_duration_ms) AS dur
# FROM checks
# WHERE 1
#   AND check_name LIKE 'Integration tests%'
#   AND commit_sha = '79f4156eaa083ddd69722c267b88baa9d4091f7f'
# GROUP BY test_file
# HAVING test_file != ''
# ORDER BY dur desc
RAW_TEST_DURATIONS = """
test_s3_aws_sdk_has_slightly_unreliable_behaviour/test.py	1202991
test_throttling/test.py	797321
test_storage_rabbitmq/test.py	711457
test_backup_restore_new/test.py	510930
test_ddl_config_hostname/test.py	292228
test_dictionaries_update_and_reload/test.py	278202
test_backup_restore_on_cluster/test.py	275680
test_host_regexp_multiple_ptr_records/test.py	268327
test_replicated_merge_tree_compatibility/test.py	259752
test_storage_s3_queue/test_3.py	218091
test_backward_compatibility/test_aggregate_function_state.py	213529
test_version_update_after_mutation/test.py	180664
test_dictionaries_dependency/test.py	167554
test_row_policy/test.py	165171
test_ttl_replicated/test.py	159103
test_select_access_rights/test_from_system_tables.py	156511
test_distributed_ddl/test.py	146284
test_version_update/test.py	125295
test_no_merges_volume_ttl/test.py	123835
test_backward_compatibility/test_ip_types_binary_compatibility.py	123736
test_memory_profiler_min_max_borders/test.py	122667
test_distributed_insert_backward_compatibility/test.py	121309
test_prefer_global_in_and_join/test.py	120199
test_executable_dictionary/test.py	118182
test_async_logger_metrics/test.py	117695
test_replicated_s3_zero_copy_drop_partition/test.py	116694
test_alternative_keeper_config/test.py	115820
test_drop_replica/test.py	114384
test_mysql_protocol/test.py	114286
test_session_settings_table/test.py	110349
test_backup_restore_on_cluster/test_huge_concurrent_restore.py	106627
test_distributed_system_query/test.py	106262
test_backup_restore_on_cluster/test_slow_rmt.py	105889
test_named_collections_if_exists_on_cluster/test.py	102690
test_groupBitmapAnd_on_distributed/test.py	101673
test_composable_protocols/test.py	100259
test_backup_restore_new/test_cancel_backup.py	100111
test_keeper_reconfig_remove_many/test.py	98747
test_async_metrics_in_cgroup/test.py	98188
test_backward_compatibility/test_vertical_merges_from_compact_parts.py	97798
test_max_suspicious_broken_parts/test.py	93415
test_backup_restore_keeper_map/test.py	88876
test_lightweight_updates/test.py	87504
test_rocksdb_read_only/test.py	86513
test_move_ttl_broken_compatibility/test.py	85991
test_replicated_parse_zk_metadata/test.py	84858
test_fetch_memory_usage/test.py	84174
test_backward_compatibility/test_functions.py	82214
test_keeper_three_nodes_two_alive/test.py	80830
test_mutations_with_merge_tree/test.py	77604
test_zookeeper_config/test.py	77530
test_disk_checker/test.py	77445
test_replication_credentials/test.py	76146
test_keeper_znode_time/test.py	72705
test_refreshable_mat_view_replicated/test.py	72541
test_tmp_policy/test.py	72383
test_attach_partition_using_copy/test.py	70520
test_concurrent_ttl_merges/test.py	70471
test_trace_log_build_id/test.py	69348
test_backup_restore_on_cluster/test_concurrency.py	69204
test_insert_into_distributed_sync_async/test.py	68857
test_storage_url_http_headers/test.py	68812
test_memory_limit_observer/test.py	68743
test_system_ddl_worker_queue/test.py	67196
test_jbod_balancer/test.py	67091
test_parallel_replicas_increase_error_count/test.py	66934
test_quorum_inserts/test.py	65703
test_manipulate_statistics/test.py	65557
test_backward_compatibility/test_old_client_with_replicated_columns.py	64786
test_parallel_replicas_snapshot_from_initiator/test.py	64097
test_move_partition_to_volume_async/test.py	63813
test_storage_s3/test.py	63492
test_keeper_reconfig_add/test.py	62869
test_backup_restore_on_cluster/test_disallow_concurrency.py	62212
test_refreshable_mv/test.py	62147
test_keeper_compression/test_without_compression.py	60718
test_backup_restore_on_cluster_with_checksum_data_file_name/test.py	60613
test_replicated_mutations/test.py	60563
test_hedged_requests_parallel/test.py	60070
test_distributed_ddl/test_replicated_alter.py	59179
test_odbc_interaction/test.py	58775
test_buffer_profile/test.py	58532
test_replicated_merge_tree_encryption_codec/test.py	58273
test_stop_insert_when_disk_close_to_full/test.py	57715
test_keeper_reconfig_replace_leader/test.py	57256
test_replicated_fetches_bandwidth/test.py	56953
test_restore_replica/test.py	55977
test_cancel_freeze/test.py	55693
test_replication_without_zookeeper/test.py	54999
test_keeper_max_request_size/test.py	54809
test_keeper_mntr_pressure/test.py	54797
test_system_logs_comment/test.py	54576
test_range_hashed_dictionary_types/test.py	54424
test_async_load_databases/test.py	53166
test_structured_logging_json/test.py	53147
test_keeper_reconfig_replace_leader_in_one_command/test.py	53114
test_explain_estimates/test.py	53072
test_kafka_bad_messages/test_1.py	52429
test_keeper_password/test.py	52390
test_filesystem_cache/test.py	52276
test_hot_reload_storage_policy/test.py	52126
test_old_parts_finally_removed/test.py	51700
test_create_query_constraints/test.py	51436
test_tcp_handler_connection_limits/test.py	51235
test_storage_kafka_sasl/test.py	50886
test_storage_postgresql/test.py	50583
test_encrypted_disk_replication/test.py	50481
test_shard_names/test.py	49869
test_disabled_access_control_improvements/test_row_policy.py	49767
test_fetch_partition_from_auxiliary_zookeeper/test.py	49627
test_backward_compatibility/test_const_node_optimization.py	49597
test_settings_from_server/test.py	49297
test_dictionaries_mysql/test.py	49204
test_keeper_internal_secure/test.py	49077
test_scheduler_query/test.py	48133
test_arrowflight_interface/test.py	47902
test_restore_db_replica/test.py	47818
test_ttl_multilevel_group_by/test.py	47793
test_concurrent_queries_restriction_by_query_kind/test.py	47266
test_storage_rabbitmq/test_failed_connection.py	47190
test_file_schema_inference_cache/test.py	47056
test_backward_compatibility/test_rocksdb_upgrade.py	46693
test_mutations_hardlinks/test.py	46554
test_async_insert_memory/test.py	46467
test_prometheus_protocols/test_different_table_engines.py	46414
test_postgresql_replica_database_engine/test_3.py	46264
test_database_hms/test.py	45922
test_storage_kafka/test_produce_http_interface.py	45872
test_group_array_element_size/test.py	45028
test_fetch_partition_with_outdated_parts/test.py	44982
test_s3_plain_rewritable_rotate_tables/test.py	44911
test_multi_access_storage_role_management/test.py	44690
test_database_iceberg_nessie_catalog/test.py	44316
test_backward_compatibility/test.py	44226
test_alter_on_mixed_type_cluster/test.py	44068
test_grant_and_revoke/test_with_table_engine_grant.py	44007
test_transposed_metric_log/test.py	43905
test_delayed_replica_failover/test.py	43812
test_backup_restore_on_cluster/test_different_versions.py	43791
test_database_iceberg/test.py	43732
test_validate_only_initial_alter_query/test_replicated_database.py	42945
test_storage_hudi/test.py	42565
test_replicated_database/test.py	42446
test_insert_into_distributed/test.py	42189
test_ddl_alter_query/test.py	41946
test_access_control_on_cluster/test.py	41757
test_reloading_settings_from_users_xml/test.py	41747
test_dictionaries_config_reload/test.py	41724
test_storage_kafka/test_batch_slow_1.py	41255
test_replicated_merge_tree_with_auxiliary_zookeepers/test.py	41150
test_postgresql_replica_database_engine/test_1.py	41134
test_storage_azure_blob_storage/test.py	41065
test_ddl_on_cluster_stop_waiting_for_offline_hosts/test.py	40402
test_storage_kafka/test_batch_slow_2.py	40127
test_merge_tree_s3_with_cache/test.py	39841
test_role/test.py	39779
test_mutations_in_partitions_of_merge_tree/test.py	39456
test_select_access_rights/test_main.py	39371
test_storage_kerberized_kafka/test.py	39226
test_kerberos_auth/test.py	38881
test_replicated_merge_tree_encrypted_disk/test.py	38793
test_keeper_force_recovery/test.py	38784
test_parallel_replicas_failover/test.py	38770
test_storage_kafka/test_batch_slow_0.py	38762
test_random_inserts/test.py	38620
test_store_cleanup/test.py	38601
test_replace_partition/test.py	38523
test_system_merges/test.py	38262
test_storage_s3_queue/test_5.py	38178
test_storage_kafka/test_zookeeper_locks.py	37900
test_trace_collector_serverwide/test.py	37717
test_backup_restore_on_cluster/test_two_shards_two_replicas.py	37706
test_backup_restore_on_cluster/test_cancel_backup.py	37669
test_graphite_merge_tree/test.py	37423
test_rocksdb_options/test.py	37341
test_default_compression_codec/test.py	37184
test_executable_table_function/test.py	37061
test_external_cluster/test.py	36902
test_send_request_to_leader_replica/test.py	36538
test_azure_blob_storage_native_copy/test.py	36341
test_s3_cluster_restart/test.py	36281
test_keeper_secure_client/test.py	36170
test_server_reload/test.py	35861
test_parallel_replicas_custom_key_load_balancing/test.py	35716
test_part_uuid/test.py	35445
test_max_bytes_ratio_before_external_order_group_by_for_server/test.py	34902
test_peak_memory_usage/test.py	34810
test_grpc_protocol/test.py	34802
test_mask_sensitive_info/test.py	34638
test_format_schema_on_server/test.py	34626
test_create_user_and_login/test.py	34600
test_postgresql_replica_database_engine/test_0.py	34492
test_s3_cluster/test.py	34473
test_table_db_num_limit/test.py	34389
test_keeper_ipv4_fallback/test.py	34120
test_backward_compatibility/test_block_marshalling.py	34031
test_storage_mysql/test.py	34008
test_kafka_bad_messages/test.py	33898
test_log_family_s3/test.py	33835
test_dictionaries_with_invalid_structure/test.py	33827
test_remote_function_view/test.py	33781
test_shard_level_const_function/test.py	33747
test_backward_compatibility/test_aggregation_with_out_of_order_buckets.py	33720
test_distributed_ddl_password/test.py	33687
test_storage_kafka/test_batch_fast.py	33587
test_host_regexp_hosts_file_resolution/test.py	33548
test_recompression_ttl/test.py	33455
test_render_log_file_name_templates/test.py	33401
test_replicated_engine_arguments/test.py	33302
test_atomic_drop_table/test.py	33230
test_distributed_load_balancing/test.py	33057
test_concurrent_threads_soft_limit/test.py	32938
test_storage_delta/test.py	32929
test_custom_dashboards/test.py	32736
test_distributed_ddl_on_cross_replication/test.py	32405
test_storage_iceberg_no_spark/test_writes_create_table_bugs.py	32260
test_storage_iceberg_no_spark/test_writes_with_compression_metadata.py	32259
test_cluster_all_replicas/test.py	32213
test_storage_iceberg_no_spark/test_writes_statistics_by_minmax_pruning.py	32086
test_parallel_replicas_over_distributed/test.py	32033
test_dictionaries_replace/test.py	32004
test_insert_distributed_async_send/test.py	31929
test_backward_compatibility/test_insert_profile_events.py	31584
test_passing_max_partitions_to_read_remotely/test.py	31555
test_storage_dict/test.py	31490
test_inserts_with_keeper_retries/test.py	31431
test_authentication/test.py	31366
test_config_hide_in_preprocessed/test.py	31314
test_backup_restore_s3/test.py	31305
test_system_logs_hostname/test_replicated.py	31258
test_parallel_replicas_custom_key/test.py	31253
test_warning_broken_tables/test.py	31221
test_git_import/test.py	31191
test_block_structure_mismatch/test.py	31111
test_backward_compatibility/test_cte_distributed.py	31039
test_s3_cluster_insert_select/test.py	31013
test_storage_s3_queue/test_1.py	30835
test_insert_over_http_query_log/test.py	30824
test_merges_memory_limit/test.py	30735
test_https_replication/test.py	30595
test_storage_url_with_proxy/test.py	30535
test_postgresql_replica_database_engine/test_2.py	30508
test_zookeeper_config/test_password.py	30503
test_partition/test.py	30460
test_backward_compatibility/test_aggregate_fixed_key.py	30430
test_config_substitutions/test.py	30247
test_distributed_directory_monitor_split_batch_on_failure/test.py	30214
test_user_ip_restrictions/test.py	30167
test_rename_column/test.py	30131
test_union_header/test.py	30103
test_reload_clusters_config/test.py	30074
test_max_suspicious_broken_parts_replicated/test.py	30067
test_tcp_handler_interserver_listen_host/test_case.py	29996
test_storage_kafka/test_batch_slow_6.py	29879
test_merge_table_over_distributed/test.py	29860
test_secure_socket/test.py	29807
test_lost_part/test.py	29783
test_config_reloader_interval/test.py	29671
test_insert_into_distributed_through_materialized_view/test.py	29577
test_http_and_readonly/test.py	29549
test_groupBitmapAnd_on_distributed/test_groupBitmapAndState_on_distributed_table.py	29542
test_distributed_inter_server_secret/test.py	29504
test_userspace_page_cache/test.py	29463
test_replica_can_become_leader/test.py	29375
test_build_sets_from_multiple_threads/test.py	29360
test_storage_kafka/test_batch_slow_4.py	29348
test_hedged_requests/test.py	29342
test_dictionaries_ddl/test.py	29236
test_merge_tree_s3_failover/test.py	29203
test_allowed_url_from_config/test.py	29111
test_dictionaries_access/test.py	29082
test_storage_kafka/test_intent_sizes.py	29067
test_zookeeper_config_load_balancing/test.py	29064
test_system_clusters_actual_information/test.py	29055
test_parallel_replicas_skip_shards/test.py	28808
test_optimize_on_insert/test.py	28752
test_backup_restore_storage_policy/test.py	28730
test_recovery_replica/test.py	28687
test_logs_level/test.py	28665
test_named_collections/test.py	28649
test_inherit_multiple_profiles/test.py	28615
test_reload_auxiliary_zookeepers/test.py	28538
test_s3_with_https/test.py	28517
test_parallel_replicas_insert_select/test.py	28442
test_temporary_data_in_cache/test.py	28434
test_merge_tree_azure_blob_storage/test.py	28413
test_disk_configuration/test.py	28402
test_asynchronous_metric_log_table/test.py	28385
test_server_start_and_ip_conversions/test.py	28382
test_system_reconnect_zookeeper/test.py	28357
test_format_cannot_allocate_thread/test.py	28287
test_storage_s3_queue/test_2.py	28250
test_merge_tree_load_marks/test.py	28244
test_delayed_remote_source/test.py	28207
test_storage_s3_queue/test_4.py	28199
test_dot_in_user_name/test.py	28162
test_replicated_database/test_settings_recover_lost_replica.py	28132
test_http_connection_drain_before_reuse/test.py	28130
test_system_metrics/test.py	28120
test_named_collections_encrypted/test.py	28105
test_ddl_worker_retry_when_dropping_db_failed/test.py	28048
test_storage_s3_queue/test_0.py	27983
test_ddl_worker_with_loopback_hosts/test.py	27978
test_alter_comment_on_cluster/test.py	27966
test_async_insert_adaptive_busy_timeout/test.py	27946
test_alter_database_on_cluster/test.py	27912
test_temporary_data/test.py	27895
test_sync_replica_on_cluster/test.py	27820
test_attach_partition_with_large_destination/test.py	27816
test_force_drop_table/test.py	27805
test_always_fetch_merged/test.py	27751
test_distributed_ddl_parallel/test.py	27679
test_reload_client_certificate/test.py	27678
test_reload_zookeeper/test.py	27608
test_storage_delta/test_imds.py	27605
test_statistics_cache/test.py	27577
test_zero_copy_expand_macros/test.py	27568
test_compression_nested_columns/test.py	27531
test_jbod_load_balancing/test.py	27513
test_storage_kafka/test_batch_slow_5.py	27502
test_database_replicated_settings/test.py	27408
test_quota/test.py	27360
test_storage_s3_queue/test_parallel_inserts.py	27266
test_storage_azure_blob_storage/test_check_after_upload.py	27247
test_backward_compatibility/test_memory_bound_aggregation.py	27170
test_backup_restore_s3/test_throttling.py	27158
test_attach_without_checksums/test.py	27067
test_truncate_database/test_replicated.py	26962
test_consistant_parts_after_move_partition/test.py	26910
test_replicated_access/test.py	26873
test_old_versions/test.py	26860
test_part_log_table/test.py	26842
test_attach_without_fetching/test.py	26799
test_password_constraints/test.py	26777
test_cleanup_dir_after_bad_zk_conn/test.py	26761
test_consistent_parts_after_clone_replica/test.py	26677
test_storage_azure_blob_storage/test_cluster.py	26549
test_mutation_fetch_fallback/test.py	26549
test_enabling_access_management/test.py	26548
test_system_start_stop_listen/test.py	26512
test_cluster_discovery/test_auxiliary_keeper.py	26478
test_replicated_merge_tree_replicated_db_ttl/test.py	26477
test_jbod_ha/test.py	26448
test_polymorphic_parts/test.py	26440
test_user_zero_database_access/test_user_zero_database_access.py	26408
test_checking_s3_blobs_paranoid/test.py	26387
test_backward_compatibility/test_short_strings_aggregation.py	26386
test_dotnet_client/test.py	26356
test_keeper_reconfig_remove/test.py	26311
test_settings_randomization/test.py	26244
test_broken_projections/test.py	26048
test_keeper_client/test.py	26015
test_insert_distributed_load_balancing/test.py	25937
test_keeper_persistent_log/test.py	25900
test_join_set_family_s3/test.py	25851
test_dictionaries_dependency_xml/test.py	25826
test_prometheus_endpoint/test.py	25791
test_os_thread_nice_value/test.py	25738
test_interserver_dns_retires/test.py	25699
test_quorum_inserts_parallel/test.py	25662
test_log_query_probability/test.py	25619
test_user_defined_object_persistence/test.py	25591
test_storage_url/test.py	25550
test_backward_compatibility/test_select_aggregate_alias_column.py	25508
test_table_function_mongodb/test.py	25473
test_threadpool_readers/test.py	25436
test_keeper_availability_zone/test.py	25394
test_s3_table_function_with_https_proxy/test.py	25362
test_max_rows_to_read_leaf_with_view/test.py	25341
test_truncate_database/test_distributed.py	25293
test_https_replication/test_change_ip.py	25287
test_custom_settings/test.py	25226
test_non_default_compression/test.py	25220
test_replicated_merge_tree_wait_on_shutdown/test.py	25213
test_replicated_fetches_timeouts/test.py	25181
test_replica_is_active/test.py	25122
test_backward_compatibility/test_parallel_replicas_protocol.py	25013
test_replicated_database_cluster_groups/test.py	25000
test_plain_rewr_legacy_layout/test.py	24996
test_drop_if_empty/test.py	24992
test_extreme_deduplication/test.py	24989
test_settings_constraints_distributed/test.py	24984
test_read_temporary_tables_on_failure/test.py	24969
test_max_authentication_methods_per_user/test.py	24919
test_log_lz4_streaming/test.py	24881
test_unknown_column_dist_table_with_alias/test.py	24859
test_format_avro_confluent/test.py	24839
test_default_database_on_cluster/test.py	24773
test_replicated_merge_tree_config/test.py	24762
test_format_schema_source/test.py	24675
test_table_functions_access_rights/test.py	24673
test_azure_blob_storage_plain_rewritable/test.py	24621
test_recovery_time_metric/test.py	24598
test_move_partition_to_disk_on_cluster/test.py	24573
test_user_valid_until/test.py	24573
test_mark_cache_profile_events/test.py	24566
test_scheduler_cpu_preemptive/test.py	24549
test_reloading_storage_configuration/test.py	24500
test_cleanup_after_start/test.py	24487
test_library_bridge/test.py	24439
test_database_glue/test.py	24391
test_system_detached_tables/test.py	24379
test_grant_and_revoke/test_without_table_engine_grant.py	24337
test_async_connect_to_multiple_ips/test.py	24317
test_keeper_map_retries/test.py	24316
test_s3_storage_conf_new_proxy/test.py	24305
test_memory_limit/test.py	24245
test_s3_plain_rewritable/test.py	24238
test_lost_part_during_startup/test.py	24229
test_zookeeper_config/test_secure.py	24213
test_trace_log_memory_context/test.py	24202
test_suggestions/test.py	24179
test_on_cluster_timeouts/test.py	24169
test_executable_user_defined_function/test.py	24158
test_restore_external_engines/test.py	24134
test_merge_tree_s3/test.py	24040
test_replicated_users/test.py	24039
test_fix_metadata_version/test.py	24005
test_mutations_with_projection/test.py	23992
test_dictionary_custom_settings/test.py	23990
test_replicated_merge_tree_s3/test.py	23977
test_drop_is_lock_free/test.py	23933
test_keeper_incorrect_config/test.py	23924
test_s3_table_function_with_http_proxy/test.py	23889
test_parallel_replicas_no_replicas/test.py	23884
test_keeper_back_to_back/test.py	23853
test_replicated_merge_tree_thread_schedule_timeouts/test.py	23852
test_backup_s3_storage_class/test.py	23852
test_transactions/test.py	23845
test_distributed_config/test.py	23844
test_drop_database_replica/test.py	23842
test_distributed_storage_configuration/test.py	23842
test_broken_part_during_merge/test.py	23829
test_merge_tree_empty_parts/test.py	23824
test_https_s3_table_function_with_http_proxy_no_tunneling/test.py	23821
test_ldap_external_user_directory/test.py	23811
test_read_only_table/test.py	23789
test_keeper_max_append_byte_size/test.py	23748
test_reload_certificate/test.py	23743
test_s3_storage_conf_proxy/test.py	23728
test_http_native/test.py	23716
test_tlsv1_3/test.py	23701
test_keeper_snapshot_small_distance/test.py	23656
test_storage_mongodb/test.py	23655
test_keeper_watches/test.py	23651
test_default_compression_in_mergetree_settings/test.py	23646
test_plain_rewritable_backward_compatibility/test.py	23645
test_remote_prewhere/test.py	23644
test_default_role/test.py	23634
test_prometheus_protocols/test_write_read.py	23605
test_multiple_disks/test.py	23600
test_unambiguous_alter_commands/test.py	23593
test_concurrent_queries_for_all_users_restriction/test.py	23584
test_keeper_profiler/test.py	23573
test_keeper_s3_snapshot/test.py	23572
test_disk_types/test.py	23572
test_remove_stale_moving_parts/test.py	23568
test_system_logs_recreate/test.py	23568
test_backup_restore/test.py	23566
test_parquet_page_index/test.py	23562
test_disable_insertion_and_mutation/test.py	23559
test_compressed_marks_restart/test.py	23555
test_s3_low_cardinality_right_border/test.py	23549
test_merge_tree_load_parts/test.py	23544
test_zookeeper_connection_log/test.py	23541
test_backup_restore_new/test_shutdown_wait_backup.py	23540
test_ssl_cert_authentication/test.py	23523
test_dictionary_asynchronous_metrics/test.py	23523
test_runtime_configurable_cache_size/test.py	23521
test_keeper_four_word_command/test_allow_list.py	23502
test_disks_app_other_disk_types/test.py	23497
test_keeper_nodes_remove/test.py	23495
test_user_directories/test.py	23489
test_drop_replica_with_auxiliary_zookeepers/test.py	23473
test_covered_by_broken_exists/test.py	23472
test_sql_roles_for_xml_users/test.py	23471
test_placement_info/test.py	23463
test_keeper_auth/test.py	23458
test_insert_distributed_async_extra_dirs/test.py	23456
test_tcp_handler_http_responses/test_case.py	23453
test_reload_query_masking_rules/test.py	23450
test_accept_invalid_certificate/test.py	23438
test_force_deduplication/test.py	23437
test_lazy_database/test.py	23435
test_database_disk_setting/test.py	23432
test_keeper_dynamic_log_level/test.py	23429
test_dictionary_ddl_on_cluster/test.py	23429
test_force_restore_data_flag_for_keeper_dataloss/test.py	23424
test_storage_numbers/test.py	23420
test_postgresql_protocol/test.py	23415
test_keeper_zookeeper_converter/test.py	23387
test_server_keep_alive/test.py	23375
test_alter_settings_on_cluster/test.py	23374
test_replicated_database_interserver_host/test.py	23369
test_limited_replicated_fetches/test.py	23365
test_attach_backup_from_s3_plain/test.py	23355
test_intersecting_parts/test.py	23352
test_attach_table_from_s3_plain_readonly/test.py	23346
test_keeper_snapshots/test.py	23342
test_limit_materialized_view_count/test.py	23336
test_keeper_force_recovery_single_node/test.py	23334
test_backup_restore_azure_blob_storage/test.py	23330
test_keeper_four_word_command/test.py	23328
test_keeper_nodes_add/test.py	23317
test_ssh_keys_authentication/test.py	23310
test_disks_app_func/test.py	23310
test_keeper_invalid_digest/test.py	23307
test_allow_feature_tier/test.py	23302
test_storage_policies/test.py	23300
test_filesystem_layout/test.py	23295
test_startup_scripts_execution_state/test.py	23295
test_aliases_in_default_expr_not_break_table_structure/test.py	23283
test_settings_constraints/test.py	23276
test_restart_server/test.py	23275
test_keeper_compression/test_with_compression.py	23267
test_dictionaries_wait_for_load/test.py	23263
test_s3_storage_class/test.py	23255
test_naive_bayes_bad_models/test.py	23253
test_executable_user_defined_functions_config_reload/test.py	23245
test_ssh/test.py	23241
test_backward_compatibility/test_normalized_count_comparison.py	23238
test_backup_log/test.py	23231
test_system_reload_async_metrics/test.py	23219
test_geoparquet/test.py	23217
test_jemalloc_global_profiler/test.py	23212
test_text_log_level/test.py	23209
test_catboost_evaluate/test.py	23207
test_shutdown_static_destructor_failure/test.py	23205
test_shutdown_wait_unfinished_queries/test.py	23203
test_detached_parts_metrics/test.py	23201
test_reload_max_table_size_to_drop/test.py	23200
test_prometheus_protocols/test_evaluation.py	23199
test_deduplicated_attached_part_rename/test.py	23196
test_keeper_block_acl/test.py	23196
test_timezone_config/test.py	23187
test_ssh/test_options_propagation_enabled.py	23185
test_log_levels_update/test.py	23179
test_attach_table_normalizer/test.py	23177
test_database_backup/test.py	23176
test_access_for_functions/test.py	23173
test_keeper_remove_acl/test.py	23157
test_scram_sha256_password_with_replicated_zookeeper_replicator/test.py	23144
test_scheduler_cpu/test.py	23142
test_merge_tree_settings_constraints/test.py	23141
test_server_startup_and_shutdown_logs/test.py	23134
test_disabled_mysql_server/test.py	23130
test_send_crash_reports/test.py	23120
test_globs_in_filepath/test.py	23111
test_endpoint_macro_substitution/test.py	23109
test_wrong_db_or_table_name/test.py	23106
test_merge_tree_prewarm_cache/test.py	23096
test_profile_settings_and_constraints_order/test.py	23082
test_storage_delta_disks/test.py	23079
test_match_process_uid_against_data_owner/test.py	23076
test_internal_queries_not_counted/test.py	23075
test_library_bridge/test_exiled.py	23068
test_keeper_broken_logs/test.py	23060
test_parts_delete_zookeeper/test.py	23060
test_dictionaries_null_value/test.py	23030
test_keeper_and_access_storage/test.py	23029
test_drop_no_local_path/test.py	23020
test_distributed_format/test.py	23003
test_disabled_access_control_improvements/test_select_from_system_tables.py	22976
test_arrowflight_interface/test_ticket_expiration.py	22960
test_dictionary_allow_read_expired_keys/test_default_reading.py	22940
test_keeper_multinode_simple/test.py	22936
test_profile_events_s3/test.py	22912
test_dictionary_allow_read_expired_keys/test_dict_get_or_default.py	22911
test_storage_iceberg_concurrent/test_concurrent_reads.py	22896
test_dictionary_allow_read_expired_keys/test_default_string.py	22850
test_dictionary_allow_read_expired_keys/test_dict_get.py	22840
test_system_flush_logs/test.py	22729
test_storage_alias_replicated/test.py	22590
test_replicated_database_recover_digest_mismatch/test.py	22404
test_matview_union_replicated/test.py	22277
test_fetch_partition_should_reset_mutation/test.py	21733
test_http_failover/test.py	21442
test_sharding_key_from_default_column/test.py	21274
test_database_disk/test.py	21177
test_storage_nats/test_nats_jet_stream.py	20962
test_asynchronous_metrics_pk_bytes_fields/test.py	20937
test_storage_nats/test_nats_core.py	20927
test_concurrent_queries_for_user_restriction/test.py	20705
test_restart_with_unavailable_azure/test.py	20506
test_replicated_detach_table/test.py	20504
test_disk_name_virtual_column/test.py	20424
test_alter_moving_garbage/test.py	20318
test_keeper_map/test.py	20146
test_permissions_drop_replica/test.py	19857
test_file_cluster/test.py	19765
test_parallel_replicas_invisible_parts/test.py	19420
test_check_table_name_length_2/test.py	19340
test_parallel_replicas_protocol/test.py	18955
test_cross_replication/test.py	18893
test_remote_blobs_naming/test_backward_compatibility.py	18799
test_disk_over_web_server/test.py	18753
test_storage_kafka/test_compression_codec.py	18582
test_storage_kafka/test_schema_registry_skip_bytes.py	18576
test_database_delta/test.py	18490
test_storage_iceberg_disks/test.py	18299
test_check_table/test.py	18271
test_compatibility_merge_tree_settings/test.py	18130
test_replicated_table_attach/test.py	17943
test_keeper_memory_soft_limit/test.py	17851
test_mysql57_database_engine/test.py	17586
test_config_decryption/test_zk.py	17478
test_system_logs/test_system_logs.py	17204
test_ddl_worker_non_leader/test.py	17136
test_keeper_two_nodes_cluster/test.py	17066
test_distributed_async_insert_for_node_changes/test.py	17047
test_profile_max_sessions_for_user/test.py	17014
test_settings_profile/test.py	16232
test_ttl_move/test.py	15727
test_global_overcommit_tracker/test.py	15698
test_failed_async_inserts/test.py	15598
test_codec_encrypted/test.py	15576
test_encrypted_disk/test.py	15339
test_keeper_nodes_move/test.py	15274
test_dictionaries_all_layouts_separate_sources/test_clickhouse_remote.py	14947
test_overcommit_tracker/test.py	14817
test_backward_compatibility/test_convert_ordinary.py	14709
test_replicating_constants/test.py	14657
test_dictionaries_all_layouts_separate_sources/test_mysql.py	14490
test_graphite_merge_tree_typed/test.py	14465
test_acme_tls/test_multi_node.py	14041
test_cluster_discovery/test_password.py	14038
test_replicated_user_defined_functions/test.py	13997
test_acme_tls/test_single_node.py	13904
test_postgresql_database_engine/test.py	13869
test_replicated_database_alter_modify_order_by/test.py	13632
test_storage_iceberg_with_spark/test_writes_field_partitioning.py	13566
test_analyzer_compatibility/test.py	13207
test_parallel_replicas_distributed_skip_shards/test.py	12977
test_storage_iceberg_with_spark/test_writes_with_partitioned_table.py	12758
test_modify_engine_on_restart/test_storage_policies.py	12727
test_modify_engine_on_restart/test_unusual_path.py	12722
test_modify_engine_on_restart/test_ordinary.py	12703
test_dremio_engine/test.py	12662
test_parallel_replicas_custom_key_failover/test.py	12629
test_modify_engine_on_restart/test_zk_path_exists.py	12549
test_dictionaries_postgresql/test.py	12164
test_config_decryption/test.py	12026
test_scheduler/test.py	11888
test_dictionaries_all_layouts_separate_sources/test_mongo_uri.py	11842
test_cluster_discovery/test_dynamic_clusters.py	11830
test_input_format_parallel_parsing_memory_tracking/test.py	11828
test_cluster_discovery/test.py	11826
test_modify_engine_on_restart/test_args.py	11803
test_dns_cache/test.py	11793
test_parallel_replicas_all_marks_read/test.py	11783
test_storage_s3_intelligent_tier/test.py	11774
test_attach_with_different_projections_or_indices/test.py	11763
test_database_iceberg_lakekeeper_catalog/test.py	11756
test_s3_imds/test_simple.py	11755
test_session_log/test.py	11755
test_dictionaries_redis/test.py	11739
test_modify_engine_on_restart/test_mv.py	11723
test_grpc_protocol_ssl/test.py	11718
test_dictionaries_select_all/test.py	11718
test_keeper_mntr_data_size/test.py	11717
test_dictionaries_all_layouts_separate_sources/test_https.py	11708
test_distributed_respect_user_timeouts/test.py	11706
test_MemoryTracking/test.py	11703
test_storage_redis/test.py	11702
test_ddl_worker_replicas/test.py	11699
test_dictionaries_all_layouts_separate_sources/test_file.py	11687
test_s3_style_link/test.py	11686
test_refreshable_mv_skip_old_temp_table_ddls/test.py	11669
test_dictionaries_redis/test_long.py	11662
test_dictionaries_all_layouts_separate_sources/test_http.py	11661
test_storage_s3/test_sts.py	11659
test_postpone_failed_tasks/test.py	11654
test_user_grants_from_config/test.py	11652
test_allowed_client_hosts/test.py	11649
test_relative_filepath/test.py	11641
test_table_function_redis/test.py	11639
test_keeper_session/test.py	11626
test_check_table_name_length/test.py	11608
test_keeper_persistent_log_multinode/test.py	11608
test_s3_table_functions/test.py	11607
test_aggregation_memory_efficient/test.py	11606
test_executable_udf_names_in_system_query_log/test.py	11603
test_s3_imds/test_session_token.py	11597
test_undrop_query/test.py	11596
test_dictionaries_all_layouts_separate_sources/test_executable_hashed.py	11594
test_s3_access_headers/test.py	11583
test_arrowflight_storage/test.py	11582
test_sql_user_defined_functions_on_cluster/test.py	11580
test_merge_tree_check_part_with_cache/test.py	11566
test_modify_engine_on_restart/test.py	11560
test_external_http_authenticator/test.py	11550
test_disk_access_storage/test.py	11544
test_dictionaries_all_layouts_separate_sources/test_mongo.py	11530
test_storage_iceberg_with_spark/test_writes_mutate_delete.py	11529
test_cow_policy/test.py	11524
test_keeper_restore_from_snapshot/test_disk_s3.py	11515
test_dictionaries_all_layouts_separate_sources/test_clickhouse_local.py	11508
test_alter_update_cast_keep_nullable/test.py	11504
test_dictionaries_all_layouts_separate_sources/test_executable_cache.py	11500
test_storage_iceberg_with_spark/test_writes_multiple_threads.py	11485
test_zookeeper_fallback_session/test.py	11471
test_keeper_path_acl/test.py	11466
test_config_decryption/test_zk_secure.py	11465
test_storage_iceberg_with_spark/test_restart_broken_s3.py	11464
test_storage_iceberg_with_spark/test_schema_inference.py	11460
test_materialized_view_restart_server/test.py	11456
test_freeze_table/test.py	11440
test_storage_iceberg_schema_evolution/test_evolved_schema_complex.py	11424
test_storage_iceberg_schema_evolution/test_map_evolved_nested.py	11421
test_storage_iceberg_schema_evolution/test_full_drop.py	11413
test_storage_iceberg_schema_evolution/test_tuple_evolved_nested.py	11406
test_storage_s3/test_invalid_env_credentials.py	11393
test_server_overload/test.py	11388
test_storage_iceberg_with_spark/test_partition_pruning.py	11388
test_mysql_database_engine/test.py	11342
test_crash_log/test.py	11312
test_ytsaurus/test_dictionaries.py	10831
test_ytsaurus/test_tables.py	10794
test_system_queries/test.py	8358
test_keeper_snapshot_on_exit/test.py	7171
test_keeper_snapshots_multinode/test.py	6811
test_server_initialization/test.py	6811
test_keeper_feature_flags_config/test.py	6300
test_startup_scripts/test.py	6217
test_config_corresponding_root/test.py	6175
test_distributed_default_database/test.py	6072
test_enable_user_name_access_type/test.py	5869
test_keeper_disks/test.py	5815
test_storage_iceberg_with_spark/test_cluster_table_function.py	5810
test_storage_iceberg_with_spark/test_writes.py	5797
test_filesystem_cache_uninitialized/test.py	5778
test_storage_iceberg_with_spark/test_writes_mutate_update.py	5734
test_keeper_restore_from_snapshot/test.py	3439
test_keeper_http_control/test.py	3400
test_userspace_page_cache/test_incorrect_limits.py	824
test_storage_iceberg_no_spark/test_writes_multiple_files.py	130
test_refreshable_mat_view/test.py	111
test_storage_iceberg_with_spark/test_position_deletes.py	9
test_storage_iceberg_schema_evolution/test_array_evolved_nested.py	8
test_storage_iceberg_schema_evolution/test_evolved_schema_simple.py	8
test_storage_iceberg_with_spark/test_metadata_file_format_with_uuid.py	4
test_distributed_over_distributed/test.py	3
test_http_handlers_config/test.py	3
test_storage_iceberg_with_spark/test_metadata_file_selection.py	3
test_storage_iceberg_with_spark/test_explicit_metadata_file.py	2
test_storage_iceberg_with_spark/test_minmax_pruning.py	2
test_config_decryption/test_wrong_settings.py	1
test_storage_iceberg_with_spark/test_partition_pruning_with_subquery_set.py	0
test_storage_iceberg_with_spark/test_partition_by.py	0
test_storage_iceberg_with_spark/test_minmax_pruning_with_null.py	0
test_config_yaml_main/test.py	0
test_storage_iceberg_no_spark/test_graceful_error_not_configured_iceberg_metadata_log.py	0
test_storage_iceberg_with_spark/test_pruning_nullable_bug.py	0
test_storage_iceberg_with_spark/test_schema_evolution_with_time_travel.py	0
test_storage_iceberg_no_spark/test_read_in_order_with_pyiceberg.py	0
test_storage_iceberg_with_spark/test_types.py	0
test_storage_iceberg_no_spark/test_writes_nullable_bugs2.py	0
test_cgroup_limit/test.py	0
test_storage_iceberg_with_spark/test_metadata_cache.py	0
test_storage_iceberg_with_spark/test_cluster_table_function_with_partition_pruning.py	0
test_system_reload_async_metrics/test_async_metrics_invalid_settings.py	0
test_storage_iceberg_with_spark/test_read_in_order.py	0
test_storage_iceberg_with_spark/test_writes_drop_table.py	0
test_config_xml_full/test.py	0
test_storage_iceberg_schema_evolution/test_correct_column_mapper_is_chosen.py	0
test_storage_iceberg_with_spark/test_filesystem_cache.py	0
test_storage_iceberg_with_spark/test_writes_create_version_hint.py	0
test_storage_iceberg_with_spark/test_writes_schema_evolution.py	0
test_storage_iceberg_with_spark/test_relevant_iceberg_schema_chosen.py	0
test_storage_iceberg_no_spark/test_time_travel_bug_fix_validation.py	0
test_storage_iceberg_with_spark/test_delete_files.py	0
test_validate_threadpool_writer_pool_size/test.py	0
test_storage_iceberg_with_spark/test_writes_create_table.py	0
test_config_yaml_merge_keys/test.py	0
test_storage_iceberg_with_spark/test_optimize.py	0
test_storage_iceberg_with_spark/test_system_iceberg_metadata.py	0
test_storage_iceberg_with_spark/test_compressed_metadata.py	0
test_storage_iceberg_with_spark/test_single_iceberg_file.py	0
test_jemalloc_percpu_arena/test.py	0
test_storage_iceberg_schema_evolution/test_array_evolved_with_struct.py	0
test_disks_app_interactive/test.py	0
test_storage_iceberg_with_spark/test_writes_create_partitioned_table.py	0
test_storage_iceberg_with_spark/test_iceberg_snapshot_reads.py	0
test_storage_iceberg_with_spark/test_writes_complex_type.py	0
test_config_xml_main/test.py	0
test_storage_iceberg_no_spark/test_writes_multiple_threads.py	0
test_concurrent_backups_s3/test.py	0
test_config_xml_yaml_mix/test.py	0
test_search_orphaned_parts/test.py	0
test_config_decryption/test_wrong_settings_zk.py	0
test_storage_iceberg_with_spark/test_metadata_file_selection_from_version_hint.py	0
test_storage_iceberg_with_spark/test_minmax_pruning_for_arrays_and_maps_subfields_disabled.py	0
test_keeper_three_nodes_start/test.py	0
test_config_yaml_full/test.py	0
test_storage_iceberg_with_spark/test_multiple_iceberg_file.py	0
test_storage_iceberg_with_spark/test_explanation.py	0
test_storage_iceberg_with_spark/test_writes_different_path_format_error.py	0
test_storage_iceberg_with_spark/test_writes_from_zero.py	0
test_storage_iceberg_with_spark/test_bucket_partition_pruning.py	0
"""


def _parse_raw_durations(raw: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for line in raw.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Accept both tab- and space-separated formats; last token is duration
        parts = line.split()
        try:
            duration = int(parts[-1])
        except Exception:
            continue
        path = " ".join(parts[:-1])
        out[path] = duration
    return out


TEST_DURATIONS: dict[str, int] = _parse_raw_durations(RAW_TEST_DURATIONS)


def get_optimal_test_batch(
    tests: list[str], total_batches: int, batch_num: int, num_workers: int
) -> tuple[list[str], list[str]]:
    """
    @tests - all tests to run
    @total_batches - total number of batches
    @batch_num - current batch number
    @num_workers - number of parallel workers in a batch
    returns optimal subset of parallel tests for batch_num and optimal subset of sequential tests for batch_num, based on data in TEST_DURATIONS.
    Test files not present in TEST_DURATIONS will be distributed by round robin.
    The function optimizes tail latency of batch with num_workers parallel workers.
    The function works in a deterministic way, so that batch calculated on the other machine with the same input generates the same result.
    """
    # parallel_skip_prefixes sanity check
    for test_config in TEST_CONFIGS:
        assert any(
            test_file.removeprefix("./").startswith(test_config.prefix)
            for test_file in tests
        ), f"No test files found for prefix [{test_config.prefix}] in [{tests}]"

    sequential_test_modules = [
        test_file
        for test_file in tests
        if any(test_file.startswith(test_config.prefix) for test_config in TEST_CONFIGS)
    ]
    parallel_test_modules = [
        test_file for test_file in tests if test_file not in sequential_test_modules
    ]

    if batch_num > total_batches:
        raise ValueError(f"batch_num must be in [1, {total_batches}], got {batch_num}")

    # Helper: group tests by their top-level directory (prefix)
    #  same prefix tests are grouped together to minimize docker pulls in test fixtures in each job batch
    def group_by_prefix(items: list[str]) -> dict[str, list[str]]:
        groups: dict[str, list[str]] = {}
        for it in sorted(items):
            prefix = it.split("/", 1)[0]
            groups.setdefault(prefix, []).append(it)
        return groups

    # Parallel groups and Sequential groups separated to allow distinct packing
    parallel_groups = group_by_prefix(parallel_test_modules)
    sequential_groups = group_by_prefix(sequential_test_modules)

    # Compute group durations as sum of known test durations within the group
    def groups_with_durations(groups: dict[str, list[str]]):
        known_groups: list[tuple[str, int]] = []  # (prefix, duration)
        unknown_groups: list[str] = []  # prefixes with zero known duration
        for prefix, items in sorted(groups.items()):
            dur = sum(TEST_DURATIONS.get(t, 0) for t in items)
            if dur > 0:
                known_groups.append((prefix, dur))
            else:
                unknown_groups.append(prefix)
        # Sort known by (-duration, prefix) for deterministic LPT
        known_groups.sort(key=lambda x: (-x[1], x[0]))
        # Sort unknown prefixes to make RR deterministic
        unknown_groups.sort()
        return known_groups, unknown_groups

    p_known, p_unknown = groups_with_durations(parallel_groups)
    s_known, s_unknown = groups_with_durations(sequential_groups)

    # Prepare batch containers and weights
    parallel_batches: list[list[str]] = [[] for _ in range(total_batches)]
    parallel_weights: list[int] = [0] * total_batches

    # LPT assign known-duration parallel groups
    for prefix, dur in p_known:
        idx = min(range(total_batches), key=lambda i: (parallel_weights[i], i))
        # prefix, dur sorted in p_known starting with longest duration - keep the order in batches to decrease tail latency
        parallel_batches[idx].extend(parallel_groups[prefix])
        parallel_weights[idx] += dur

    # Sort tests within each batch by duration (longest first) to minimize tail latency
    # when tests are picked by workers from the queue
    for idx in range(total_batches):
        parallel_batches[idx].sort(key=lambda x: (-TEST_DURATIONS[x], x))

    # Round-robin assign unknown-duration parallel groups
    for i, prefix in enumerate(p_unknown):
        idx = i % total_batches
        parallel_batches[idx].extend(parallel_groups[prefix])

    # Sequential batches: start from scaled parallel weights to account for worker concurrency
    sequential_batches: list[list[str]] = [[] for _ in range(total_batches)]
    sequential_weights: list[int] = [0] * total_batches

    # LPT assign known-duration sequential groups
    for prefix, dur in s_known:
        idx = min(range(total_batches), key=lambda i: (sequential_weights[i], i))
        # prefix, dur sorted in s_known starting with longest duration - keep the order in batches to decrease tail latency
        sequential_batches[idx].extend(sequential_groups[prefix])
        sequential_weights[idx] += dur

    # Round-robin assign unknown-duration sequential groups
    for i, prefix in enumerate(s_unknown):
        idx = i % total_batches
        sequential_batches[idx].extend(sequential_groups[prefix])

    print(
        f"Batches parallel weights: [{[weight // num_workers // 1000 for weight in parallel_weights]}]"
    )
    print(f"Batches weights: [{[weight // 1000 for weight in sequential_weights]}]")

    # Sanity check (non-fatal): ensure total test count preserved
    total_assigned = sum(len(b) for b in parallel_batches) + sum(
        len(b) for b in sequential_batches
    )
    assert total_assigned == len(tests)

    return parallel_batches[batch_num - 1], sequential_batches[batch_num - 1]
