# swagger_client.RunbookSnapshotsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_runbook_snapshot**](RunbookSnapshotsApi.md#create_runbook_snapshot) | **POST** /api/runbookSnapshots | Create a RunbookSnapshotResource
[**create_runbook_snapshot_snapshot_variables**](RunbookSnapshotsApi.md#create_runbook_snapshot_snapshot_variables) | **POST** /api/runbookSnapshots/{id}/snapshot-variables | 
[**create_runbook_snapshot_snapshot_variables_spaces**](RunbookSnapshotsApi.md#create_runbook_snapshot_snapshot_variables_spaces) | **POST** /api/{baseSpaceId}/runbookSnapshots/{id}/snapshot-variables | 
[**create_runbook_snapshot_spaces**](RunbookSnapshotsApi.md#create_runbook_snapshot_spaces) | **POST** /api/{baseSpaceId}/runbookSnapshots | Create a RunbookSnapshotResource
[**delete_runbook_snapshot**](RunbookSnapshotsApi.md#delete_runbook_snapshot) | **DELETE** /api/runbookSnapshots/{id} | Delete a RunbookSnapshotResource by ID
[**delete_runbook_snapshot_spaces**](RunbookSnapshotsApi.md#delete_runbook_snapshot_spaces) | **DELETE** /api/{baseSpaceId}/runbookSnapshots/{id} | Delete a RunbookSnapshotResource by ID
[**get_runbook_run_preview_for_runbook_snapshot**](RunbookSnapshotsApi.md#get_runbook_run_preview_for_runbook_snapshot) | **GET** /api/runbookSnapshots/{id}/runbookRuns/preview/{environment}/{tenant?} | 
[**get_runbook_run_preview_for_runbook_snapshot_spaces**](RunbookSnapshotsApi.md#get_runbook_run_preview_for_runbook_snapshot_spaces) | **GET** /api/{baseSpaceId}/runbookSnapshots/{id}/runbookRuns/preview/{environment}/{tenant?} | 
[**get_runbook_run_template_for_runbook_snapshot**](RunbookSnapshotsApi.md#get_runbook_run_template_for_runbook_snapshot) | **GET** /api/runbookSnapshots/{id}/runbookRuns/template | 
[**get_runbook_run_template_for_runbook_snapshot_spaces**](RunbookSnapshotsApi.md#get_runbook_run_template_for_runbook_snapshot_spaces) | **GET** /api/{baseSpaceId}/runbookSnapshots/{id}/runbookRuns/template | 
[**get_runbook_snapshot_by_id**](RunbookSnapshotsApi.md#get_runbook_snapshot_by_id) | **GET** /api/runbookSnapshots/{id} | Get a RunbookSnapshotResource by ID
[**get_runbook_snapshot_by_id_spaces**](RunbookSnapshotsApi.md#get_runbook_snapshot_by_id_spaces) | **GET** /api/{baseSpaceId}/runbookSnapshots/{id} | Get a RunbookSnapshotResource by ID
[**get_runbook_snapshot_by_project_and_name**](RunbookSnapshotsApi.md#get_runbook_snapshot_by_project_and_name) | **GET** /api/projects/{id}/runbookSnapshots/{name} | 
[**get_runbook_snapshot_by_project_and_name_spaces**](RunbookSnapshotsApi.md#get_runbook_snapshot_by_project_and_name_spaces) | **GET** /api/{baseSpaceId}/projects/{id}/runbookSnapshots/{name} | 
[**index_project_runbook_snapshots**](RunbookSnapshotsApi.md#index_project_runbook_snapshots) | **GET** /api/projects/{id}/runbookSnapshots | Get a list of RunbookSnapshotResources for the given ProjectResource
[**index_project_runbook_snapshots_spaces**](RunbookSnapshotsApi.md#index_project_runbook_snapshots_spaces) | **GET** /api/{baseSpaceId}/projects/{id}/runbookSnapshots | Get a list of RunbookSnapshotResources for the given ProjectResource
[**index_runbook_runbook_snapshots**](RunbookSnapshotsApi.md#index_runbook_runbook_snapshots) | **GET** /api/runbooks/{id}/runbookSnapshots | Get a list of RunbookSnapshotResources for the given RunbookResource
[**index_runbook_runbook_snapshots_spaces**](RunbookSnapshotsApi.md#index_runbook_runbook_snapshots_spaces) | **GET** /api/{baseSpaceId}/runbooks/{id}/runbookSnapshots | Get a list of RunbookSnapshotResources for the given RunbookResource
[**index_runbook_snapshot_runbook_runs**](RunbookSnapshotsApi.md#index_runbook_snapshot_runbook_runs) | **GET** /api/runbookSnapshots/{id}/runbookRuns | Get a list of RunbookRunResources for the given RunbookSnapshotResource
[**index_runbook_snapshot_runbook_runs_spaces**](RunbookSnapshotsApi.md#index_runbook_snapshot_runbook_runs_spaces) | **GET** /api/{baseSpaceId}/runbookSnapshots/{id}/runbookRuns | Get a list of RunbookRunResources for the given RunbookSnapshotResource
[**index_runbook_snapshots**](RunbookSnapshotsApi.md#index_runbook_snapshots) | **GET** /api/runbookSnapshots | Get a list of RunbookSnapshotResources
[**index_runbook_snapshots_spaces**](RunbookSnapshotsApi.md#index_runbook_snapshots_spaces) | **GET** /api/{baseSpaceId}/runbookSnapshots | Get a list of RunbookSnapshotResources
[**update_runbook_snapshot**](RunbookSnapshotsApi.md#update_runbook_snapshot) | **PUT** /api/runbookSnapshots/{id} | Modify a RunbookSnapshotResource by ID
[**update_runbook_snapshot_spaces**](RunbookSnapshotsApi.md#update_runbook_snapshot_spaces) | **PUT** /api/{baseSpaceId}/runbookSnapshots/{id} | Modify a RunbookSnapshotResource by ID

# **create_runbook_snapshot**
> RunbookSnapshotResource create_runbook_snapshot(body=body)

Create a RunbookSnapshotResource

Creates a new snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RunbookSnapshotResource() # RunbookSnapshotResource | The RunbookSnapshotResource resource to create (optional)

try:
    # Create a RunbookSnapshotResource
    api_response = api_instance.create_runbook_snapshot(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->create_runbook_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunbookSnapshotResource**](RunbookSnapshotResource.md)| The RunbookSnapshotResource resource to create | [optional] 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_runbook_snapshot_snapshot_variables**
> RunbookSnapshotResource create_runbook_snapshot_snapshot_variables(id)



Refresh the variable snapshots associated with the runbook snapshot. The runbook's process must not have changed since the snapshot was created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.create_runbook_snapshot_snapshot_variables(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->create_runbook_snapshot_snapshot_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_runbook_snapshot_snapshot_variables_spaces**
> RunbookSnapshotResource create_runbook_snapshot_snapshot_variables_spaces(base_space_id, id)



Refresh the variable snapshots associated with the runbook snapshot. The runbook's process must not have changed since the snapshot was created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.create_runbook_snapshot_snapshot_variables_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->create_runbook_snapshot_snapshot_variables_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_runbook_snapshot_spaces**
> RunbookSnapshotResource create_runbook_snapshot_spaces(base_space_id, body=body)

Create a RunbookSnapshotResource

Creates a new snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
body = swagger_client.RunbookSnapshotResource() # RunbookSnapshotResource | The RunbookSnapshotResource resource to create (optional)

try:
    # Create a RunbookSnapshotResource
    api_response = api_instance.create_runbook_snapshot_spaces(base_space_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->create_runbook_snapshot_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **body** | [**RunbookSnapshotResource**](RunbookSnapshotResource.md)| The RunbookSnapshotResource resource to create | [optional] 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_runbook_snapshot**
> delete_runbook_snapshot(id)

Delete a RunbookSnapshotResource by ID

Deletes an existing snapshot, along with all of the runs, tasks and other associated resources belonging to the snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the RunbookSnapshotResource to delete

try:
    # Delete a RunbookSnapshotResource by ID
    api_instance.delete_runbook_snapshot(id)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->delete_runbook_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the RunbookSnapshotResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_runbook_snapshot_spaces**
> delete_runbook_snapshot_spaces(base_space_id, id)

Delete a RunbookSnapshotResource by ID

Deletes an existing snapshot, along with all of the runs, tasks and other associated resources belonging to the snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the RunbookSnapshotResource to delete

try:
    # Delete a RunbookSnapshotResource by ID
    api_instance.delete_runbook_snapshot_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->delete_runbook_snapshot_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the RunbookSnapshotResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_run_preview_for_runbook_snapshot**
> RunbookRunPreviewResource get_runbook_run_preview_for_runbook_snapshot(environment, tenant, id)



Gets a document that describes what steps will/won't be run during a run to a given environment (and tenant if supplied).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
environment = 'environment_example' # str | ID of the environment
tenant = 'tenant_example' # str | ID of the tenant
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_runbook_run_preview_for_runbook_snapshot(environment, tenant, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_run_preview_for_runbook_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| ID of the environment | 
 **tenant** | **str**| ID of the tenant | 
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookRunPreviewResource**](RunbookRunPreviewResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_run_preview_for_runbook_snapshot_spaces**
> RunbookRunPreviewResource get_runbook_run_preview_for_runbook_snapshot_spaces(base_space_id, environment, tenant, id)



Gets a document that describes what steps will/won't be run during a run to a given environment (and tenant if supplied).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
environment = 'environment_example' # str | ID of the environment
tenant = 'tenant_example' # str | ID of the tenant
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_runbook_run_preview_for_runbook_snapshot_spaces(base_space_id, environment, tenant, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_run_preview_for_runbook_snapshot_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **environment** | **str**| ID of the environment | 
 **tenant** | **str**| ID of the tenant | 
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookRunPreviewResource**](RunbookRunPreviewResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_run_template_for_runbook_snapshot**
> RunbookRunTemplateResource get_runbook_run_template_for_runbook_snapshot(id)



Gets all of the information necessary for creating or editing a run for this snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_runbook_run_template_for_runbook_snapshot(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_run_template_for_runbook_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookRunTemplateResource**](RunbookRunTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_run_template_for_runbook_snapshot_spaces**
> RunbookRunTemplateResource get_runbook_run_template_for_runbook_snapshot_spaces(base_space_id, id)



Gets all of the information necessary for creating or editing a run for this snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_runbook_run_template_for_runbook_snapshot_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_run_template_for_runbook_snapshot_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookRunTemplateResource**](RunbookRunTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_snapshot_by_id**
> RunbookSnapshotResource get_runbook_snapshot_by_id(id)

Get a RunbookSnapshotResource by ID

Gets a snapshot by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the RunbookSnapshotResource to load

try:
    # Get a RunbookSnapshotResource by ID
    api_response = api_instance.get_runbook_snapshot_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_snapshot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the RunbookSnapshotResource to load | 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_snapshot_by_id_spaces**
> RunbookSnapshotResource get_runbook_snapshot_by_id_spaces(base_space_id, id)

Get a RunbookSnapshotResource by ID

Gets a snapshot by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the RunbookSnapshotResource to load

try:
    # Get a RunbookSnapshotResource by ID
    api_response = api_instance.get_runbook_snapshot_by_id_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_snapshot_by_id_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the RunbookSnapshotResource to load | 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_snapshot_by_project_and_name**
> RunbookSnapshotResource get_runbook_snapshot_by_project_and_name(name, id)



Gets a single runbookSnapshot by project ID and name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of the runbook
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_runbook_snapshot_by_project_and_name(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_snapshot_by_project_and_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the runbook | 
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runbook_snapshot_by_project_and_name_spaces**
> RunbookSnapshotResource get_runbook_snapshot_by_project_and_name_spaces(base_space_id, name, id)



Gets a single runbookSnapshot by project ID and name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
name = 'name_example' # str | Name of the runbook
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_runbook_snapshot_by_project_and_name_spaces(base_space_id, name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->get_runbook_snapshot_by_project_and_name_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **name** | **str**| Name of the runbook | 
 **id** | **str**| ID of the resource | 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_project_runbook_snapshots**
> ResourceCollectionRunbookSnapshotResource index_project_runbook_snapshots(id, skip=skip, take=take)

Get a list of RunbookSnapshotResources for the given ProjectResource

Lists all of the runbookSnapshots that belong to the given project. RunbookSnapshots will be ordered from most recent to least recent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the Project
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of RunbookSnapshotResources for the given ProjectResource
    api_response = api_instance.index_project_runbook_snapshots(id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_project_runbook_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Project | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionRunbookSnapshotResource**](ResourceCollectionRunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_project_runbook_snapshots_spaces**
> ResourceCollectionRunbookSnapshotResource index_project_runbook_snapshots_spaces(base_space_id, id, skip=skip, take=take)

Get a list of RunbookSnapshotResources for the given ProjectResource

Lists all of the runbookSnapshots that belong to the given project. RunbookSnapshots will be ordered from most recent to least recent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the Project
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of RunbookSnapshotResources for the given ProjectResource
    api_response = api_instance.index_project_runbook_snapshots_spaces(base_space_id, id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_project_runbook_snapshots_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the Project | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionRunbookSnapshotResource**](ResourceCollectionRunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_runbook_runbook_snapshots**
> ResourceCollectionRunbookSnapshotResource index_runbook_runbook_snapshots(id, skip=skip, take=take)

Get a list of RunbookSnapshotResources for the given RunbookResource

Lists all of the runbookSnapshots that belong to the given runbook. RunbookSnapshots will be ordered from most recent to least recent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the Runbook
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of RunbookSnapshotResources for the given RunbookResource
    api_response = api_instance.index_runbook_runbook_snapshots(id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_runbook_runbook_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Runbook | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionRunbookSnapshotResource**](ResourceCollectionRunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_runbook_runbook_snapshots_spaces**
> ResourceCollectionRunbookSnapshotResource index_runbook_runbook_snapshots_spaces(base_space_id, id, skip=skip, take=take)

Get a list of RunbookSnapshotResources for the given RunbookResource

Lists all of the runbookSnapshots that belong to the given runbook. RunbookSnapshots will be ordered from most recent to least recent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the Runbook
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of RunbookSnapshotResources for the given RunbookResource
    api_response = api_instance.index_runbook_runbook_snapshots_spaces(base_space_id, id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_runbook_runbook_snapshots_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the Runbook | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionRunbookSnapshotResource**](ResourceCollectionRunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_runbook_snapshot_runbook_runs**
> ResourceCollectionRunbookRunResource index_runbook_snapshot_runbook_runs(id, skip=skip, take=take)

Get a list of RunbookRunResources for the given RunbookSnapshotResource

Lists all of the runs that belong to the given snapshot. Runs will be ordered from most recent to least recent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the RunbookSnapshot
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of RunbookRunResources for the given RunbookSnapshotResource
    api_response = api_instance.index_runbook_snapshot_runbook_runs(id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_runbook_snapshot_runbook_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the RunbookSnapshot | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionRunbookRunResource**](ResourceCollectionRunbookRunResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_runbook_snapshot_runbook_runs_spaces**
> ResourceCollectionRunbookRunResource index_runbook_snapshot_runbook_runs_spaces(base_space_id, id, skip=skip, take=take)

Get a list of RunbookRunResources for the given RunbookSnapshotResource

Lists all of the runs that belong to the given snapshot. Runs will be ordered from most recent to least recent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the RunbookSnapshot
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of RunbookRunResources for the given RunbookSnapshotResource
    api_response = api_instance.index_runbook_snapshot_runbook_runs_spaces(base_space_id, id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_runbook_snapshot_runbook_runs_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the RunbookSnapshot | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionRunbookRunResource**](ResourceCollectionRunbookRunResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_runbook_snapshots**
> ResourceCollectionRunbookSnapshotResource index_runbook_snapshots(skip=skip, take=take)

Get a list of RunbookSnapshotResources

Lists all of the snapshots in the supplied Octopus Deploy Space, from all projects. The results will be sorted from most recent to least recent snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of RunbookSnapshotResources
    api_response = api_instance.index_runbook_snapshots(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_runbook_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionRunbookSnapshotResource**](ResourceCollectionRunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_runbook_snapshots_spaces**
> ResourceCollectionRunbookSnapshotResource index_runbook_snapshots_spaces(base_space_id, skip=skip, take=take)

Get a list of RunbookSnapshotResources

Lists all of the snapshots in the supplied Octopus Deploy Space, from all projects. The results will be sorted from most recent to least recent snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of RunbookSnapshotResources
    api_response = api_instance.index_runbook_snapshots_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->index_runbook_snapshots_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionRunbookSnapshotResource**](ResourceCollectionRunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_runbook_snapshot**
> RunbookSnapshotResource update_runbook_snapshot(id, body=body)

Modify a RunbookSnapshotResource by ID

Updates an existing snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the RunbookSnapshotResource to modify
body = swagger_client.RunbookSnapshotResource() # RunbookSnapshotResource | The RunbookSnapshotResource resource to create (optional)

try:
    # Modify a RunbookSnapshotResource by ID
    api_response = api_instance.update_runbook_snapshot(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->update_runbook_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the RunbookSnapshotResource to modify | 
 **body** | [**RunbookSnapshotResource**](RunbookSnapshotResource.md)| The RunbookSnapshotResource resource to create | [optional] 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_runbook_snapshot_spaces**
> RunbookSnapshotResource update_runbook_snapshot_spaces(base_space_id, id, body=body)

Modify a RunbookSnapshotResource by ID

Updates an existing snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RunbookSnapshotsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the RunbookSnapshotResource to modify
body = swagger_client.RunbookSnapshotResource() # RunbookSnapshotResource | The RunbookSnapshotResource resource to create (optional)

try:
    # Modify a RunbookSnapshotResource by ID
    api_response = api_instance.update_runbook_snapshot_spaces(base_space_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunbookSnapshotsApi->update_runbook_snapshot_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the RunbookSnapshotResource to modify | 
 **body** | [**RunbookSnapshotResource**](RunbookSnapshotResource.md)| The RunbookSnapshotResource resource to create | [optional] 

### Return type

[**RunbookSnapshotResource**](RunbookSnapshotResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

