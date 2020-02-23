# swagger_client.ScopedUserRoleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scoped_user_role**](ScopedUserRoleApi.md#create_scoped_user_role) | **POST** /api/scopeduserroles | Create a ScopedUserRoleResource
[**create_scoped_user_role_spaces**](ScopedUserRoleApi.md#create_scoped_user_role_spaces) | **POST** /api/{baseSpaceId}/scopeduserroles | Create a ScopedUserRoleResource
[**delete_scoped_user_role**](ScopedUserRoleApi.md#delete_scoped_user_role) | **DELETE** /api/scopeduserroles/{id} | Delete a ScopedUserRoleResource by ID
[**delete_scoped_user_role_spaces**](ScopedUserRoleApi.md#delete_scoped_user_role_spaces) | **DELETE** /api/{baseSpaceId}/scopeduserroles/{id} | Delete a ScopedUserRoleResource by ID
[**get_list_scoped_user_role**](ScopedUserRoleApi.md#get_list_scoped_user_role) | **GET** /api/scopeduserroles | 
[**get_list_scoped_user_role_spaces**](ScopedUserRoleApi.md#get_list_scoped_user_role_spaces) | **GET** /api/{baseSpaceId}/scopeduserroles | 
[**get_scoped_user_role_by_id**](ScopedUserRoleApi.md#get_scoped_user_role_by_id) | **GET** /api/scopeduserroles/{id} | Get a ScopedUserRoleResource by ID
[**get_scoped_user_role_by_id_spaces**](ScopedUserRoleApi.md#get_scoped_user_role_by_id_spaces) | **GET** /api/{baseSpaceId}/scopeduserroles/{id} | Get a ScopedUserRoleResource by ID
[**update_scoped_user_role**](ScopedUserRoleApi.md#update_scoped_user_role) | **PUT** /api/scopeduserroles/{id} | Modify a ScopedUserRoleResource by ID
[**update_scoped_user_role_spaces**](ScopedUserRoleApi.md#update_scoped_user_role_spaces) | **PUT** /api/{baseSpaceId}/scopeduserroles/{id} | Modify a ScopedUserRoleResource by ID

# **create_scoped_user_role**
> ScopedUserRoleResource create_scoped_user_role(body=body)

Create a ScopedUserRoleResource

Creates a scoped user role.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Create a ScopedUserRoleResource
    api_response = api_instance.create_scoped_user_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->create_scoped_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scoped_user_role_spaces**
> ScopedUserRoleResource create_scoped_user_role_spaces(base_space_id, body=body)

Create a ScopedUserRoleResource

Creates a scoped user role.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
body = swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Create a ScopedUserRoleResource
    api_response = api_instance.create_scoped_user_role_spaces(base_space_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->create_scoped_user_role_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **body** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scoped_user_role**
> delete_scoped_user_role(id)

Delete a ScopedUserRoleResource by ID

Deletes an existing scoped user role.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ScopedUserRoleResource to delete

try:
    # Delete a ScopedUserRoleResource by ID
    api_instance.delete_scoped_user_role(id)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->delete_scoped_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ScopedUserRoleResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scoped_user_role_spaces**
> delete_scoped_user_role_spaces(base_space_id, id)

Delete a ScopedUserRoleResource by ID

Deletes an existing scoped user role.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ScopedUserRoleResource to delete

try:
    # Delete a ScopedUserRoleResource by ID
    api_instance.delete_scoped_user_role_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->delete_scoped_user_role_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ScopedUserRoleResource to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_scoped_user_role**
> ResourceCollectionScopedUserRoleResource get_list_scoped_user_role()



Lists the name and ID of all of the scoped user roles in the supplied Octopus Deploy Space. The results will be sorted by name.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_list_scoped_user_role()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->get_list_scoped_user_role: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceCollectionScopedUserRoleResource**](ResourceCollectionScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_scoped_user_role_spaces**
> ResourceCollectionScopedUserRoleResource get_list_scoped_user_role_spaces(base_space_id)



Lists the name and ID of all of the scoped user roles in the supplied Octopus Deploy Space. The results will be sorted by name.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.get_list_scoped_user_role_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->get_list_scoped_user_role_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**ResourceCollectionScopedUserRoleResource**](ResourceCollectionScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scoped_user_role_by_id**
> ScopedUserRoleResource get_scoped_user_role_by_id(id)

Get a ScopedUserRoleResource by ID

Gets a scoped user role by ID.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ScopedUserRoleResource to load

try:
    # Get a ScopedUserRoleResource by ID
    api_response = api_instance.get_scoped_user_role_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->get_scoped_user_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ScopedUserRoleResource to load | 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scoped_user_role_by_id_spaces**
> ScopedUserRoleResource get_scoped_user_role_by_id_spaces(base_space_id, id)

Get a ScopedUserRoleResource by ID

Gets a scoped user role by ID.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ScopedUserRoleResource to load

try:
    # Get a ScopedUserRoleResource by ID
    api_response = api_instance.get_scoped_user_role_by_id_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->get_scoped_user_role_by_id_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ScopedUserRoleResource to load | 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scoped_user_role**
> ScopedUserRoleResource update_scoped_user_role(id, body=body)

Modify a ScopedUserRoleResource by ID

Modifies an existing scoped user role.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ScopedUserRoleResource to modify
body = swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Modify a ScopedUserRoleResource by ID
    api_response = api_instance.update_scoped_user_role(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->update_scoped_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ScopedUserRoleResource to modify | 
 **body** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scoped_user_role_spaces**
> ScopedUserRoleResource update_scoped_user_role_spaces(base_space_id, id, body=body)

Modify a ScopedUserRoleResource by ID

Modifies an existing scoped user role.

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
api_instance = swagger_client.ScopedUserRoleApi(swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ScopedUserRoleResource to modify
body = swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Modify a ScopedUserRoleResource by ID
    api_response = api_instance.update_scoped_user_role_spaces(base_space_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->update_scoped_user_role_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ScopedUserRoleResource to modify | 
 **body** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

