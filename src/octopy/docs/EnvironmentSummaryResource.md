# EnvironmentSummaryResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**EnvironmentResource**](EnvironmentResource.md) |  | [optional] 
**total_machines** | **int** |  | [optional] 
**total_disabled_machines** | **int** |  | [optional] 
**machine_health_status_summaries** | **dict(str, int)** |  | [optional] 
**machine_endpoint_summaries** | **dict(str, int)** |  | [optional] 
**machine_tenant_summaries** | **dict(str, int)** |  | [optional] 
**machine_tenant_tag_summaries** | **dict(str, int)** |  | [optional] 
**tentacle_upgrades_required** | **bool** |  | [optional] 
**machine_ids_for_calamari_upgrade** | **list[str]** |  | [optional] 
**machine_ids_for_tentacle_upgrade** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

