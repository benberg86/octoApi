# LicenseStatusResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_compliant** | **bool** |  | [optional] 
**hosting_environment** | **str** |  | [optional] 
**compliance_summary** | **str** |  | [optional] 
**effective_expiry_date** | **date** |  | [optional] 
**days_to_effective_expiry_date** | **int** |  | [optional] 
**messages** | [**list[LicenseMessageResource]**](LicenseMessageResource.md) |  | [optional] 
**limits** | [**list[LicenseLimitStatusResource]**](LicenseLimitStatusResource.md) |  | [optional] 
**effective_node_task_limit** | **int** |  | [optional] 
**effective_cluster_task_limit** | **int** |  | [optional] 
**is_node_task_limit_controlled_by_license** | **bool** |  | [optional] 
**is_cluster_task_limit_controlled_by_license** | **bool** |  | [optional] 
**permissions_mode** | **str** |  | [optional] 
**does_expiry_block_key_activities** | **bool** |  | [optional] 
**last_modified_on** | **datetime** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**links** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

