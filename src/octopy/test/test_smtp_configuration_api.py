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
from api.smtp_configuration_api import SmtpConfigurationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSmtpConfigurationApi(unittest.TestCase):
    """SmtpConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = api.smtp_configuration_api.SmtpConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_smtp_configuration(self):
        """Test case for get_smtp_configuration

        """
        pass

    def test_get_smtp_is_configured(self):
        """Test case for get_smtp_is_configured

        """
        pass

    def test_update_smtp_configuration(self):
        """Test case for update_smtp_configuration

        """
        pass


if __name__ == '__main__':
    unittest.main()
