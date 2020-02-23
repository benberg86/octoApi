# swagger_client.DynamicExtensionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dynamic_extensions**](DynamicExtensionsApi.md#get_dynamic_extensions) | **GET** /api/dynamic-extensions/settings | 

# **get_dynamic_extensions**
> DynamicExtensionsSettingsResource get_dynamic_extensions()



Retrieves the current dynamic extensions settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicExtensionsApi()

try:
    api_response = api_instance.get_dynamic_extensions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicExtensionsApi->get_dynamic_extensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DynamicExtensionsSettingsResource**](DynamicExtensionsSettingsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

