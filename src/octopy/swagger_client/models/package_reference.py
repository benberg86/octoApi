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


class PackageReference(object):
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
        'package_id': 'str',
        'feed_id': 'str',
        'acquisition_location': 'str',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'package_id': 'PackageId',
        'feed_id': 'FeedId',
        'acquisition_location': 'AcquisitionLocation',
        'properties': 'Properties'
    }

    def __init__(self, id=None, name=None, package_id=None, feed_id=None, acquisition_location=None, properties=None):  # noqa: E501
        """PackageReference - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._package_id = None
        self._feed_id = None
        self._acquisition_location = None
        self._properties = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if package_id is not None:
            self.package_id = package_id
        if feed_id is not None:
            self.feed_id = feed_id
        if acquisition_location is not None:
            self.acquisition_location = acquisition_location
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this PackageReference.  # noqa: E501


        :return: The id of this PackageReference.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageReference.


        :param id: The id of this PackageReference.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PackageReference.  # noqa: E501


        :return: The name of this PackageReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageReference.


        :param name: The name of this PackageReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def package_id(self):
        """Gets the package_id of this PackageReference.  # noqa: E501


        :return: The package_id of this PackageReference.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this PackageReference.


        :param package_id: The package_id of this PackageReference.  # noqa: E501
        :type: str
        """

        self._package_id = package_id

    @property
    def feed_id(self):
        """Gets the feed_id of this PackageReference.  # noqa: E501


        :return: The feed_id of this PackageReference.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this PackageReference.


        :param feed_id: The feed_id of this PackageReference.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

    @property
    def acquisition_location(self):
        """Gets the acquisition_location of this PackageReference.  # noqa: E501


        :return: The acquisition_location of this PackageReference.  # noqa: E501
        :rtype: str
        """
        return self._acquisition_location

    @acquisition_location.setter
    def acquisition_location(self, acquisition_location):
        """Sets the acquisition_location of this PackageReference.


        :param acquisition_location: The acquisition_location of this PackageReference.  # noqa: E501
        :type: str
        """

        self._acquisition_location = acquisition_location

    @property
    def properties(self):
        """Gets the properties of this PackageReference.  # noqa: E501


        :return: The properties of this PackageReference.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PackageReference.


        :param properties: The properties of this PackageReference.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

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
        if issubclass(PackageReference, dict):
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
        if not isinstance(other, PackageReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
