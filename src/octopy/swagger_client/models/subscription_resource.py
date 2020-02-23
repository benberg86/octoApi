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


class SubscriptionResource(object):
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
        'type': 'str',
        'is_disabled': 'bool',
        'event_notification_subscription': 'EventNotificationSubscription',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'type': 'Type',
        'is_disabled': 'IsDisabled',
        'event_notification_subscription': 'EventNotificationSubscription',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, type=None, is_disabled=None, event_notification_subscription=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """SubscriptionResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._is_disabled = None
        self._event_notification_subscription = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if event_notification_subscription is not None:
            self.event_notification_subscription = event_notification_subscription
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
        """Gets the id of this SubscriptionResource.  # noqa: E501


        :return: The id of this SubscriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionResource.


        :param id: The id of this SubscriptionResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionResource.  # noqa: E501


        :return: The name of this SubscriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionResource.


        :param name: The name of this SubscriptionResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this SubscriptionResource.  # noqa: E501


        :return: The type of this SubscriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionResource.


        :param type: The type of this SubscriptionResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Event"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def is_disabled(self):
        """Gets the is_disabled of this SubscriptionResource.  # noqa: E501


        :return: The is_disabled of this SubscriptionResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this SubscriptionResource.


        :param is_disabled: The is_disabled of this SubscriptionResource.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def event_notification_subscription(self):
        """Gets the event_notification_subscription of this SubscriptionResource.  # noqa: E501


        :return: The event_notification_subscription of this SubscriptionResource.  # noqa: E501
        :rtype: EventNotificationSubscription
        """
        return self._event_notification_subscription

    @event_notification_subscription.setter
    def event_notification_subscription(self, event_notification_subscription):
        """Sets the event_notification_subscription of this SubscriptionResource.


        :param event_notification_subscription: The event_notification_subscription of this SubscriptionResource.  # noqa: E501
        :type: EventNotificationSubscription
        """

        self._event_notification_subscription = event_notification_subscription

    @property
    def space_id(self):
        """Gets the space_id of this SubscriptionResource.  # noqa: E501


        :return: The space_id of this SubscriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this SubscriptionResource.


        :param space_id: The space_id of this SubscriptionResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this SubscriptionResource.  # noqa: E501


        :return: The last_modified_on of this SubscriptionResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this SubscriptionResource.


        :param last_modified_on: The last_modified_on of this SubscriptionResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this SubscriptionResource.  # noqa: E501


        :return: The last_modified_by of this SubscriptionResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this SubscriptionResource.


        :param last_modified_by: The last_modified_by of this SubscriptionResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this SubscriptionResource.  # noqa: E501


        :return: The links of this SubscriptionResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SubscriptionResource.


        :param links: The links of this SubscriptionResource.  # noqa: E501
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
        if issubclass(SubscriptionResource, dict):
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
        if not isinstance(other, SubscriptionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
