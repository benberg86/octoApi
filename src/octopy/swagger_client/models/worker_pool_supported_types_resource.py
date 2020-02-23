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


class WorkerPoolSupportedTypesResource(object):
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
        'supported_pool_types': 'list[str]',
        'id': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'supported_pool_types': 'SupportedPoolTypes',
        'id': 'Id',
        'links': 'Links'
    }

    def __init__(self, supported_pool_types=None, id=None, links=None):  # noqa: E501
        """WorkerPoolSupportedTypesResource - a model defined in Swagger"""  # noqa: E501
        self._supported_pool_types = None
        self._id = None
        self._links = None
        self.discriminator = None
        if supported_pool_types is not None:
            self.supported_pool_types = supported_pool_types
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links

    @property
    def supported_pool_types(self):
        """Gets the supported_pool_types of this WorkerPoolSupportedTypesResource.  # noqa: E501


        :return: The supported_pool_types of this WorkerPoolSupportedTypesResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_pool_types

    @supported_pool_types.setter
    def supported_pool_types(self, supported_pool_types):
        """Sets the supported_pool_types of this WorkerPoolSupportedTypesResource.


        :param supported_pool_types: The supported_pool_types of this WorkerPoolSupportedTypesResource.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["StaticWorkerPool", "DynamicWorkerPool"]  # noqa: E501
        if not set(supported_pool_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `supported_pool_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(supported_pool_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_pool_types = supported_pool_types

    @property
    def id(self):
        """Gets the id of this WorkerPoolSupportedTypesResource.  # noqa: E501


        :return: The id of this WorkerPoolSupportedTypesResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkerPoolSupportedTypesResource.


        :param id: The id of this WorkerPoolSupportedTypesResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this WorkerPoolSupportedTypesResource.  # noqa: E501


        :return: The links of this WorkerPoolSupportedTypesResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this WorkerPoolSupportedTypesResource.


        :param links: The links of this WorkerPoolSupportedTypesResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

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
        if issubclass(WorkerPoolSupportedTypesResource, dict):
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
        if not isinstance(other, WorkerPoolSupportedTypesResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
