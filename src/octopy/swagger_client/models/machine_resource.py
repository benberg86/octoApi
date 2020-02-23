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


class MachineResource(object):
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
        'thumbprint': 'str',
        'uri': 'str',
        'is_disabled': 'bool',
        'machine_policy_id': 'str',
        'status': 'str',
        'health_status': 'str',
        'has_latest_calamari': 'bool',
        'status_summary': 'str',
        'is_in_process': 'bool',
        'endpoint': 'EndpointResource',
        'operating_system': 'str',
        'shell_name': 'str',
        'shell_version': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'thumbprint': 'Thumbprint',
        'uri': 'Uri',
        'is_disabled': 'IsDisabled',
        'machine_policy_id': 'MachinePolicyId',
        'status': 'Status',
        'health_status': 'HealthStatus',
        'has_latest_calamari': 'HasLatestCalamari',
        'status_summary': 'StatusSummary',
        'is_in_process': 'IsInProcess',
        'endpoint': 'Endpoint',
        'operating_system': 'OperatingSystem',
        'shell_name': 'ShellName',
        'shell_version': 'ShellVersion',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, thumbprint=None, uri=None, is_disabled=None, machine_policy_id=None, status=None, health_status=None, has_latest_calamari=None, status_summary=None, is_in_process=None, endpoint=None, operating_system=None, shell_name=None, shell_version=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """MachineResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._thumbprint = None
        self._uri = None
        self._is_disabled = None
        self._machine_policy_id = None
        self._status = None
        self._health_status = None
        self._has_latest_calamari = None
        self._status_summary = None
        self._is_in_process = None
        self._endpoint = None
        self._operating_system = None
        self._shell_name = None
        self._shell_version = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if thumbprint is not None:
            self.thumbprint = thumbprint
        if uri is not None:
            self.uri = uri
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if machine_policy_id is not None:
            self.machine_policy_id = machine_policy_id
        if status is not None:
            self.status = status
        if health_status is not None:
            self.health_status = health_status
        if has_latest_calamari is not None:
            self.has_latest_calamari = has_latest_calamari
        if status_summary is not None:
            self.status_summary = status_summary
        if is_in_process is not None:
            self.is_in_process = is_in_process
        if endpoint is not None:
            self.endpoint = endpoint
        if operating_system is not None:
            self.operating_system = operating_system
        if shell_name is not None:
            self.shell_name = shell_name
        if shell_version is not None:
            self.shell_version = shell_version
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this MachineResource.  # noqa: E501


        :return: The id of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MachineResource.


        :param id: The id of this MachineResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MachineResource.  # noqa: E501


        :return: The name of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MachineResource.


        :param name: The name of this MachineResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def thumbprint(self):
        """Gets the thumbprint of this MachineResource.  # noqa: E501


        :return: The thumbprint of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this MachineResource.


        :param thumbprint: The thumbprint of this MachineResource.  # noqa: E501
        :type: str
        """

        self._thumbprint = thumbprint

    @property
    def uri(self):
        """Gets the uri of this MachineResource.  # noqa: E501


        :return: The uri of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this MachineResource.


        :param uri: The uri of this MachineResource.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def is_disabled(self):
        """Gets the is_disabled of this MachineResource.  # noqa: E501


        :return: The is_disabled of this MachineResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this MachineResource.


        :param is_disabled: The is_disabled of this MachineResource.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def machine_policy_id(self):
        """Gets the machine_policy_id of this MachineResource.  # noqa: E501


        :return: The machine_policy_id of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._machine_policy_id

    @machine_policy_id.setter
    def machine_policy_id(self, machine_policy_id):
        """Sets the machine_policy_id of this MachineResource.


        :param machine_policy_id: The machine_policy_id of this MachineResource.  # noqa: E501
        :type: str
        """

        self._machine_policy_id = machine_policy_id

    @property
    def status(self):
        """Gets the status of this MachineResource.  # noqa: E501


        :return: The status of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MachineResource.


        :param status: The status of this MachineResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Online", "Offline", "Unknown", "NeedsUpgrade", "CalamariNeedsUpgrade", "Disabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def health_status(self):
        """Gets the health_status of this MachineResource.  # noqa: E501


        :return: The health_status of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this MachineResource.


        :param health_status: The health_status of this MachineResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Healthy", "Unavailable", "Unknown", "HasWarnings", "Unhealthy"]  # noqa: E501
        if health_status not in allowed_values:
            raise ValueError(
                "Invalid value for `health_status` ({0}), must be one of {1}"  # noqa: E501
                .format(health_status, allowed_values)
            )

        self._health_status = health_status

    @property
    def has_latest_calamari(self):
        """Gets the has_latest_calamari of this MachineResource.  # noqa: E501


        :return: The has_latest_calamari of this MachineResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_latest_calamari

    @has_latest_calamari.setter
    def has_latest_calamari(self, has_latest_calamari):
        """Sets the has_latest_calamari of this MachineResource.


        :param has_latest_calamari: The has_latest_calamari of this MachineResource.  # noqa: E501
        :type: bool
        """

        self._has_latest_calamari = has_latest_calamari

    @property
    def status_summary(self):
        """Gets the status_summary of this MachineResource.  # noqa: E501


        :return: The status_summary of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this MachineResource.


        :param status_summary: The status_summary of this MachineResource.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def is_in_process(self):
        """Gets the is_in_process of this MachineResource.  # noqa: E501


        :return: The is_in_process of this MachineResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_process

    @is_in_process.setter
    def is_in_process(self, is_in_process):
        """Sets the is_in_process of this MachineResource.


        :param is_in_process: The is_in_process of this MachineResource.  # noqa: E501
        :type: bool
        """

        self._is_in_process = is_in_process

    @property
    def endpoint(self):
        """Gets the endpoint of this MachineResource.  # noqa: E501


        :return: The endpoint of this MachineResource.  # noqa: E501
        :rtype: EndpointResource
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this MachineResource.


        :param endpoint: The endpoint of this MachineResource.  # noqa: E501
        :type: EndpointResource
        """

        self._endpoint = endpoint

    @property
    def operating_system(self):
        """Gets the operating_system of this MachineResource.  # noqa: E501


        :return: The operating_system of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this MachineResource.


        :param operating_system: The operating_system of this MachineResource.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def shell_name(self):
        """Gets the shell_name of this MachineResource.  # noqa: E501


        :return: The shell_name of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._shell_name

    @shell_name.setter
    def shell_name(self, shell_name):
        """Sets the shell_name of this MachineResource.


        :param shell_name: The shell_name of this MachineResource.  # noqa: E501
        :type: str
        """

        self._shell_name = shell_name

    @property
    def shell_version(self):
        """Gets the shell_version of this MachineResource.  # noqa: E501


        :return: The shell_version of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._shell_version

    @shell_version.setter
    def shell_version(self, shell_version):
        """Sets the shell_version of this MachineResource.


        :param shell_version: The shell_version of this MachineResource.  # noqa: E501
        :type: str
        """

        self._shell_version = shell_version

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this MachineResource.  # noqa: E501


        :return: The last_modified_on of this MachineResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this MachineResource.


        :param last_modified_on: The last_modified_on of this MachineResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this MachineResource.  # noqa: E501


        :return: The last_modified_by of this MachineResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this MachineResource.


        :param last_modified_by: The last_modified_by of this MachineResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this MachineResource.  # noqa: E501


        :return: The links of this MachineResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MachineResource.


        :param links: The links of this MachineResource.  # noqa: E501
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
        if issubclass(MachineResource, dict):
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
        if not isinstance(other, MachineResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
