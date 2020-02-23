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


class PackageVersionResource(object):
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
        'package_id': 'str',
        'feed_id': 'str',
        'links': 'dict(str, str)',
        'version': 'str',
        'published': 'datetime',
        'size_bytes': 'int',
        'title': 'str',
        'release_notes': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'package_id': 'PackageId',
        'feed_id': 'FeedId',
        'links': 'Links',
        'version': 'Version',
        'published': 'Published',
        'size_bytes': 'SizeBytes',
        'title': 'Title',
        'release_notes': 'ReleaseNotes'
    }

    def __init__(self, id=None, package_id=None, feed_id=None, links=None, version=None, published=None, size_bytes=None, title=None, release_notes=None):  # noqa: E501
        """PackageVersionResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._package_id = None
        self._feed_id = None
        self._links = None
        self._version = None
        self._published = None
        self._size_bytes = None
        self._title = None
        self._release_notes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if package_id is not None:
            self.package_id = package_id
        if feed_id is not None:
            self.feed_id = feed_id
        if links is not None:
            self.links = links
        if version is not None:
            self.version = version
        if published is not None:
            self.published = published
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if title is not None:
            self.title = title
        if release_notes is not None:
            self.release_notes = release_notes

    @property
    def id(self):
        """Gets the id of this PackageVersionResource.  # noqa: E501


        :return: The id of this PackageVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageVersionResource.


        :param id: The id of this PackageVersionResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def package_id(self):
        """Gets the package_id of this PackageVersionResource.  # noqa: E501


        :return: The package_id of this PackageVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this PackageVersionResource.


        :param package_id: The package_id of this PackageVersionResource.  # noqa: E501
        :type: str
        """

        self._package_id = package_id

    @property
    def feed_id(self):
        """Gets the feed_id of this PackageVersionResource.  # noqa: E501


        :return: The feed_id of this PackageVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this PackageVersionResource.


        :param feed_id: The feed_id of this PackageVersionResource.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

    @property
    def links(self):
        """Gets the links of this PackageVersionResource.  # noqa: E501


        :return: The links of this PackageVersionResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PackageVersionResource.


        :param links: The links of this PackageVersionResource.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    @property
    def version(self):
        """Gets the version of this PackageVersionResource.  # noqa: E501


        :return: The version of this PackageVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PackageVersionResource.


        :param version: The version of this PackageVersionResource.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def published(self):
        """Gets the published of this PackageVersionResource.  # noqa: E501


        :return: The published of this PackageVersionResource.  # noqa: E501
        :rtype: datetime
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this PackageVersionResource.


        :param published: The published of this PackageVersionResource.  # noqa: E501
        :type: datetime
        """

        self._published = published

    @property
    def size_bytes(self):
        """Gets the size_bytes of this PackageVersionResource.  # noqa: E501


        :return: The size_bytes of this PackageVersionResource.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this PackageVersionResource.


        :param size_bytes: The size_bytes of this PackageVersionResource.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

    @property
    def title(self):
        """Gets the title of this PackageVersionResource.  # noqa: E501


        :return: The title of this PackageVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PackageVersionResource.


        :param title: The title of this PackageVersionResource.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def release_notes(self):
        """Gets the release_notes of this PackageVersionResource.  # noqa: E501


        :return: The release_notes of this PackageVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this PackageVersionResource.


        :param release_notes: The release_notes of this PackageVersionResource.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

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
        if issubclass(PackageVersionResource, dict):
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
        if not isinstance(other, PackageVersionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
