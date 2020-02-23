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


class MachineHealthCheckPolicy(object):
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
        'power_shell_health_check_policy': 'MachineScriptPolicy',
        'bash_health_check_policy': 'MachineScriptPolicy',
        'health_check_interval': 'str',
        'health_check_cron': 'str',
        'health_check_cron_timezone': 'str',
        'health_check_type': 'str'
    }

    attribute_map = {
        'power_shell_health_check_policy': 'PowerShellHealthCheckPolicy',
        'bash_health_check_policy': 'BashHealthCheckPolicy',
        'health_check_interval': 'HealthCheckInterval',
        'health_check_cron': 'HealthCheckCron',
        'health_check_cron_timezone': 'HealthCheckCronTimezone',
        'health_check_type': 'HealthCheckType'
    }

    def __init__(self, power_shell_health_check_policy=None, bash_health_check_policy=None, health_check_interval=None, health_check_cron=None, health_check_cron_timezone=None, health_check_type=None):  # noqa: E501
        """MachineHealthCheckPolicy - a model defined in Swagger"""  # noqa: E501
        self._power_shell_health_check_policy = None
        self._bash_health_check_policy = None
        self._health_check_interval = None
        self._health_check_cron = None
        self._health_check_cron_timezone = None
        self._health_check_type = None
        self.discriminator = None
        if power_shell_health_check_policy is not None:
            self.power_shell_health_check_policy = power_shell_health_check_policy
        if bash_health_check_policy is not None:
            self.bash_health_check_policy = bash_health_check_policy
        if health_check_interval is not None:
            self.health_check_interval = health_check_interval
        if health_check_cron is not None:
            self.health_check_cron = health_check_cron
        if health_check_cron_timezone is not None:
            self.health_check_cron_timezone = health_check_cron_timezone
        if health_check_type is not None:
            self.health_check_type = health_check_type

    @property
    def power_shell_health_check_policy(self):
        """Gets the power_shell_health_check_policy of this MachineHealthCheckPolicy.  # noqa: E501


        :return: The power_shell_health_check_policy of this MachineHealthCheckPolicy.  # noqa: E501
        :rtype: MachineScriptPolicy
        """
        return self._power_shell_health_check_policy

    @power_shell_health_check_policy.setter
    def power_shell_health_check_policy(self, power_shell_health_check_policy):
        """Sets the power_shell_health_check_policy of this MachineHealthCheckPolicy.


        :param power_shell_health_check_policy: The power_shell_health_check_policy of this MachineHealthCheckPolicy.  # noqa: E501
        :type: MachineScriptPolicy
        """

        self._power_shell_health_check_policy = power_shell_health_check_policy

    @property
    def bash_health_check_policy(self):
        """Gets the bash_health_check_policy of this MachineHealthCheckPolicy.  # noqa: E501


        :return: The bash_health_check_policy of this MachineHealthCheckPolicy.  # noqa: E501
        :rtype: MachineScriptPolicy
        """
        return self._bash_health_check_policy

    @bash_health_check_policy.setter
    def bash_health_check_policy(self, bash_health_check_policy):
        """Sets the bash_health_check_policy of this MachineHealthCheckPolicy.


        :param bash_health_check_policy: The bash_health_check_policy of this MachineHealthCheckPolicy.  # noqa: E501
        :type: MachineScriptPolicy
        """

        self._bash_health_check_policy = bash_health_check_policy

    @property
    def health_check_interval(self):
        """Gets the health_check_interval of this MachineHealthCheckPolicy.  # noqa: E501


        :return: The health_check_interval of this MachineHealthCheckPolicy.  # noqa: E501
        :rtype: str
        """
        return self._health_check_interval

    @health_check_interval.setter
    def health_check_interval(self, health_check_interval):
        """Sets the health_check_interval of this MachineHealthCheckPolicy.


        :param health_check_interval: The health_check_interval of this MachineHealthCheckPolicy.  # noqa: E501
        :type: str
        """

        self._health_check_interval = health_check_interval

    @property
    def health_check_cron(self):
        """Gets the health_check_cron of this MachineHealthCheckPolicy.  # noqa: E501


        :return: The health_check_cron of this MachineHealthCheckPolicy.  # noqa: E501
        :rtype: str
        """
        return self._health_check_cron

    @health_check_cron.setter
    def health_check_cron(self, health_check_cron):
        """Sets the health_check_cron of this MachineHealthCheckPolicy.


        :param health_check_cron: The health_check_cron of this MachineHealthCheckPolicy.  # noqa: E501
        :type: str
        """

        self._health_check_cron = health_check_cron

    @property
    def health_check_cron_timezone(self):
        """Gets the health_check_cron_timezone of this MachineHealthCheckPolicy.  # noqa: E501


        :return: The health_check_cron_timezone of this MachineHealthCheckPolicy.  # noqa: E501
        :rtype: str
        """
        return self._health_check_cron_timezone

    @health_check_cron_timezone.setter
    def health_check_cron_timezone(self, health_check_cron_timezone):
        """Sets the health_check_cron_timezone of this MachineHealthCheckPolicy.


        :param health_check_cron_timezone: The health_check_cron_timezone of this MachineHealthCheckPolicy.  # noqa: E501
        :type: str
        """

        self._health_check_cron_timezone = health_check_cron_timezone

    @property
    def health_check_type(self):
        """Gets the health_check_type of this MachineHealthCheckPolicy.  # noqa: E501


        :return: The health_check_type of this MachineHealthCheckPolicy.  # noqa: E501
        :rtype: str
        """
        return self._health_check_type

    @health_check_type.setter
    def health_check_type(self, health_check_type):
        """Sets the health_check_type of this MachineHealthCheckPolicy.


        :param health_check_type: The health_check_type of this MachineHealthCheckPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["RunScript", "OnlyConnectivity"]  # noqa: E501
        if health_check_type not in allowed_values:
            raise ValueError(
                "Invalid value for `health_check_type` ({0}), must be one of {1}"  # noqa: E501
                .format(health_check_type, allowed_values)
            )

        self._health_check_type = health_check_type

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
        if issubclass(MachineHealthCheckPolicy, dict):
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
        if not isinstance(other, MachineHealthCheckPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
