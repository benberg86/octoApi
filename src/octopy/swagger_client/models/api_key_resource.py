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


class ApiKeyResource(object):
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
        'purpose': 'str',
        'user_id': 'str',
        'api_key': 'str',
        'created': 'datetime',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'purpose': 'Purpose',
        'user_id': 'UserId',
        'api_key': 'ApiKey',
        'created': 'Created',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, purpose=None, user_id=None, api_key=None, created=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """ApiKeyResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._purpose = None
        self._user_id = None
        self._api_key = None
        self._created = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if purpose is not None:
            self.purpose = purpose
        if user_id is not None:
            self.user_id = user_id
        if api_key is not None:
            self.api_key = api_key
        if created is not None:
            self.created = created
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this ApiKeyResource.  # noqa: E501


        :return: The id of this ApiKeyResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiKeyResource.


        :param id: The id of this ApiKeyResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def purpose(self):
        """Gets the purpose of this ApiKeyResource.  # noqa: E501


        :return: The purpose of this ApiKeyResource.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this ApiKeyResource.


        :param purpose: The purpose of this ApiKeyResource.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def user_id(self):
        """Gets the user_id of this ApiKeyResource.  # noqa: E501


        :return: The user_id of this ApiKeyResource.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ApiKeyResource.


        :param user_id: The user_id of this ApiKeyResource.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def api_key(self):
        """Gets the api_key of this ApiKeyResource.  # noqa: E501


        :return: The api_key of this ApiKeyResource.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ApiKeyResource.


        :param api_key: The api_key of this ApiKeyResource.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def created(self):
        """Gets the created of this ApiKeyResource.  # noqa: E501


        :return: The created of this ApiKeyResource.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApiKeyResource.


        :param created: The created of this ApiKeyResource.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this ApiKeyResource.  # noqa: E501


        :return: The last_modified_on of this ApiKeyResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this ApiKeyResource.


        :param last_modified_on: The last_modified_on of this ApiKeyResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ApiKeyResource.  # noqa: E501


        :return: The last_modified_by of this ApiKeyResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ApiKeyResource.


        :param last_modified_by: The last_modified_by of this ApiKeyResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this ApiKeyResource.  # noqa: E501


        :return: The links of this ApiKeyResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiKeyResource.


        :param links: The links of this ApiKeyResource.  # noqa: E501
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
        if issubclass(ApiKeyResource, dict):
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
        if not isinstance(other, ApiKeyResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
