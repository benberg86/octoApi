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


class UserTeamsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user_get_teams(self, id, **kwargs):  # noqa: E501
        """get_user_get_teams  # noqa: E501

        Gets a list of teams (id and name only) for the specified user, including any from external auth-provider security groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_get_teams(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: list[ProjectedTeamReferenceDataItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_get_teams_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_get_teams_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_user_get_teams_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_user_get_teams  # noqa: E501

        Gets a list of teams (id and name only) for the specified user, including any from external auth-provider security groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_get_teams_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the resource (required)
        :return: list[ProjectedTeamReferenceDataItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_get_teams" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_user_get_teams`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/{id}/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectedTeamReferenceDataItem]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_get_teams_spaces(self, base_space_id, id, **kwargs):  # noqa: E501
        """get_user_get_teams_spaces  # noqa: E501

        Gets a list of teams (id and name only) for the specified user, including any from external auth-provider security groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_get_teams_spaces(base_space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str base_space_id: ID of the space (required)
        :param str id: ID of the resource (required)
        :return: list[ProjectedTeamReferenceDataItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_get_teams_spaces_with_http_info(base_space_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_get_teams_spaces_with_http_info(base_space_id, id, **kwargs)  # noqa: E501
            return data

    def get_user_get_teams_spaces_with_http_info(self, base_space_id, id, **kwargs):  # noqa: E501
        """get_user_get_teams_spaces  # noqa: E501

        Gets a list of teams (id and name only) for the specified user, including any from external auth-provider security groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_get_teams_spaces_with_http_info(base_space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str base_space_id: ID of the space (required)
        :param str id: ID of the resource (required)
        :return: list[ProjectedTeamReferenceDataItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['base_space_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_get_teams_spaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'base_space_id' is set
        if ('base_space_id' not in params or
                params['base_space_id'] is None):
            raise ValueError("Missing the required parameter `base_space_id` when calling `get_user_get_teams_spaces`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_user_get_teams_spaces`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'base_space_id' in params:
            path_params['baseSpaceId'] = params['base_space_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQuery', 'NugetApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/{baseSpaceId}/users/{id}/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectedTeamReferenceDataItem]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
