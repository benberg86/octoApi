# swagger_client.AuthenticationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_login_initiated**](AuthenticationApi.md#create_login_initiated) | **POST** /api/authentication/checklogininitiated | 
[**get_authentication**](AuthenticationApi.md#get_authentication) | **GET** /api/authentication | 

# **create_login_initiated**
> LoginInitiatedResource create_login_initiated()



Given a url query string, determines whether an external server (.e.g Okta) has initiated login and if so the provider's name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    api_response = api_instance.create_login_initiated()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_login_initiated: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginInitiatedResource**](LoginInitiatedResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication**
> AuthenticationResource get_authentication()



Provides the details of the enabled authentication providers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    api_response = api_instance.get_authentication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_authentication: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationResource**](AuthenticationResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

