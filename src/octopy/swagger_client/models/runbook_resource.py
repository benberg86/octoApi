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


class RunbookResource(object):
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
        'description': 'str',
        'runbook_process_id': 'str',
        'published_runbook_snapshot_id': 'str',
        'project_id': 'str',
        'space_id': 'str',
        'multi_tenancy_mode': 'str',
        'connectivity_policy': 'ProjectConnectivityPolicy',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'runbook_process_id': 'RunbookProcessId',
        'published_runbook_snapshot_id': 'PublishedRunbookSnapshotId',
        'project_id': 'ProjectId',
        'space_id': 'SpaceId',
        'multi_tenancy_mode': 'MultiTenancyMode',
        'connectivity_policy': 'ConnectivityPolicy',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, description=None, runbook_process_id=None, published_runbook_snapshot_id=None, project_id=None, space_id=None, multi_tenancy_mode=None, connectivity_policy=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """RunbookResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._runbook_process_id = None
        self._published_runbook_snapshot_id = None
        self._project_id = None
        self._space_id = None
        self._multi_tenancy_mode = None
        self._connectivity_policy = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if runbook_process_id is not None:
            self.runbook_process_id = runbook_process_id
        if published_runbook_snapshot_id is not None:
            self.published_runbook_snapshot_id = published_runbook_snapshot_id
        if project_id is not None:
            self.project_id = project_id
        if space_id is not None:
            self.space_id = space_id
        if multi_tenancy_mode is not None:
            self.multi_tenancy_mode = multi_tenancy_mode
        if connectivity_policy is not None:
            self.connectivity_policy = connectivity_policy
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this RunbookResource.  # noqa: E501


        :return: The id of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunbookResource.


        :param id: The id of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RunbookResource.  # noqa: E501


        :return: The name of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RunbookResource.


        :param name: The name of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RunbookResource.  # noqa: E501


        :return: The description of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RunbookResource.


        :param description: The description of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def runbook_process_id(self):
        """Gets the runbook_process_id of this RunbookResource.  # noqa: E501


        :return: The runbook_process_id of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._runbook_process_id

    @runbook_process_id.setter
    def runbook_process_id(self, runbook_process_id):
        """Sets the runbook_process_id of this RunbookResource.


        :param runbook_process_id: The runbook_process_id of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._runbook_process_id = runbook_process_id

    @property
    def published_runbook_snapshot_id(self):
        """Gets the published_runbook_snapshot_id of this RunbookResource.  # noqa: E501


        :return: The published_runbook_snapshot_id of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._published_runbook_snapshot_id

    @published_runbook_snapshot_id.setter
    def published_runbook_snapshot_id(self, published_runbook_snapshot_id):
        """Sets the published_runbook_snapshot_id of this RunbookResource.


        :param published_runbook_snapshot_id: The published_runbook_snapshot_id of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._published_runbook_snapshot_id = published_runbook_snapshot_id

    @property
    def project_id(self):
        """Gets the project_id of this RunbookResource.  # noqa: E501


        :return: The project_id of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RunbookResource.


        :param project_id: The project_id of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def space_id(self):
        """Gets the space_id of this RunbookResource.  # noqa: E501


        :return: The space_id of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this RunbookResource.


        :param space_id: The space_id of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def multi_tenancy_mode(self):
        """Gets the multi_tenancy_mode of this RunbookResource.  # noqa: E501


        :return: The multi_tenancy_mode of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._multi_tenancy_mode

    @multi_tenancy_mode.setter
    def multi_tenancy_mode(self, multi_tenancy_mode):
        """Sets the multi_tenancy_mode of this RunbookResource.


        :param multi_tenancy_mode: The multi_tenancy_mode of this RunbookResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Untenanted", "TenantedOrUntenanted", "Tenanted"]  # noqa: E501
        if multi_tenancy_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `multi_tenancy_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(multi_tenancy_mode, allowed_values)
            )

        self._multi_tenancy_mode = multi_tenancy_mode

    @property
    def connectivity_policy(self):
        """Gets the connectivity_policy of this RunbookResource.  # noqa: E501


        :return: The connectivity_policy of this RunbookResource.  # noqa: E501
        :rtype: ProjectConnectivityPolicy
        """
        return self._connectivity_policy

    @connectivity_policy.setter
    def connectivity_policy(self, connectivity_policy):
        """Sets the connectivity_policy of this RunbookResource.


        :param connectivity_policy: The connectivity_policy of this RunbookResource.  # noqa: E501
        :type: ProjectConnectivityPolicy
        """

        self._connectivity_policy = connectivity_policy

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this RunbookResource.  # noqa: E501


        :return: The last_modified_on of this RunbookResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this RunbookResource.


        :param last_modified_on: The last_modified_on of this RunbookResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this RunbookResource.  # noqa: E501


        :return: The last_modified_by of this RunbookResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this RunbookResource.


        :param last_modified_by: The last_modified_by of this RunbookResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this RunbookResource.  # noqa: E501


        :return: The links of this RunbookResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RunbookResource.


        :param links: The links of this RunbookResource.  # noqa: E501
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
        if issubclass(RunbookResource, dict):
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
        if not isinstance(other, RunbookResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
