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


class ExtensionsInfoResource(object):
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
        'id': 'str',
        'name': 'str',
        'assembly_name': 'str',
        'author': 'str',
        'version': 'str',
        'is_custom': 'bool',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'assembly_name': 'AssemblyName',
        'author': 'Author',
        'version': 'Version',
        'is_custom': 'IsCustom',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, assembly_name=None, author=None, version=None, is_custom=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """ExtensionsInfoResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._assembly_name = None
        self._author = None
        self._version = None
        self._is_custom = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if assembly_name is not None:
            self.assembly_name = assembly_name
        if author is not None:
            self.author = author
        if version is not None:
            self.version = version
        if is_custom is not None:
            self.is_custom = is_custom
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this ExtensionsInfoResource.  # noqa: E501


        :return: The id of this ExtensionsInfoResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtensionsInfoResource.


        :param id: The id of this ExtensionsInfoResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExtensionsInfoResource.  # noqa: E501


        :return: The name of this ExtensionsInfoResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtensionsInfoResource.


        :param name: The name of this ExtensionsInfoResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def assembly_name(self):
        """Gets the assembly_name of this ExtensionsInfoResource.  # noqa: E501


        :return: The assembly_name of this ExtensionsInfoResource.  # noqa: E501
        :rtype: str
        """
        return self._assembly_name

    @assembly_name.setter
    def assembly_name(self, assembly_name):
        """Sets the assembly_name of this ExtensionsInfoResource.


        :param assembly_name: The assembly_name of this ExtensionsInfoResource.  # noqa: E501
        :type: str
        """

        self._assembly_name = assembly_name

    @property
    def author(self):
        """Gets the author of this ExtensionsInfoResource.  # noqa: E501


        :return: The author of this ExtensionsInfoResource.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ExtensionsInfoResource.


        :param author: The author of this ExtensionsInfoResource.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def version(self):
        """Gets the version of this ExtensionsInfoResource.  # noqa: E501


        :return: The version of this ExtensionsInfoResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExtensionsInfoResource.


        :param version: The version of this ExtensionsInfoResource.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def is_custom(self):
        """Gets the is_custom of this ExtensionsInfoResource.  # noqa: E501


        :return: The is_custom of this ExtensionsInfoResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom

    @is_custom.setter
    def is_custom(self, is_custom):
        """Sets the is_custom of this ExtensionsInfoResource.


        :param is_custom: The is_custom of this ExtensionsInfoResource.  # noqa: E501
        :type: bool
        """

        self._is_custom = is_custom

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this ExtensionsInfoResource.  # noqa: E501


        :return: The last_modified_on of this ExtensionsInfoResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this ExtensionsInfoResource.


        :param last_modified_on: The last_modified_on of this ExtensionsInfoResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ExtensionsInfoResource.  # noqa: E501


        :return: The last_modified_by of this ExtensionsInfoResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ExtensionsInfoResource.


        :param last_modified_by: The last_modified_by of this ExtensionsInfoResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this ExtensionsInfoResource.  # noqa: E501


        :return: The links of this ExtensionsInfoResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ExtensionsInfoResource.


        :param links: The links of this ExtensionsInfoResource.  # noqa: E501
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
        if issubclass(ExtensionsInfoResource, dict):
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
        if not isinstance(other, ExtensionsInfoResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
