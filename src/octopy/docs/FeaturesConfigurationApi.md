# swagger_client.FeaturesConfigurationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_features_configuration**](FeaturesConfigurationApi.md#get_features_configuration) | **GET** /api/featuresconfiguration | 
[**update_features_configuration**](FeaturesConfigurationApi.md#update_features_configuration) | **PUT** /api/featuresconfiguration | 

# **get_features_configuration**
> FeaturesConfigurationResource get_features_configuration()



Gets information about the features configuration in use by the Octopus Server

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
api_instance = swagger_client.FeaturesConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_features_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesConfigurationApi->get_features_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeaturesConfigurationResource**](FeaturesConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_features_configuration**
> FeaturesConfigurationResource update_features_configuration()



Updates the features configuration used by the Octopus Server

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
api_instance = swagger_client.FeaturesConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.update_features_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesConfigurationApi->update_features_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeaturesConfigurationResource**](FeaturesConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

