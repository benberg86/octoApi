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


class MachineCleanupPolicy(object):
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
        'delete_machines_behavior': 'str',
        'delete_machines_elapsed_time_span': 'str'
    }

    attribute_map = {
        'delete_machines_behavior': 'DeleteMachinesBehavior',
        'delete_machines_elapsed_time_span': 'DeleteMachinesElapsedTimeSpan'
    }

    def __init__(self, delete_machines_behavior=None, delete_machines_elapsed_time_span=None):  # noqa: E501
        """MachineCleanupPolicy - a model defined in Swagger"""  # noqa: E501
        self._delete_machines_behavior = None
        self._delete_machines_elapsed_time_span = None
        self.discriminator = None
        if delete_machines_behavior is not None:
            self.delete_machines_behavior = delete_machines_behavior
        if delete_machines_elapsed_time_span is not None:
            self.delete_machines_elapsed_time_span = delete_machines_elapsed_time_span

    @property
    def delete_machines_behavior(self):
        """Gets the delete_machines_behavior of this MachineCleanupPolicy.  # noqa: E501


        :return: The delete_machines_behavior of this MachineCleanupPolicy.  # noqa: E501
        :rtype: str
        """
        return self._delete_machines_behavior

    @delete_machines_behavior.setter
    def delete_machines_behavior(self, delete_machines_behavior):
        """Sets the delete_machines_behavior of this MachineCleanupPolicy.


        :param delete_machines_behavior: The delete_machines_behavior of this MachineCleanupPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["DoNotDelete", "DeleteUnavailableMachines"]  # noqa: E501
        if delete_machines_behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `delete_machines_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(delete_machines_behavior, allowed_values)
            )

        self._delete_machines_behavior = delete_machines_behavior

    @property
    def delete_machines_elapsed_time_span(self):
        """Gets the delete_machines_elapsed_time_span of this MachineCleanupPolicy.  # noqa: E501


        :return: The delete_machines_elapsed_time_span of this MachineCleanupPolicy.  # noqa: E501
        :rtype: str
        """
        return self._delete_machines_elapsed_time_span

    @delete_machines_elapsed_time_span.setter
    def delete_machines_elapsed_time_span(self, delete_machines_elapsed_time_span):
        """Sets the delete_machines_elapsed_time_span of this MachineCleanupPolicy.


        :param delete_machines_elapsed_time_span: The delete_machines_elapsed_time_span of this MachineCleanupPolicy.  # noqa: E501
        :type: str
        """

        self._delete_machines_elapsed_time_span = delete_machines_elapsed_time_span

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
        if issubclass(MachineCleanupPolicy, dict):
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
        if not isinstance(other, MachineCleanupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
