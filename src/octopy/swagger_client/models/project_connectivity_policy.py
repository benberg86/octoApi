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


class ProjectConnectivityPolicy(object):
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
        'skip_machine_behavior': 'str',
        'target_roles': 'list[str]',
        'allow_deployments_to_no_targets': 'bool',
        'exclude_unhealthy_targets': 'bool'
    }

    attribute_map = {
        'skip_machine_behavior': 'SkipMachineBehavior',
        'target_roles': 'TargetRoles',
        'allow_deployments_to_no_targets': 'AllowDeploymentsToNoTargets',
        'exclude_unhealthy_targets': 'ExcludeUnhealthyTargets'
    }

    def __init__(self, skip_machine_behavior=None, target_roles=None, allow_deployments_to_no_targets=None, exclude_unhealthy_targets=None):  # noqa: E501
        """ProjectConnectivityPolicy - a model defined in Swagger"""  # noqa: E501
        self._skip_machine_behavior = None
        self._target_roles = None
        self._allow_deployments_to_no_targets = None
        self._exclude_unhealthy_targets = None
        self.discriminator = None
        if skip_machine_behavior is not None:
            self.skip_machine_behavior = skip_machine_behavior
        if target_roles is not None:
            self.target_roles = target_roles
        if allow_deployments_to_no_targets is not None:
            self.allow_deployments_to_no_targets = allow_deployments_to_no_targets
        if exclude_unhealthy_targets is not None:
            self.exclude_unhealthy_targets = exclude_unhealthy_targets

    @property
    def skip_machine_behavior(self):
        """Gets the skip_machine_behavior of this ProjectConnectivityPolicy.  # noqa: E501


        :return: The skip_machine_behavior of this ProjectConnectivityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._skip_machine_behavior

    @skip_machine_behavior.setter
    def skip_machine_behavior(self, skip_machine_behavior):
        """Sets the skip_machine_behavior of this ProjectConnectivityPolicy.


        :param skip_machine_behavior: The skip_machine_behavior of this ProjectConnectivityPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "SkipUnavailableMachines"]  # noqa: E501
        if skip_machine_behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `skip_machine_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(skip_machine_behavior, allowed_values)
            )

        self._skip_machine_behavior = skip_machine_behavior

    @property
    def target_roles(self):
        """Gets the target_roles of this ProjectConnectivityPolicy.  # noqa: E501


        :return: The target_roles of this ProjectConnectivityPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_roles

    @target_roles.setter
    def target_roles(self, target_roles):
        """Sets the target_roles of this ProjectConnectivityPolicy.


        :param target_roles: The target_roles of this ProjectConnectivityPolicy.  # noqa: E501
        :type: list[str]
        """

        self._target_roles = target_roles

    @property
    def allow_deployments_to_no_targets(self):
        """Gets the allow_deployments_to_no_targets of this ProjectConnectivityPolicy.  # noqa: E501


        :return: The allow_deployments_to_no_targets of this ProjectConnectivityPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._allow_deployments_to_no_targets

    @allow_deployments_to_no_targets.setter
    def allow_deployments_to_no_targets(self, allow_deployments_to_no_targets):
        """Sets the allow_deployments_to_no_targets of this ProjectConnectivityPolicy.


        :param allow_deployments_to_no_targets: The allow_deployments_to_no_targets of this ProjectConnectivityPolicy.  # noqa: E501
        :type: bool
        """

        self._allow_deployments_to_no_targets = allow_deployments_to_no_targets

    @property
    def exclude_unhealthy_targets(self):
        """Gets the exclude_unhealthy_targets of this ProjectConnectivityPolicy.  # noqa: E501


        :return: The exclude_unhealthy_targets of this ProjectConnectivityPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_unhealthy_targets

    @exclude_unhealthy_targets.setter
    def exclude_unhealthy_targets(self, exclude_unhealthy_targets):
        """Sets the exclude_unhealthy_targets of this ProjectConnectivityPolicy.


        :param exclude_unhealthy_targets: The exclude_unhealthy_targets of this ProjectConnectivityPolicy.  # noqa: E501
        :type: bool
        """

        self._exclude_unhealthy_targets = exclude_unhealthy_targets

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
        if issubclass(ProjectConnectivityPolicy, dict):
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
        if not isinstance(other, ProjectConnectivityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
