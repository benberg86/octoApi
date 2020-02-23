# swagger_client.PerformanceConfigurationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_performance_configuration**](PerformanceConfigurationApi.md#get_performance_configuration) | **GET** /api/performanceconfiguration | 
[**update_performance_configuration**](PerformanceConfigurationApi.md#update_performance_configuration) | **PUT** /api/performanceconfiguration | 

# **get_performance_configuration**
> PerformanceConfigurationResource get_performance_configuration()



Get performance settings for the Octopus Server

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
api_instance = swagger_client.PerformanceConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_performance_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceConfigurationApi->get_performance_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PerformanceConfigurationResource**](PerformanceConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_configuration**
> PerformanceConfigurationResource update_performance_configuration()



Updates the performance settings for the Octopus Server

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
api_instance = swagger_client.PerformanceConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.update_performance_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceConfigurationApi->update_performance_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PerformanceConfigurationResource**](PerformanceConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

