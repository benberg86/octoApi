# swagger_client.SpaceHomeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_space_home**](SpaceHomeApi.md#get_space_home) | **GET** /api/(?&lt;spaceId&gt;Spaces-\d+) | 

# **get_space_home**
> SpaceRootResource get_space_home(space_id)



Returns a document describing the specified Space and links to other parts of the API that apply to the Space.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceHomeApi()
space_id = 'space_id_example' # str | ID of the space

try:
    api_response = api_instance.get_space_home(space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceHomeApi->get_space_home: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| ID of the space | 

### Return type

[**SpaceRootResource**](SpaceRootResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

