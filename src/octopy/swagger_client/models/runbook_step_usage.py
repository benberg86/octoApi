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


class RunbookStepUsage(object):
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
        'process_id': 'str',
        'runbook_id': 'str',
        'runbook_name': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'project_slug': 'str',
        'steps': 'list[StepUsageEntry]'
    }

    attribute_map = {
        'process_id': 'ProcessId',
        'runbook_id': 'RunbookId',
        'runbook_name': 'RunbookName',
        'project_name': 'ProjectName',
        'project_id': 'ProjectId',
        'project_slug': 'ProjectSlug',
        'steps': 'Steps'
    }

    def __init__(self, process_id=None, runbook_id=None, runbook_name=None, project_name=None, project_id=None, project_slug=None, steps=None):  # noqa: E501
        """RunbookStepUsage - a model defined in Swagger"""  # noqa: E501
        self._process_id = None
        self._runbook_id = None
        self._runbook_name = None
        self._project_name = None
        self._project_id = None
        self._project_slug = None
        self._steps = None
        self.discriminator = None
        if process_id is not None:
            self.process_id = process_id
        if runbook_id is not None:
            self.runbook_id = runbook_id
        if runbook_name is not None:
            self.runbook_name = runbook_name
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if project_slug is not None:
            self.project_slug = project_slug
        if steps is not None:
            self.steps = steps

    @property
    def process_id(self):
        """Gets the process_id of this RunbookStepUsage.  # noqa: E501


        :return: The process_id of this RunbookStepUsage.  # noqa: E501
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this RunbookStepUsage.


        :param process_id: The process_id of this RunbookStepUsage.  # noqa: E501
        :type: str
        """

        self._process_id = process_id

    @property
    def runbook_id(self):
        """Gets the runbook_id of this RunbookStepUsage.  # noqa: E501


        :return: The runbook_id of this RunbookStepUsage.  # noqa: E501
        :rtype: str
        """
        return self._runbook_id

    @runbook_id.setter
    def runbook_id(self, runbook_id):
        """Sets the runbook_id of this RunbookStepUsage.


        :param runbook_id: The runbook_id of this RunbookStepUsage.  # noqa: E501
        :type: str
        """

        self._runbook_id = runbook_id

    @property
    def runbook_name(self):
        """Gets the runbook_name of this RunbookStepUsage.  # noqa: E501


        :return: The runbook_name of this RunbookStepUsage.  # noqa: E501
        :rtype: str
        """
        return self._runbook_name

    @runbook_name.setter
    def runbook_name(self, runbook_name):
        """Sets the runbook_name of this RunbookStepUsage.


        :param runbook_name: The runbook_name of this RunbookStepUsage.  # noqa: E501
        :type: str
        """

        self._runbook_name = runbook_name

    @property
    def project_name(self):
        """Gets the project_name of this RunbookStepUsage.  # noqa: E501


        :return: The project_name of this RunbookStepUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this RunbookStepUsage.


        :param project_name: The project_name of this RunbookStepUsage.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this RunbookStepUsage.  # noqa: E501


        :return: The project_id of this RunbookStepUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RunbookStepUsage.


        :param project_id: The project_id of this RunbookStepUsage.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_slug(self):
        """Gets the project_slug of this RunbookStepUsage.  # noqa: E501


        :return: The project_slug of this RunbookStepUsage.  # noqa: E501
        :rtype: str
        """
        return self._project_slug

    @project_slug.setter
    def project_slug(self, project_slug):
        """Sets the project_slug of this RunbookStepUsage.


        :param project_slug: The project_slug of this RunbookStepUsage.  # noqa: E501
        :type: str
        """

        self._project_slug = project_slug

    @property
    def steps(self):
        """Gets the steps of this RunbookStepUsage.  # noqa: E501


        :return: The steps of this RunbookStepUsage.  # noqa: E501
        :rtype: list[StepUsageEntry]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this RunbookStepUsage.


        :param steps: The steps of this RunbookStepUsage.  # noqa: E501
        :type: list[StepUsageEntry]
        """

        self._steps = steps

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
        if issubclass(RunbookStepUsage, dict):
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
        if not isinstance(other, RunbookStepUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
