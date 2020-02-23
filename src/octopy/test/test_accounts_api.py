# coding: utf-8

"""
    Octopus Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2019.13.4+Branch.tags-2019.13.4.Sha.0d7b19b0ef3b9f74ec58e5c86ae6af95165ef70e
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.accounts_api import AccountsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_account(self):
        """Test case for create_account

        Create a AccountResource  # noqa: E501
        """
        pass

    def test_create_account_spaces(self):
        """Test case for create_account_spaces

        Create a AccountResource  # noqa: E501
        """
        pass

    def test_delete_account(self):
        """Test case for delete_account

        Delete a AccountResource by ID  # noqa: E501
        """
        pass

    def test_delete_account_spaces(self):
        """Test case for delete_account_spaces

        Delete a AccountResource by ID  # noqa: E501
        """
        pass

    def test_get_account_by_id(self):
        """Test case for get_account_by_id

        Get a AccountResource by ID  # noqa: E501
        """
        pass

    def test_get_account_by_id_spaces(self):
        """Test case for get_account_by_id_spaces

        Get a AccountResource by ID  # noqa: E501
        """
        pass

    def test_get_account_public_key_download(self):
        """Test case for get_account_public_key_download

        """
        pass

    def test_get_account_public_key_download_spaces(self):
        """Test case for get_account_public_key_download_spaces

        """
        pass

    def test_get_account_usage_list(self):
        """Test case for get_account_usage_list

        """
        pass

    def test_get_account_usage_list_spaces(self):
        """Test case for get_account_usage_list_spaces

        """
        pass

    def test_get_azure_environments(self):
        """Test case for get_azure_environments

        """
        pass

    def test_get_azure_environments_spaces(self):
        """Test case for get_azure_environments_spaces

        """
        pass

    def test_get_azure_resource_groups_list(self):
        """Test case for get_azure_resource_groups_list

        """
        pass

    def test_get_azure_resource_groups_list_spaces(self):
        """Test case for get_azure_resource_groups_list_spaces

        """
        pass

    def test_get_azure_storage_accounts_list(self):
        """Test case for get_azure_storage_accounts_list

        """
        pass

    def test_get_azure_storage_accounts_list_spaces(self):
        """Test case for get_azure_storage_accounts_list_spaces

        """
        pass

    def test_get_azure_web_sites_list(self):
        """Test case for get_azure_web_sites_list

        """
        pass

    def test_get_azure_web_sites_list_spaces(self):
        """Test case for get_azure_web_sites_list_spaces

        """
        pass

    def test_get_azure_web_sites_slot_list(self):
        """Test case for get_azure_web_sites_slot_list

        """
        pass

    def test_get_azure_web_sites_slot_list_spaces(self):
        """Test case for get_azure_web_sites_slot_list_spaces

        """
        pass

    def test_index_accounts(self):
        """Test case for index_accounts

        Get a list of AccountResources  # noqa: E501
        """
        pass

    def test_index_accounts_spaces(self):
        """Test case for index_accounts_spaces

        Get a list of AccountResources  # noqa: E501
        """
        pass

    def test_list_all_accounts(self):
        """Test case for list_all_accounts

        Get a list of AccountResources  # noqa: E501
        """
        pass

    def test_list_all_accounts_spaces(self):
        """Test case for list_all_accounts_spaces

        Get a list of AccountResources  # noqa: E501
        """
        pass

    def test_update_account(self):
        """Test case for update_account

        Modify a AccountResource by ID  # noqa: E501
        """
        pass

    def test_update_account_spaces(self):
        """Test case for update_account_spaces

        Modify a AccountResource by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
