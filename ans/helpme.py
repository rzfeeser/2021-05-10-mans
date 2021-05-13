import pprint

mydata = {'ontap_info': {'ontapi_version': '170', 'ontap_version': '170', 'snapmirror_info': {'napwpccu323v:vol_jh32vol_dest': {'break_failed_count': '0', 'break_successful_count': '0', 'catalog_status': 'idle', 'destination_location': 'napwpccu323v:vol_jh32vol_dest', 'destination_volume': 'vol_jh32vol_dest', 'destination_volume_node': 'napwpccu30-01', 'destination_vserver': 'napwpccu323v', 'destination_vserver_uuid': '5e3b9bea-d083-11ea-b3c5-00a098ef54fe', 'exported_snapshot': 'snapmirror.0f801738-d084-11ea-83c9-00a098ef4f6a_2162696218.2021-05-11_090500', 'exported_snapshot_timestamp': '1620741900', 'is_catalog_enabled': 'false', 'is_constituent': 'false', 'is_healthy': 'true', 'lag_time': '797', 'last_transfer_duration': '0', 'last_transfer_end_timestamp': '1620742198', 'last_transfer_from': 'napsdccu323v:jh32vol', 'last_transfer_network_compression_ratio': '1:1', 'last_transfer_size': '0', 'last_transfer_type': 'resync', 'max_transfer_rate': '0', 'mirror_state': 'snapmirrored', 'newest_snapshot': 'snapmirror.0f801738-d084-11ea-83c9-00a098ef4f6a_2162696218.2021-05-11_090500', 'newest_snapshot_timestamp': '1620741900', 'opmask': '18446744073709551615', 'policy': 'MirrorAndVault', 'policy_type': 'mirror_vault', 'relationship_control_plane': 'v2', 'relationship_group_type': 'none', 'relationship_id': 'a4727c91-8e5e-11eb-9503-00a098ef4696', 'relationship_status': 'idle', 'relationship_type': 'extended_data_protection', 'resync_failed_count': '0', 'resync_successful_count': '1', 'source_location': 'napsdccu323v:jh32vol', 'source_volume': 'jh32vol', 'source_vserver': 'napsdccu323v', 'source_vserver_uuid': '0f801738-d084-11ea-83c9-00a098ef4f6a', 'total_transfer_bytes': '0', 'total_transfer_time_secs': '0', 'update_failed_count': '0', 'update_successful_count': '0', 'vserver': 'napwpccu323v'}}}, 'state': 'info', 'changed': False, 'failed': False, 'attempts': 1}

pprint.pprint(mydata)


print( list(mydata["ontap_info"]["snapmirror_info"].keys())[0])
##ontap_info.snapmirror_info.keys()[0].relationship_status == "idle"

set_facts:
    mysterykey: "{{ ontap_info.snapmirror_info.keys() | list }}[0]"

ontap_info.snapmirror_info.mysterykey.relationship_status == "idle"
