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


class MachineConnectionStatus(object):
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
        'machine_id': 'str',
        'logs': 'list[ActivityLogElement]',
        'status': 'str',
        'current_tentacle_version': 'str',
        'last_checked': 'datetime',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'machine_id': 'MachineId',
        'logs': 'Logs',
        'status': 'Status',
        'current_tentacle_version': 'CurrentTentacleVersion',
        'last_checked': 'LastChecked',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, machine_id=None, logs=None, status=None, current_tentacle_version=None, last_checked=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """MachineConnectionStatus - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._machine_id = None
        self._logs = None
        self._status = None
        self._current_tentacle_version = None
        self._last_checked = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if machine_id is not None:
            self.machine_id = machine_id
        if logs is not None:
            self.logs = logs
        if status is not None:
            self.status = status
        if current_tentacle_version is not None:
            self.current_tentacle_version = current_tentacle_version
        if last_checked is not None:
            self.last_checked = last_checked
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this MachineConnectionStatus.  # noqa: E501


        :return: The id of this MachineConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MachineConnectionStatus.


        :param id: The id of this MachineConnectionStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def machine_id(self):
        """Gets the machine_id of this MachineConnectionStatus.  # noqa: E501


        :return: The machine_id of this MachineConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this MachineConnectionStatus.


        :param machine_id: The machine_id of this MachineConnectionStatus.  # noqa: E501
        :type: str
        """

        self._machine_id = machine_id

    @property
    def logs(self):
        """Gets the logs of this MachineConnectionStatus.  # noqa: E501


        :return: The logs of this MachineConnectionStatus.  # noqa: E501
        :rtype: list[ActivityLogElement]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this MachineConnectionStatus.


        :param logs: The logs of this MachineConnectionStatus.  # noqa: E501
        :type: list[ActivityLogElement]
        """

        self._logs = logs

    @property
    def status(self):
        """Gets the status of this MachineConnectionStatus.  # noqa: E501


        :return: The status of this MachineConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MachineConnectionStatus.


        :param status: The status of this MachineConnectionStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def current_tentacle_version(self):
        """Gets the current_tentacle_version of this MachineConnectionStatus.  # noqa: E501


        :return: The current_tentacle_version of this MachineConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_tentacle_version

    @current_tentacle_version.setter
    def current_tentacle_version(self, current_tentacle_version):
        """Sets the current_tentacle_version of this MachineConnectionStatus.


        :param current_tentacle_version: The current_tentacle_version of this MachineConnectionStatus.  # noqa: E501
        :type: str
        """

        self._current_tentacle_version = current_tentacle_version

    @property
    def last_checked(self):
        """Gets the last_checked of this MachineConnectionStatus.  # noqa: E501


        :return: The last_checked of this MachineConnectionStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_checked

    @last_checked.setter
    def last_checked(self, last_checked):
        """Sets the last_checked of this MachineConnectionStatus.


        :param last_checked: The last_checked of this MachineConnectionStatus.  # noqa: E501
        :type: datetime
        """

        self._last_checked = last_checked

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this MachineConnectionStatus.  # noqa: E501


        :return: The last_modified_on of this MachineConnectionStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this MachineConnectionStatus.


        :param last_modified_on: The last_modified_on of this MachineConnectionStatus.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this MachineConnectionStatus.  # noqa: E501


        :return: The last_modified_by of this MachineConnectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this MachineConnectionStatus.


        :param last_modified_by: The last_modified_by of this MachineConnectionStatus.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this MachineConnectionStatus.  # noqa: E501


        :return: The links of this MachineConnectionStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MachineConnectionStatus.


        :param links: The links of this MachineConnectionStatus.  # noqa: E501
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
        if issubclass(MachineConnectionStatus, dict):
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
        if not isinstance(other, MachineConnectionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
