# swagger_client.ExternalSecurityGroupsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_providers_that_support_external_security_groups**](ExternalSecurityGroupsApi.md#get_list_providers_that_support_external_security_groups) | **GET** /api/externalsecuritygroupproviders | 

# **get_list_providers_that_support_external_security_groups**
> list[AuthenticationProviderThatSupportsGroups] get_list_providers_that_support_external_security_groups()



Lists the authentication providers that support external group lookups.

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
api_instance = swagger_client.ExternalSecurityGroupsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_list_providers_that_support_external_security_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalSecurityGroupsApi->get_list_providers_that_support_external_security_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AuthenticationProviderThatSupportsGroups]**](AuthenticationProviderThatSupportsGroups.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

