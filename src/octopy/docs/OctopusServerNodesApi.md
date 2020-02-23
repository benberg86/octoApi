# swagger_client.OctopusServerNodesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_octopus_server_node**](OctopusServerNodesApi.md#delete_octopus_server_node) | **DELETE** /api/octopusservernodes/{id} | Delete a OctopusServerNodeResource by ID
[**get_load_balancer_ping**](OctopusServerNodesApi.md#get_load_balancer_ping) | **GET** /api/octopusservernodes/ping | 
[**get_octopus_server_cluster_summary**](OctopusServerNodesApi.md#get_octopus_server_cluster_summary) | **GET** /api/octopusservernodes/summary | 
[**get_octopus_server_node_by_id**](OctopusServerNodesApi.md#get_octopus_server_node_by_id) | **GET** /api/octopusservernodes/{id} | Get a OctopusServerNodeResource by ID
[**get_octopus_server_node_details**](OctopusServerNodesApi.md#get_octopus_server_node_details) | **GET** /api/octopusservernodes/{id}/details | 
[**index_octopus_server_nodes**](OctopusServerNodesApi.md#index_octopus_server_nodes) | **GET** /api/octopusservernodes | Get a list of OctopusServerNodeResources
[**list_all_octopus_server_nodes**](OctopusServerNodesApi.md#list_all_octopus_server_nodes) | **GET** /api/octopusservernodes/all | Get a list of OctopusServerNodeResources
[**update_octopus_server_node**](OctopusServerNodesApi.md#update_octopus_server_node) | **PUT** /api/octopusservernodes/{id} | Modify a OctopusServerNodeResource by ID

# **delete_octopus_server_node**
> delete_octopus_server_node(id)

Delete a OctopusServerNodeResource by ID

Deletes an Octopus Server node.

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the OctopusServerNodeResource to delete

try:
    # Delete a OctopusServerNodeResource by ID
    api_instance.delete_octopus_server_node(id)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->delete_octopus_server_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OctopusServerNodeResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_ping**
> get_load_balancer_ping()



Returns HTTP ImATeapot (418) when the Octopus Server node is draining or offline, otherwise HTTP OK (200). Always returns the node information in the body.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OctopusServerNodesApi()

try:
    api_instance.get_load_balancer_ping()
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->get_load_balancer_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_octopus_server_cluster_summary**
> get_octopus_server_cluster_summary()



Returns all nodes, with status information

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.get_octopus_server_cluster_summary()
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->get_octopus_server_cluster_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_octopus_server_node_by_id**
> OctopusServerNodeResource get_octopus_server_node_by_id(id)

Get a OctopusServerNodeResource by ID

Gets an Octopus Server node by ID.

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the OctopusServerNodeResource to load

try:
    # Get a OctopusServerNodeResource by ID
    api_response = api_instance.get_octopus_server_node_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->get_octopus_server_node_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OctopusServerNodeResource to load | 

### Return type

[**OctopusServerNodeResource**](OctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_octopus_server_node_details**
> OctopusServerNodeDetailsResource get_octopus_server_node_details(id)



A count of the running tasks per node.

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.get_octopus_server_node_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->get_octopus_server_node_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**OctopusServerNodeDetailsResource**](OctopusServerNodeDetailsResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_octopus_server_nodes**
> ResourceCollectionOctopusServerNodeResource index_octopus_server_nodes(skip=skip, take=take)

Get a list of OctopusServerNodeResources

List all of the Octopus Server nodes participating in the current Octopus Server cluster.

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of OctopusServerNodeResources
    api_response = api_instance.index_octopus_server_nodes(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->index_octopus_server_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionOctopusServerNodeResource**](ResourceCollectionOctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_octopus_server_nodes**
> list[OctopusServerNodeResource] list_all_octopus_server_nodes()

Get a list of OctopusServerNodeResources

Lists the name and ID of all Octopus Server nodes.

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of OctopusServerNodeResources
    api_response = api_instance.list_all_octopus_server_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->list_all_octopus_server_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OctopusServerNodeResource]**](OctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_octopus_server_node**
> OctopusServerNodeResource update_octopus_server_node(id, body=body)

Modify a OctopusServerNodeResource by ID

Modifies an Octopus Server node.

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
api_instance = swagger_client.OctopusServerNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the OctopusServerNodeResource to modify
body = swagger_client.OctopusServerNodeResource() # OctopusServerNodeResource | The OctopusServerNodeResource resource to create (optional)

try:
    # Modify a OctopusServerNodeResource by ID
    api_response = api_instance.update_octopus_server_node(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->update_octopus_server_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OctopusServerNodeResource to modify | 
 **body** | [**OctopusServerNodeResource**](OctopusServerNodeResource.md)| The OctopusServerNodeResource resource to create | [optional] 

### Return type

[**OctopusServerNodeResource**](OctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

