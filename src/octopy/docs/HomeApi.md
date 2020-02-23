# swagger_client.HomeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_home**](HomeApi.md#get_home) | **GET** /api | 

# **get_home**
> RootResource get_home()



Returns a document describing the current Octopus Server and links to other parts of the API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomeApi()

try:
    api_response = api_instance.get_home()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->get_home: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RootResource**](RootResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

