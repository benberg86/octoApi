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


class UserPermissionSetResource(object):
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
        'space_permissions': 'object',
        'system_permissions': 'list[str]',
        'teams': 'list[ProjectedTeamReferenceDataItem]',
        'is_teams_complete': 'bool',
        'is_permissions_complete': 'bool',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'space_permissions': 'SpacePermissions',
        'system_permissions': 'SystemPermissions',
        'teams': 'Teams',
        'is_teams_complete': 'IsTeamsComplete',
        'is_permissions_complete': 'IsPermissionsComplete',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, space_permissions=None, system_permissions=None, teams=None, is_teams_complete=None, is_permissions_complete=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """UserPermissionSetResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._space_permissions = None
        self._system_permissions = None
        self._teams = None
        self._is_teams_complete = None
        self._is_permissions_complete = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if space_permissions is not None:
            self.space_permissions = space_permissions
        if system_permissions is not None:
            self.system_permissions = system_permissions
        if teams is not None:
            self.teams = teams
        if is_teams_complete is not None:
            self.is_teams_complete = is_teams_complete
        if is_permissions_complete is not None:
            self.is_permissions_complete = is_permissions_complete
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this UserPermissionSetResource.  # noqa: E501


        :return: The id of this UserPermissionSetResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserPermissionSetResource.


        :param id: The id of this UserPermissionSetResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def space_permissions(self):
        """Gets the space_permissions of this UserPermissionSetResource.  # noqa: E501


        :return: The space_permissions of this UserPermissionSetResource.  # noqa: E501
        :rtype: object
        """
        return self._space_permissions

    @space_permissions.setter
    def space_permissions(self, space_permissions):
        """Sets the space_permissions of this UserPermissionSetResource.


        :param space_permissions: The space_permissions of this UserPermissionSetResource.  # noqa: E501
        :type: object
        """

        self._space_permissions = space_permissions

    @property
    def system_permissions(self):
        """Gets the system_permissions of this UserPermissionSetResource.  # noqa: E501


        :return: The system_permissions of this UserPermissionSetResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._system_permissions

    @system_permissions.setter
    def system_permissions(self, system_permissions):
        """Sets the system_permissions of this UserPermissionSetResource.


        :param system_permissions: The system_permissions of this UserPermissionSetResource.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AdministerSystem", "ProjectEdit", "ProjectView", "ProjectCreate", "ProjectDelete", "ProcessView", "ProcessEdit", "VariableEdit", "VariableEditUnscoped", "VariableView", "VariableViewUnscoped", "ReleaseCreate", "ReleaseView", "ReleaseEdit", "ReleaseDelete", "DefectReport", "DefectResolve", "DeploymentCreate", "DeploymentDelete", "DeploymentView", "EnvironmentView", "EnvironmentCreate", "EnvironmentEdit", "EnvironmentDelete", "MachineCreate", "MachineEdit", "MachineView", "MachineDelete", "ArtifactView", "ArtifactCreate", "ArtifactEdit", "ArtifactDelete", "FeedView", "EventView", "LibraryVariableSetView", "LibraryVariableSetCreate", "LibraryVariableSetEdit", "LibraryVariableSetDelete", "ProjectGroupView", "ProjectGroupCreate", "ProjectGroupEdit", "ProjectGroupDelete", "TeamCreate", "TeamView", "TeamEdit", "TeamDelete", "UserView", "UserInvite", "UserRoleView", "UserRoleEdit", "TaskView", "TaskCreate", "TaskCancel", "TaskEdit", "InterruptionView", "InterruptionSubmit", "InterruptionViewSubmitResponsible", "BuiltInFeedPush", "BuiltInFeedAdminister", "BuiltInFeedDownload", "ActionTemplateView", "ActionTemplateCreate", "ActionTemplateEdit", "ActionTemplateDelete", "LifecycleCreate", "LifecycleView", "LifecycleEdit", "LifecycleDelete", "AccountView", "AccountEdit", "AccountCreate", "AccountDelete", "TenantCreate", "TenantEdit", "TenantView", "TenantDelete", "TagSetCreate", "TagSetEdit", "TagSetDelete", "MachinePolicyCreate", "MachinePolicyView", "MachinePolicyEdit", "MachinePolicyDelete", "ProxyCreate", "ProxyView", "ProxyEdit", "ProxyDelete", "SubscriptionCreate", "SubscriptionView", "SubscriptionEdit", "SubscriptionDelete", "TriggerCreate", "TriggerView", "TriggerEdit", "TriggerDelete", "CertificateView", "CertificateCreate", "CertificateEdit", "CertificateDelete", "CertificateExportPrivateKey", "UserEdit", "ConfigureServer", "FeedEdit", "WorkerView", "WorkerEdit", "SpaceEdit", "SpaceView", "SpaceDelete", "SpaceCreate", "BuildInformationPush", "BuildInformationAdminister", "RunbookView", "RunbookEdit", "RunbookRunView", "RunbookRunDelete", "RunbookRunCreate"]  # noqa: E501
        if not set(system_permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `system_permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(system_permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._system_permissions = system_permissions

    @property
    def teams(self):
        """Gets the teams of this UserPermissionSetResource.  # noqa: E501


        :return: The teams of this UserPermissionSetResource.  # noqa: E501
        :rtype: list[ProjectedTeamReferenceDataItem]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this UserPermissionSetResource.


        :param teams: The teams of this UserPermissionSetResource.  # noqa: E501
        :type: list[ProjectedTeamReferenceDataItem]
        """

        self._teams = teams

    @property
    def is_teams_complete(self):
        """Gets the is_teams_complete of this UserPermissionSetResource.  # noqa: E501


        :return: The is_teams_complete of this UserPermissionSetResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_teams_complete

    @is_teams_complete.setter
    def is_teams_complete(self, is_teams_complete):
        """Sets the is_teams_complete of this UserPermissionSetResource.


        :param is_teams_complete: The is_teams_complete of this UserPermissionSetResource.  # noqa: E501
        :type: bool
        """

        self._is_teams_complete = is_teams_complete

    @property
    def is_permissions_complete(self):
        """Gets the is_permissions_complete of this UserPermissionSetResource.  # noqa: E501


        :return: The is_permissions_complete of this UserPermissionSetResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_permissions_complete

    @is_permissions_complete.setter
    def is_permissions_complete(self, is_permissions_complete):
        """Sets the is_permissions_complete of this UserPermissionSetResource.


        :param is_permissions_complete: The is_permissions_complete of this UserPermissionSetResource.  # noqa: E501
        :type: bool
        """

        self._is_permissions_complete = is_permissions_complete

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this UserPermissionSetResource.  # noqa: E501


        :return: The last_modified_on of this UserPermissionSetResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this UserPermissionSetResource.


        :param last_modified_on: The last_modified_on of this UserPermissionSetResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this UserPermissionSetResource.  # noqa: E501


        :return: The last_modified_by of this UserPermissionSetResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this UserPermissionSetResource.


        :param last_modified_by: The last_modified_by of this UserPermissionSetResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this UserPermissionSetResource.  # noqa: E501


        :return: The links of this UserPermissionSetResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserPermissionSetResource.


        :param links: The links of this UserPermissionSetResource.  # noqa: E501
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
        if issubclass(UserPermissionSetResource, dict):
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
        if not isinstance(other, UserPermissionSetResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
