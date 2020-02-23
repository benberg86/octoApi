# swagger_client.EventsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_by_id**](EventsApi.md#get_event_by_id) | **GET** /api/events/{id} | Get a EventResource by ID
[**get_event_by_id_spaces**](EventsApi.md#get_event_by_id_spaces) | **GET** /api/{baseSpaceId}/events/{id} | Get a EventResource by ID
[**get_list_event_agents**](EventsApi.md#get_list_event_agents) | **GET** /api/events/agents | 
[**get_list_event_agents_spaces**](EventsApi.md#get_list_event_agents_spaces) | **GET** /api/{baseSpaceId}/events/agents | 
[**get_list_event_categories**](EventsApi.md#get_list_event_categories) | **GET** /api/events/categories | 
[**get_list_event_categories_spaces**](EventsApi.md#get_list_event_categories_spaces) | **GET** /api/{baseSpaceId}/events/categories | 
[**get_list_event_document_types**](EventsApi.md#get_list_event_document_types) | **GET** /api/events/documenttypes | 
[**get_list_event_document_types_spaces**](EventsApi.md#get_list_event_document_types_spaces) | **GET** /api/{baseSpaceId}/events/documenttypes | 
[**get_list_event_groups**](EventsApi.md#get_list_event_groups) | **GET** /api/events/groups | 
[**get_list_event_groups_spaces**](EventsApi.md#get_list_event_groups_spaces) | **GET** /api/{baseSpaceId}/events/groups | 
[**get_list_events**](EventsApi.md#get_list_events) | **GET** /api/events | 
[**get_list_events_spaces**](EventsApi.md#get_list_events_spaces) | **GET** /api/{baseSpaceId}/events | 

# **get_event_by_id**
> EventResource get_event_by_id(id)

Get a EventResource by ID

Gets a single event by ID.

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the EventResource to load

try:
    # Get a EventResource by ID
    api_response = api_instance.get_event_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the EventResource to load | 

### Return type

[**EventResource**](EventResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_by_id_spaces**
> EventResource get_event_by_id_spaces(base_space_id, id)

Get a EventResource by ID

Gets a single event by ID.

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the EventResource to load

try:
    # Get a EventResource by ID
    api_response = api_instance.get_event_by_id_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event_by_id_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the EventResource to load | 

### Return type

[**EventResource**](EventResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_agents**
> list[EventAgentResource] get_list_event_agents()



Lists event agents.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()

try:
    api_response = api_instance.get_list_event_agents()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_agents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventAgentResource]**](EventAgentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_agents_spaces**
> list[EventAgentResource] get_list_event_agents_spaces(base_space_id)



Lists event agents.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.get_list_event_agents_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_agents_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EventAgentResource]**](EventAgentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_categories**
> list[EventCategoryResource] get_list_event_categories()



Lists event categories.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()

try:
    api_response = api_instance.get_list_event_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventCategoryResource]**](EventCategoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_categories_spaces**
> list[EventCategoryResource] get_list_event_categories_spaces(base_space_id)



Lists event categories.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.get_list_event_categories_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_categories_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EventCategoryResource]**](EventCategoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_document_types**
> list[DocumentTypeDocument] get_list_event_document_types()



Lists subscription event document types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()

try:
    api_response = api_instance.get_list_event_document_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_document_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DocumentTypeDocument]**](DocumentTypeDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_document_types_spaces**
> list[DocumentTypeDocument] get_list_event_document_types_spaces(base_space_id)



Lists subscription event document types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.get_list_event_document_types_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_document_types_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[DocumentTypeDocument]**](DocumentTypeDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_groups**
> list[EventGroupResource] get_list_event_groups()



Lists subscription event groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()

try:
    api_response = api_instance.get_list_event_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventGroupResource]**](EventGroupResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_event_groups_spaces**
> list[EventGroupResource] get_list_event_groups_spaces(base_space_id)



Lists subscription event groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.get_list_event_groups_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_event_groups_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EventGroupResource]**](EventGroupResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_events**
> get_list_events()



List all of the the audit events collected to date. Events can be filtered by various criteria. Events will be ordered by the date of the event, descending.

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))

try:
    api_instance.get_list_events()
except ApiException as e:
    print("Exception when calling EventsApi->get_list_events: %s\n" % e)
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

# **get_list_events_spaces**
> get_list_events_spaces(base_space_id)



List all of the the audit events collected to date. Events can be filtered by various criteria. Events will be ordered by the date of the event, descending.

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.get_list_events_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling EventsApi->get_list_events_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

