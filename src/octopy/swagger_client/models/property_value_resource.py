# coding: utf-8

"""
    Octopus Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2019.13.4+Branch.tags-2019.13.4.Sha.0d7b19b0ef3b9f74ec58e5c86ae6af95165ef70e
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PropertyValueResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_sensitive': 'bool',
        'value': 'str',
        'sensitive_value': 'SensitiveValue'
    }

    attribute_map = {
        'is_sensitive': 'IsSensitive',
        'value': 'Value',
        'sensitive_value': 'SensitiveValue'
    }

    def __init__(self, is_sensitive=None, value=None, sensitive_value=None):  # noqa: E501
        """PropertyValueResource - a model defined in Swagger"""  # noqa: E501
        self._is_sensitive = None
        self._value = None
        self._sensitive_value = None
        self.discriminator = None
        if is_sensitive is not None:
            self.is_sensitive = is_sensitive
        if value is not None:
            self.value = value
        if sensitive_value is not None:
            self.sensitive_value = sensitive_value

    @property
    def is_sensitive(self):
        """Gets the is_sensitive of this PropertyValueResource.  # noqa: E501


        :return: The is_sensitive of this PropertyValueResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """Sets the is_sensitive of this PropertyValueResource.


        :param is_sensitive: The is_sensitive of this PropertyValueResource.  # noqa: E501
        :type: bool
        """

        self._is_sensitive = is_sensitive

    @property
    def value(self):
        """Gets the value of this PropertyValueResource.  # noqa: E501


        :return: The value of this PropertyValueResource.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyValueResource.


        :param value: The value of this PropertyValueResource.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def sensitive_value(self):
        """Gets the sensitive_value of this PropertyValueResource.  # noqa: E501


        :return: The sensitive_value of this PropertyValueResource.  # noqa: E501
        :rtype: SensitiveValue
        """
        return self._sensitive_value

    @sensitive_value.setter
    def sensitive_value(self, sensitive_value):
        """Sets the sensitive_value of this PropertyValueResource.


        :param sensitive_value: The sensitive_value of this PropertyValueResource.  # noqa: E501
        :type: SensitiveValue
        """

        self._sensitive_value = sensitive_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PropertyValueResource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PropertyValueResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
