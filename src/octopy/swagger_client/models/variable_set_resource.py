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


class VariableSetResource(object):
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
        'owner_id': 'str',
        'version': 'int',
        'variables': 'list[VariableResource]',
        'scope_values': 'VariableScopeValues',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'owner_id': 'OwnerId',
        'version': 'Version',
        'variables': 'Variables',
        'scope_values': 'ScopeValues',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, owner_id=None, version=None, variables=None, scope_values=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """VariableSetResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._owner_id = None
        self._version = None
        self._variables = None
        self._scope_values = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if version is not None:
            self.version = version
        if variables is not None:
            self.variables = variables
        if scope_values is not None:
            self.scope_values = scope_values
        if space_id is not None:
            self.space_id = space_id
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this VariableSetResource.  # noqa: E501


        :return: The id of this VariableSetResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariableSetResource.


        :param id: The id of this VariableSetResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this VariableSetResource.  # noqa: E501


        :return: The owner_id of this VariableSetResource.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this VariableSetResource.


        :param owner_id: The owner_id of this VariableSetResource.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def version(self):
        """Gets the version of this VariableSetResource.  # noqa: E501


        :return: The version of this VariableSetResource.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VariableSetResource.


        :param version: The version of this VariableSetResource.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def variables(self):
        """Gets the variables of this VariableSetResource.  # noqa: E501


        :return: The variables of this VariableSetResource.  # noqa: E501
        :rtype: list[VariableResource]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this VariableSetResource.


        :param variables: The variables of this VariableSetResource.  # noqa: E501
        :type: list[VariableResource]
        """

        self._variables = variables

    @property
    def scope_values(self):
        """Gets the scope_values of this VariableSetResource.  # noqa: E501


        :return: The scope_values of this VariableSetResource.  # noqa: E501
        :rtype: VariableScopeValues
        """
        return self._scope_values

    @scope_values.setter
    def scope_values(self, scope_values):
        """Sets the scope_values of this VariableSetResource.


        :param scope_values: The scope_values of this VariableSetResource.  # noqa: E501
        :type: VariableScopeValues
        """

        self._scope_values = scope_values

    @property
    def space_id(self):
        """Gets the space_id of this VariableSetResource.  # noqa: E501


        :return: The space_id of this VariableSetResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this VariableSetResource.


        :param space_id: The space_id of this VariableSetResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this VariableSetResource.  # noqa: E501


        :return: The last_modified_on of this VariableSetResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this VariableSetResource.


        :param last_modified_on: The last_modified_on of this VariableSetResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this VariableSetResource.  # noqa: E501


        :return: The last_modified_by of this VariableSetResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this VariableSetResource.


        :param last_modified_by: The last_modified_by of this VariableSetResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this VariableSetResource.  # noqa: E501


        :return: The links of this VariableSetResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VariableSetResource.


        :param links: The links of this VariableSetResource.  # noqa: E501
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
        if issubclass(VariableSetResource, dict):
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
        if not isinstance(other, VariableSetResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
