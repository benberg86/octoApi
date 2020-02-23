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


class PhaseResource(object):
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
        'automatic_deployment_targets': 'list[str]',
        'optional_deployment_targets': 'list[str]',
        'minimum_environments_before_promotion': 'int',
        'is_optional_phase': 'bool',
        'release_retention_policy': 'RetentionPeriod',
        'tentacle_retention_policy': 'RetentionPeriod'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'automatic_deployment_targets': 'AutomaticDeploymentTargets',
        'optional_deployment_targets': 'OptionalDeploymentTargets',
        'minimum_environments_before_promotion': 'MinimumEnvironmentsBeforePromotion',
        'is_optional_phase': 'IsOptionalPhase',
        'release_retention_policy': 'ReleaseRetentionPolicy',
        'tentacle_retention_policy': 'TentacleRetentionPolicy'
    }

    def __init__(self, id=None, name=None, automatic_deployment_targets=None, optional_deployment_targets=None, minimum_environments_before_promotion=None, is_optional_phase=None, release_retention_policy=None, tentacle_retention_policy=None):  # noqa: E501
        """PhaseResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._automatic_deployment_targets = None
        self._optional_deployment_targets = None
        self._minimum_environments_before_promotion = None
        self._is_optional_phase = None
        self._release_retention_policy = None
        self._tentacle_retention_policy = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if automatic_deployment_targets is not None:
            self.automatic_deployment_targets = automatic_deployment_targets
        if optional_deployment_targets is not None:
            self.optional_deployment_targets = optional_deployment_targets
        if minimum_environments_before_promotion is not None:
            self.minimum_environments_before_promotion = minimum_environments_before_promotion
        if is_optional_phase is not None:
            self.is_optional_phase = is_optional_phase
        if release_retention_policy is not None:
            self.release_retention_policy = release_retention_policy
        if tentacle_retention_policy is not None:
            self.tentacle_retention_policy = tentacle_retention_policy

    @property
    def id(self):
        """Gets the id of this PhaseResource.  # noqa: E501


        :return: The id of this PhaseResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhaseResource.


        :param id: The id of this PhaseResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PhaseResource.  # noqa: E501


        :return: The name of this PhaseResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhaseResource.


        :param name: The name of this PhaseResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def automatic_deployment_targets(self):
        """Gets the automatic_deployment_targets of this PhaseResource.  # noqa: E501


        :return: The automatic_deployment_targets of this PhaseResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._automatic_deployment_targets

    @automatic_deployment_targets.setter
    def automatic_deployment_targets(self, automatic_deployment_targets):
        """Sets the automatic_deployment_targets of this PhaseResource.


        :param automatic_deployment_targets: The automatic_deployment_targets of this PhaseResource.  # noqa: E501
        :type: list[str]
        """

        self._automatic_deployment_targets = automatic_deployment_targets

    @property
    def optional_deployment_targets(self):
        """Gets the optional_deployment_targets of this PhaseResource.  # noqa: E501


        :return: The optional_deployment_targets of this PhaseResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._optional_deployment_targets

    @optional_deployment_targets.setter
    def optional_deployment_targets(self, optional_deployment_targets):
        """Sets the optional_deployment_targets of this PhaseResource.


        :param optional_deployment_targets: The optional_deployment_targets of this PhaseResource.  # noqa: E501
        :type: list[str]
        """

        self._optional_deployment_targets = optional_deployment_targets

    @property
    def minimum_environments_before_promotion(self):
        """Gets the minimum_environments_before_promotion of this PhaseResource.  # noqa: E501


        :return: The minimum_environments_before_promotion of this PhaseResource.  # noqa: E501
        :rtype: int
        """
        return self._minimum_environments_before_promotion

    @minimum_environments_before_promotion.setter
    def minimum_environments_before_promotion(self, minimum_environments_before_promotion):
        """Sets the minimum_environments_before_promotion of this PhaseResource.


        :param minimum_environments_before_promotion: The minimum_environments_before_promotion of this PhaseResource.  # noqa: E501
        :type: int
        """

        self._minimum_environments_before_promotion = minimum_environments_before_promotion

    @property
    def is_optional_phase(self):
        """Gets the is_optional_phase of this PhaseResource.  # noqa: E501


        :return: The is_optional_phase of this PhaseResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_optional_phase

    @is_optional_phase.setter
    def is_optional_phase(self, is_optional_phase):
        """Sets the is_optional_phase of this PhaseResource.


        :param is_optional_phase: The is_optional_phase of this PhaseResource.  # noqa: E501
        :type: bool
        """

        self._is_optional_phase = is_optional_phase

    @property
    def release_retention_policy(self):
        """Gets the release_retention_policy of this PhaseResource.  # noqa: E501


        :return: The release_retention_policy of this PhaseResource.  # noqa: E501
        :rtype: RetentionPeriod
        """
        return self._release_retention_policy

    @release_retention_policy.setter
    def release_retention_policy(self, release_retention_policy):
        """Sets the release_retention_policy of this PhaseResource.


        :param release_retention_policy: The release_retention_policy of this PhaseResource.  # noqa: E501
        :type: RetentionPeriod
        """

        self._release_retention_policy = release_retention_policy

    @property
    def tentacle_retention_policy(self):
        """Gets the tentacle_retention_policy of this PhaseResource.  # noqa: E501


        :return: The tentacle_retention_policy of this PhaseResource.  # noqa: E501
        :rtype: RetentionPeriod
        """
        return self._tentacle_retention_policy

    @tentacle_retention_policy.setter
    def tentacle_retention_policy(self, tentacle_retention_policy):
        """Sets the tentacle_retention_policy of this PhaseResource.


        :param tentacle_retention_policy: The tentacle_retention_policy of this PhaseResource.  # noqa: E501
        :type: RetentionPeriod
        """

        self._tentacle_retention_policy = tentacle_retention_policy

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
        if issubclass(PhaseResource, dict):
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
        if not isinstance(other, PhaseResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
