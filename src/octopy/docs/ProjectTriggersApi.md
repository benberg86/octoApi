# swagger_client.ProjectTriggersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_trigger**](ProjectTriggersApi.md#create_project_trigger) | **POST** /api/projecttriggers | Create a ProjectTriggerResource
[**create_project_trigger_spaces**](ProjectTriggersApi.md#create_project_trigger_spaces) | **POST** /api/{baseSpaceId}/projecttriggers | Create a ProjectTriggerResource
[**delete_project_trigger**](ProjectTriggersApi.md#delete_project_trigger) | **DELETE** /api/projecttriggers/{id} | Delete a ProjectTriggerResource by ID
[**delete_project_trigger_spaces**](ProjectTriggersApi.md#delete_project_trigger_spaces) | **DELETE** /api/{baseSpaceId}/projecttriggers/{id} | Delete a ProjectTriggerResource by ID
[**get_project_trigger_by_id**](ProjectTriggersApi.md#get_project_trigger_by_id) | **GET** /api/projecttriggers/{id} | Get a ProjectTriggerResource by ID
[**get_project_trigger_by_id_spaces**](ProjectTriggersApi.md#get_project_trigger_by_id_spaces) | **GET** /api/{baseSpaceId}/projecttriggers/{id} | Get a ProjectTriggerResource by ID
[**index_project_project_triggers**](ProjectTriggersApi.md#index_project_project_triggers) | **GET** /api/projects/{id}/triggers | Get a list of ProjectTriggerResources for the given ProjectResource
[**index_project_project_triggers_spaces**](ProjectTriggersApi.md#index_project_project_triggers_spaces) | **GET** /api/{baseSpaceId}/projects/{id}/triggers | Get a list of ProjectTriggerResources for the given ProjectResource
[**index_project_triggers**](ProjectTriggersApi.md#index_project_triggers) | **GET** /api/projecttriggers | Get a list of ProjectTriggerResources
[**index_project_triggers_spaces**](ProjectTriggersApi.md#index_project_triggers_spaces) | **GET** /api/{baseSpaceId}/projecttriggers | Get a list of ProjectTriggerResources
[**update_project_trigger**](ProjectTriggersApi.md#update_project_trigger) | **PUT** /api/projecttriggers/{id} | Modify a ProjectTriggerResource by ID
[**update_project_trigger_spaces**](ProjectTriggersApi.md#update_project_trigger_spaces) | **PUT** /api/{baseSpaceId}/projecttriggers/{id} | Modify a ProjectTriggerResource by ID

# **create_project_trigger**
> ProjectTriggerResource create_project_trigger(body=body)

Create a ProjectTriggerResource

Creates a new project trigger

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Create a ProjectTriggerResource
    api_response = api_instance.create_project_trigger(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->create_project_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_trigger_spaces**
> ProjectTriggerResource create_project_trigger_spaces(base_space_id, body=body)

Create a ProjectTriggerResource

Creates a new project trigger

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
body = swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Create a ProjectTriggerResource
    api_response = api_instance.create_project_trigger_spaces(base_space_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->create_project_trigger_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **body** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_trigger**
> delete_project_trigger(id)

Delete a ProjectTriggerResource by ID

Deletes an existing project trigger.

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectTriggerResource to delete

try:
    # Delete a ProjectTriggerResource by ID
    api_instance.delete_project_trigger(id)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->delete_project_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectTriggerResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_trigger_spaces**
> delete_project_trigger_spaces(base_space_id, id)

Delete a ProjectTriggerResource by ID

Deletes an existing project trigger.

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectTriggerResource to delete

try:
    # Delete a ProjectTriggerResource by ID
    api_instance.delete_project_trigger_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->delete_project_trigger_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectTriggerResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_trigger_by_id**
> ProjectTriggerResource get_project_trigger_by_id(id)

Get a ProjectTriggerResource by ID

Get a project trigger

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectTriggerResource to load

try:
    # Get a ProjectTriggerResource by ID
    api_response = api_instance.get_project_trigger_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->get_project_trigger_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectTriggerResource to load | 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_trigger_by_id_spaces**
> ProjectTriggerResource get_project_trigger_by_id_spaces(base_space_id, id)

Get a ProjectTriggerResource by ID

Get a project trigger

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectTriggerResource to load

try:
    # Get a ProjectTriggerResource by ID
    api_response = api_instance.get_project_trigger_by_id_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->get_project_trigger_by_id_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectTriggerResource to load | 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_project_project_triggers**
> ResourceCollectionProjectTriggerResource index_project_project_triggers(id, skip=skip, take=take)

Get a list of ProjectTriggerResources for the given ProjectResource

Lists all the project triggers for the given project

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the Project
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of ProjectTriggerResources for the given ProjectResource
    api_response = api_instance.index_project_project_triggers(id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->index_project_project_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Project | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionProjectTriggerResource**](ResourceCollectionProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_project_project_triggers_spaces**
> ResourceCollectionProjectTriggerResource index_project_project_triggers_spaces(base_space_id, id, skip=skip, take=take)

Get a list of ProjectTriggerResources for the given ProjectResource

Lists all the project triggers for the given project

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the Project
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items per page (optional)

try:
    # Get a list of ProjectTriggerResources for the given ProjectResource
    api_response = api_instance.index_project_project_triggers_spaces(base_space_id, id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->index_project_project_triggers_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the Project | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items per page | [optional] 

### Return type

[**ResourceCollectionProjectTriggerResource**](ResourceCollectionProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_project_triggers**
> ResourceCollectionProjectTriggerResource index_project_triggers(skip=skip, take=take)

Get a list of ProjectTriggerResources

Gets all the project triggers in the supplied Octopus Deploy Space, sorted by Id

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectTriggerResources
    api_response = api_instance.index_project_triggers(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->index_project_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectTriggerResource**](ResourceCollectionProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_project_triggers_spaces**
> ResourceCollectionProjectTriggerResource index_project_triggers_spaces(base_space_id, skip=skip, take=take)

Get a list of ProjectTriggerResources

Gets all the project triggers in the supplied Octopus Deploy Space, sorted by Id

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectTriggerResources
    api_response = api_instance.index_project_triggers_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->index_project_triggers_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectTriggerResource**](ResourceCollectionProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_trigger**
> ProjectTriggerResource update_project_trigger(id, body=body)

Modify a ProjectTriggerResource by ID

Updates an existing project trigger

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectTriggerResource to modify
body = swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Modify a ProjectTriggerResource by ID
    api_response = api_instance.update_project_trigger(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->update_project_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectTriggerResource to modify | 
 **body** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_trigger_spaces**
> ProjectTriggerResource update_project_trigger_spaces(base_space_id, id, body=body)

Modify a ProjectTriggerResource by ID

Updates an existing project trigger

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
api_instance = swagger_client.ProjectTriggersApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectTriggerResource to modify
body = swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Modify a ProjectTriggerResource by ID
    api_response = api_instance.update_project_trigger_spaces(base_space_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->update_project_trigger_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectTriggerResource to modify | 
 **body** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

