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


class InterruptionResource(object):
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
        'space_id': 'str',
        'title': 'str',
        'created': 'datetime',
        'is_pending': 'bool',
        'form': 'Form',
        'related_document_ids': 'list[str]',
        'responsible_team_ids': 'list[str]',
        'responsible_user_id': 'str',
        'can_take_responsibility': 'bool',
        'has_responsibility': 'bool',
        'task_id': 'str',
        'correlation_id': 'str',
        'is_linked_to_other_interruption': 'bool',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'space_id': 'SpaceId',
        'title': 'Title',
        'created': 'Created',
        'is_pending': 'IsPending',
        'form': 'Form',
        'related_document_ids': 'RelatedDocumentIds',
        'responsible_team_ids': 'ResponsibleTeamIds',
        'responsible_user_id': 'ResponsibleUserId',
        'can_take_responsibility': 'CanTakeResponsibility',
        'has_responsibility': 'HasResponsibility',
        'task_id': 'TaskId',
        'correlation_id': 'CorrelationId',
        'is_linked_to_other_interruption': 'IsLinkedToOtherInterruption',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, space_id=None, title=None, created=None, is_pending=None, form=None, related_document_ids=None, responsible_team_ids=None, responsible_user_id=None, can_take_responsibility=None, has_responsibility=None, task_id=None, correlation_id=None, is_linked_to_other_interruption=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """InterruptionResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._space_id = None
        self._title = None
        self._created = None
        self._is_pending = None
        self._form = None
        self._related_document_ids = None
        self._responsible_team_ids = None
        self._responsible_user_id = None
        self._can_take_responsibility = None
        self._has_responsibility = None
        self._task_id = None
        self._correlation_id = None
        self._is_linked_to_other_interruption = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if space_id is not None:
            self.space_id = space_id
        if title is not None:
            self.title = title
        if created is not None:
            self.created = created
        if is_pending is not None:
            self.is_pending = is_pending
        if form is not None:
            self.form = form
        if related_document_ids is not None:
            self.related_document_ids = related_document_ids
        if responsible_team_ids is not None:
            self.responsible_team_ids = responsible_team_ids
        if responsible_user_id is not None:
            self.responsible_user_id = responsible_user_id
        if can_take_responsibility is not None:
            self.can_take_responsibility = can_take_responsibility
        if has_responsibility is not None:
            self.has_responsibility = has_responsibility
        if task_id is not None:
            self.task_id = task_id
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if is_linked_to_other_interruption is not None:
            self.is_linked_to_other_interruption = is_linked_to_other_interruption
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this InterruptionResource.  # noqa: E501


        :return: The id of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterruptionResource.


        :param id: The id of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def space_id(self):
        """Gets the space_id of this InterruptionResource.  # noqa: E501


        :return: The space_id of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this InterruptionResource.


        :param space_id: The space_id of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def title(self):
        """Gets the title of this InterruptionResource.  # noqa: E501


        :return: The title of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InterruptionResource.


        :param title: The title of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def created(self):
        """Gets the created of this InterruptionResource.  # noqa: E501


        :return: The created of this InterruptionResource.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InterruptionResource.


        :param created: The created of this InterruptionResource.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def is_pending(self):
        """Gets the is_pending of this InterruptionResource.  # noqa: E501


        :return: The is_pending of this InterruptionResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_pending

    @is_pending.setter
    def is_pending(self, is_pending):
        """Sets the is_pending of this InterruptionResource.


        :param is_pending: The is_pending of this InterruptionResource.  # noqa: E501
        :type: bool
        """

        self._is_pending = is_pending

    @property
    def form(self):
        """Gets the form of this InterruptionResource.  # noqa: E501


        :return: The form of this InterruptionResource.  # noqa: E501
        :rtype: Form
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this InterruptionResource.


        :param form: The form of this InterruptionResource.  # noqa: E501
        :type: Form
        """

        self._form = form

    @property
    def related_document_ids(self):
        """Gets the related_document_ids of this InterruptionResource.  # noqa: E501


        :return: The related_document_ids of this InterruptionResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_document_ids

    @related_document_ids.setter
    def related_document_ids(self, related_document_ids):
        """Sets the related_document_ids of this InterruptionResource.


        :param related_document_ids: The related_document_ids of this InterruptionResource.  # noqa: E501
        :type: list[str]
        """

        self._related_document_ids = related_document_ids

    @property
    def responsible_team_ids(self):
        """Gets the responsible_team_ids of this InterruptionResource.  # noqa: E501


        :return: The responsible_team_ids of this InterruptionResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._responsible_team_ids

    @responsible_team_ids.setter
    def responsible_team_ids(self, responsible_team_ids):
        """Sets the responsible_team_ids of this InterruptionResource.


        :param responsible_team_ids: The responsible_team_ids of this InterruptionResource.  # noqa: E501
        :type: list[str]
        """

        self._responsible_team_ids = responsible_team_ids

    @property
    def responsible_user_id(self):
        """Gets the responsible_user_id of this InterruptionResource.  # noqa: E501


        :return: The responsible_user_id of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._responsible_user_id

    @responsible_user_id.setter
    def responsible_user_id(self, responsible_user_id):
        """Sets the responsible_user_id of this InterruptionResource.


        :param responsible_user_id: The responsible_user_id of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._responsible_user_id = responsible_user_id

    @property
    def can_take_responsibility(self):
        """Gets the can_take_responsibility of this InterruptionResource.  # noqa: E501


        :return: The can_take_responsibility of this InterruptionResource.  # noqa: E501
        :rtype: bool
        """
        return self._can_take_responsibility

    @can_take_responsibility.setter
    def can_take_responsibility(self, can_take_responsibility):
        """Sets the can_take_responsibility of this InterruptionResource.


        :param can_take_responsibility: The can_take_responsibility of this InterruptionResource.  # noqa: E501
        :type: bool
        """

        self._can_take_responsibility = can_take_responsibility

    @property
    def has_responsibility(self):
        """Gets the has_responsibility of this InterruptionResource.  # noqa: E501


        :return: The has_responsibility of this InterruptionResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_responsibility

    @has_responsibility.setter
    def has_responsibility(self, has_responsibility):
        """Sets the has_responsibility of this InterruptionResource.


        :param has_responsibility: The has_responsibility of this InterruptionResource.  # noqa: E501
        :type: bool
        """

        self._has_responsibility = has_responsibility

    @property
    def task_id(self):
        """Gets the task_id of this InterruptionResource.  # noqa: E501


        :return: The task_id of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this InterruptionResource.


        :param task_id: The task_id of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def correlation_id(self):
        """Gets the correlation_id of this InterruptionResource.  # noqa: E501


        :return: The correlation_id of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this InterruptionResource.


        :param correlation_id: The correlation_id of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def is_linked_to_other_interruption(self):
        """Gets the is_linked_to_other_interruption of this InterruptionResource.  # noqa: E501


        :return: The is_linked_to_other_interruption of this InterruptionResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_linked_to_other_interruption

    @is_linked_to_other_interruption.setter
    def is_linked_to_other_interruption(self, is_linked_to_other_interruption):
        """Sets the is_linked_to_other_interruption of this InterruptionResource.


        :param is_linked_to_other_interruption: The is_linked_to_other_interruption of this InterruptionResource.  # noqa: E501
        :type: bool
        """

        self._is_linked_to_other_interruption = is_linked_to_other_interruption

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this InterruptionResource.  # noqa: E501


        :return: The last_modified_on of this InterruptionResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this InterruptionResource.


        :param last_modified_on: The last_modified_on of this InterruptionResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this InterruptionResource.  # noqa: E501


        :return: The last_modified_by of this InterruptionResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this InterruptionResource.


        :param last_modified_by: The last_modified_by of this InterruptionResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this InterruptionResource.  # noqa: E501


        :return: The links of this InterruptionResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InterruptionResource.


        :param links: The links of this InterruptionResource.  # noqa: E501
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
        if issubclass(InterruptionResource, dict):
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
        if not isinstance(other, InterruptionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
