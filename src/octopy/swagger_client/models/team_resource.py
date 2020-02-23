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


class TeamResource(object):
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
        'member_user_ids': 'list[str]',
        'external_security_groups': 'list[NamedReferenceItem]',
        'can_be_deleted': 'bool',
        'can_be_renamed': 'bool',
        'can_change_roles': 'bool',
        'can_change_members': 'bool',
        'space_id': 'str',
        'description': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'member_user_ids': 'MemberUserIds',
        'external_security_groups': 'ExternalSecurityGroups',
        'can_be_deleted': 'CanBeDeleted',
        'can_be_renamed': 'CanBeRenamed',
        'can_change_roles': 'CanChangeRoles',
        'can_change_members': 'CanChangeMembers',
        'space_id': 'SpaceId',
        'description': 'Description',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, member_user_ids=None, external_security_groups=None, can_be_deleted=None, can_be_renamed=None, can_change_roles=None, can_change_members=None, space_id=None, description=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """TeamResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._member_user_ids = None
        self._external_security_groups = None
        self._can_be_deleted = None
        self._can_be_renamed = None
        self._can_change_roles = None
        self._can_change_members = None
        self._space_id = None
        self._description = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if member_user_ids is not None:
            self.member_user_ids = member_user_ids
        if external_security_groups is not None:
            self.external_security_groups = external_security_groups
        if can_be_deleted is not None:
            self.can_be_deleted = can_be_deleted
        if can_be_renamed is not None:
            self.can_be_renamed = can_be_renamed
        if can_change_roles is not None:
            self.can_change_roles = can_change_roles
        if can_change_members is not None:
            self.can_change_members = can_change_members
        if space_id is not None:
            self.space_id = space_id
        if description is not None:
            self.description = description
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this TeamResource.  # noqa: E501


        :return: The id of this TeamResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TeamResource.


        :param id: The id of this TeamResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TeamResource.  # noqa: E501


        :return: The name of this TeamResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamResource.


        :param name: The name of this TeamResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def member_user_ids(self):
        """Gets the member_user_ids of this TeamResource.  # noqa: E501


        :return: The member_user_ids of this TeamResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_user_ids

    @member_user_ids.setter
    def member_user_ids(self, member_user_ids):
        """Sets the member_user_ids of this TeamResource.


        :param member_user_ids: The member_user_ids of this TeamResource.  # noqa: E501
        :type: list[str]
        """

        self._member_user_ids = member_user_ids

    @property
    def external_security_groups(self):
        """Gets the external_security_groups of this TeamResource.  # noqa: E501


        :return: The external_security_groups of this TeamResource.  # noqa: E501
        :rtype: list[NamedReferenceItem]
        """
        return self._external_security_groups

    @external_security_groups.setter
    def external_security_groups(self, external_security_groups):
        """Sets the external_security_groups of this TeamResource.


        :param external_security_groups: The external_security_groups of this TeamResource.  # noqa: E501
        :type: list[NamedReferenceItem]
        """

        self._external_security_groups = external_security_groups

    @property
    def can_be_deleted(self):
        """Gets the can_be_deleted of this TeamResource.  # noqa: E501


        :return: The can_be_deleted of this TeamResource.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_deleted

    @can_be_deleted.setter
    def can_be_deleted(self, can_be_deleted):
        """Sets the can_be_deleted of this TeamResource.


        :param can_be_deleted: The can_be_deleted of this TeamResource.  # noqa: E501
        :type: bool
        """

        self._can_be_deleted = can_be_deleted

    @property
    def can_be_renamed(self):
        """Gets the can_be_renamed of this TeamResource.  # noqa: E501


        :return: The can_be_renamed of this TeamResource.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_renamed

    @can_be_renamed.setter
    def can_be_renamed(self, can_be_renamed):
        """Sets the can_be_renamed of this TeamResource.


        :param can_be_renamed: The can_be_renamed of this TeamResource.  # noqa: E501
        :type: bool
        """

        self._can_be_renamed = can_be_renamed

    @property
    def can_change_roles(self):
        """Gets the can_change_roles of this TeamResource.  # noqa: E501


        :return: The can_change_roles of this TeamResource.  # noqa: E501
        :rtype: bool
        """
        return self._can_change_roles

    @can_change_roles.setter
    def can_change_roles(self, can_change_roles):
        """Sets the can_change_roles of this TeamResource.


        :param can_change_roles: The can_change_roles of this TeamResource.  # noqa: E501
        :type: bool
        """

        self._can_change_roles = can_change_roles

    @property
    def can_change_members(self):
        """Gets the can_change_members of this TeamResource.  # noqa: E501


        :return: The can_change_members of this TeamResource.  # noqa: E501
        :rtype: bool
        """
        return self._can_change_members

    @can_change_members.setter
    def can_change_members(self, can_change_members):
        """Sets the can_change_members of this TeamResource.


        :param can_change_members: The can_change_members of this TeamResource.  # noqa: E501
        :type: bool
        """

        self._can_change_members = can_change_members

    @property
    def space_id(self):
        """Gets the space_id of this TeamResource.  # noqa: E501


        :return: The space_id of this TeamResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this TeamResource.


        :param space_id: The space_id of this TeamResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def description(self):
        """Gets the description of this TeamResource.  # noqa: E501


        :return: The description of this TeamResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TeamResource.


        :param description: The description of this TeamResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this TeamResource.  # noqa: E501


        :return: The last_modified_on of this TeamResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this TeamResource.


        :param last_modified_on: The last_modified_on of this TeamResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this TeamResource.  # noqa: E501


        :return: The last_modified_by of this TeamResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this TeamResource.


        :param last_modified_by: The last_modified_by of this TeamResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this TeamResource.  # noqa: E501


        :return: The links of this TeamResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TeamResource.


        :param links: The links of this TeamResource.  # noqa: E501
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
        if issubclass(TeamResource, dict):
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
        if not isinstance(other, TeamResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
