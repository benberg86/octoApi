# coding: utf-8

"""
    Octopus Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2019.13.4+Branch.tags-2019.13.4.Sha.0d7b19b0ef3b9f74ec58e5c86ae6af95165ef70e
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LetsEncryptApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_lets_encrypt_configuration(self, **kwargs):  # noqa: E501
        """get_lets_encrypt_configuration  # noqa: E501

        Returns the current Let's Encrypt configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lets_encrypt_configuration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_lets_encrypt_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_lets_encrypt_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_lets_encrypt_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """get_lets_encrypt_configuration  # noqa: E501

        Returns the current Let's Encrypt configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lets_encrypt_configuration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lets_encrypt_configuration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            'api/letsencryptconfiguration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_lets_encrypt_http_challenge(self, token, **kwargs):  # noqa: E501
        """get_lets_encrypt_http_challenge  # noqa: E501

        Returns the computed HTTP challenge for a given token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lets_encrypt_http_challenge(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: LetsEncrypt response token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_lets_encrypt_http_challenge_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_lets_encrypt_http_challenge_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def get_lets_encrypt_http_challenge_with_http_info(self, token, **kwargs):  # noqa: E501
        """get_lets_encrypt_http_challenge  # noqa: E501

        Returns the computed HTTP challenge for a given token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lets_encrypt_http_challenge_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: LetsEncrypt response token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lets_encrypt_http_challenge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_lets_encrypt_http_challenge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/.well-known/acme-challenge//{token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_lets_encrypt_configuration(self, **kwargs):  # noqa: E501
        """update_lets_encrypt_configuration  # noqa: E501

        Updates the Let's Encrypt configuration used by the Octopus Server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_lets_encrypt_configuration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_lets_encrypt_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_lets_encrypt_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_lets_encrypt_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """update_lets_encrypt_configuration  # noqa: E501

        Updates the Let's Encrypt configuration used by the Octopus Server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_lets_encrypt_configuration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_lets_encrypt_configuration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            'api/letsencryptconfiguration', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
