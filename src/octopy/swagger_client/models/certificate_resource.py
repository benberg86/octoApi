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


class CertificateResource(object):
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
        'notes': 'str',
        'certificate_data': 'SensitiveValue',
        'password': 'SensitiveValue',
        'environment_ids': 'list[str]',
        'tenanted_deployment_participation': 'str',
        'tenant_ids': 'list[str]',
        'tenant_tags': 'list[str]',
        'certificate_data_format': 'str',
        'archived': 'datetime',
        'replaced_by': 'str',
        'subject_distinguished_name': 'str',
        'subject_common_name': 'str',
        'subject_organization': 'str',
        'issuer_distinguished_name': 'str',
        'issuer_common_name': 'str',
        'issuer_organization': 'str',
        'self_signed': 'bool',
        'thumbprint': 'str',
        'not_after': 'datetime',
        'not_before': 'datetime',
        'is_expired': 'bool',
        'has_private_key': 'bool',
        'version': 'int',
        'serial_number': 'str',
        'signature_algorithm_name': 'str',
        'subject_alternative_names': 'list[str]',
        'certificate_chain': 'list[X509Certificate]',
        'space_id': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'notes': 'Notes',
        'certificate_data': 'CertificateData',
        'password': 'Password',
        'environment_ids': 'EnvironmentIds',
        'tenanted_deployment_participation': 'TenantedDeploymentParticipation',
        'tenant_ids': 'TenantIds',
        'tenant_tags': 'TenantTags',
        'certificate_data_format': 'CertificateDataFormat',
        'archived': 'Archived',
        'replaced_by': 'ReplacedBy',
        'subject_distinguished_name': 'SubjectDistinguishedName',
        'subject_common_name': 'SubjectCommonName',
        'subject_organization': 'SubjectOrganization',
        'issuer_distinguished_name': 'IssuerDistinguishedName',
        'issuer_common_name': 'IssuerCommonName',
        'issuer_organization': 'IssuerOrganization',
        'self_signed': 'SelfSigned',
        'thumbprint': 'Thumbprint',
        'not_after': 'NotAfter',
        'not_before': 'NotBefore',
        'is_expired': 'IsExpired',
        'has_private_key': 'HasPrivateKey',
        'version': 'Version',
        'serial_number': 'SerialNumber',
        'signature_algorithm_name': 'SignatureAlgorithmName',
        'subject_alternative_names': 'SubjectAlternativeNames',
        'certificate_chain': 'CertificateChain',
        'space_id': 'SpaceId',
        'last_modified_on': 'LastModifiedOn',
        'last_modified_by': 'LastModifiedBy',
        'links': 'Links'
    }

    def __init__(self, id=None, name=None, notes=None, certificate_data=None, password=None, environment_ids=None, tenanted_deployment_participation=None, tenant_ids=None, tenant_tags=None, certificate_data_format=None, archived=None, replaced_by=None, subject_distinguished_name=None, subject_common_name=None, subject_organization=None, issuer_distinguished_name=None, issuer_common_name=None, issuer_organization=None, self_signed=None, thumbprint=None, not_after=None, not_before=None, is_expired=None, has_private_key=None, version=None, serial_number=None, signature_algorithm_name=None, subject_alternative_names=None, certificate_chain=None, space_id=None, last_modified_on=None, last_modified_by=None, links=None):  # noqa: E501
        """CertificateResource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._notes = None
        self._certificate_data = None
        self._password = None
        self._environment_ids = None
        self._tenanted_deployment_participation = None
        self._tenant_ids = None
        self._tenant_tags = None
        self._certificate_data_format = None
        self._archived = None
        self._replaced_by = None
        self._subject_distinguished_name = None
        self._subject_common_name = None
        self._subject_organization = None
        self._issuer_distinguished_name = None
        self._issuer_common_name = None
        self._issuer_organization = None
        self._self_signed = None
        self._thumbprint = None
        self._not_after = None
        self._not_before = None
        self._is_expired = None
        self._has_private_key = None
        self._version = None
        self._serial_number = None
        self._signature_algorithm_name = None
        self._subject_alternative_names = None
        self._certificate_chain = None
        self._space_id = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if certificate_data is not None:
            self.certificate_data = certificate_data
        if password is not None:
            self.password = password
        if environment_ids is not None:
            self.environment_ids = environment_ids
        if tenanted_deployment_participation is not None:
            self.tenanted_deployment_participation = tenanted_deployment_participation
        if tenant_ids is not None:
            self.tenant_ids = tenant_ids
        if tenant_tags is not None:
            self.tenant_tags = tenant_tags
        if certificate_data_format is not None:
            self.certificate_data_format = certificate_data_format
        if archived is not None:
            self.archived = archived
        if replaced_by is not None:
            self.replaced_by = replaced_by
        if subject_distinguished_name is not None:
            self.subject_distinguished_name = subject_distinguished_name
        if subject_common_name is not None:
            self.subject_common_name = subject_common_name
        if subject_organization is not None:
            self.subject_organization = subject_organization
        if issuer_distinguished_name is not None:
            self.issuer_distinguished_name = issuer_distinguished_name
        if issuer_common_name is not None:
            self.issuer_common_name = issuer_common_name
        if issuer_organization is not None:
            self.issuer_organization = issuer_organization
        if self_signed is not None:
            self.self_signed = self_signed
        if thumbprint is not None:
            self.thumbprint = thumbprint
        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if is_expired is not None:
            self.is_expired = is_expired
        if has_private_key is not None:
            self.has_private_key = has_private_key
        if version is not None:
            self.version = version
        if serial_number is not None:
            self.serial_number = serial_number
        if signature_algorithm_name is not None:
            self.signature_algorithm_name = signature_algorithm_name
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if space_id is not None:
            self.space_id = space_id
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this CertificateResource.  # noqa: E501


        :return: The id of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateResource.


        :param id: The id of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CertificateResource.  # noqa: E501


        :return: The name of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateResource.


        :param name: The name of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this CertificateResource.  # noqa: E501


        :return: The notes of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CertificateResource.


        :param notes: The notes of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def certificate_data(self):
        """Gets the certificate_data of this CertificateResource.  # noqa: E501


        :return: The certificate_data of this CertificateResource.  # noqa: E501
        :rtype: SensitiveValue
        """
        return self._certificate_data

    @certificate_data.setter
    def certificate_data(self, certificate_data):
        """Sets the certificate_data of this CertificateResource.


        :param certificate_data: The certificate_data of this CertificateResource.  # noqa: E501
        :type: SensitiveValue
        """

        self._certificate_data = certificate_data

    @property
    def password(self):
        """Gets the password of this CertificateResource.  # noqa: E501


        :return: The password of this CertificateResource.  # noqa: E501
        :rtype: SensitiveValue
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CertificateResource.


        :param password: The password of this CertificateResource.  # noqa: E501
        :type: SensitiveValue
        """

        self._password = password

    @property
    def environment_ids(self):
        """Gets the environment_ids of this CertificateResource.  # noqa: E501


        :return: The environment_ids of this CertificateResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment_ids

    @environment_ids.setter
    def environment_ids(self, environment_ids):
        """Sets the environment_ids of this CertificateResource.


        :param environment_ids: The environment_ids of this CertificateResource.  # noqa: E501
        :type: list[str]
        """

        self._environment_ids = environment_ids

    @property
    def tenanted_deployment_participation(self):
        """Gets the tenanted_deployment_participation of this CertificateResource.  # noqa: E501


        :return: The tenanted_deployment_participation of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._tenanted_deployment_participation

    @tenanted_deployment_participation.setter
    def tenanted_deployment_participation(self, tenanted_deployment_participation):
        """Sets the tenanted_deployment_participation of this CertificateResource.


        :param tenanted_deployment_participation: The tenanted_deployment_participation of this CertificateResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Untenanted", "TenantedOrUntenanted", "Tenanted"]  # noqa: E501
        if tenanted_deployment_participation not in allowed_values:
            raise ValueError(
                "Invalid value for `tenanted_deployment_participation` ({0}), must be one of {1}"  # noqa: E501
                .format(tenanted_deployment_participation, allowed_values)
            )

        self._tenanted_deployment_participation = tenanted_deployment_participation

    @property
    def tenant_ids(self):
        """Gets the tenant_ids of this CertificateResource.  # noqa: E501


        :return: The tenant_ids of this CertificateResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_ids

    @tenant_ids.setter
    def tenant_ids(self, tenant_ids):
        """Sets the tenant_ids of this CertificateResource.


        :param tenant_ids: The tenant_ids of this CertificateResource.  # noqa: E501
        :type: list[str]
        """

        self._tenant_ids = tenant_ids

    @property
    def tenant_tags(self):
        """Gets the tenant_tags of this CertificateResource.  # noqa: E501


        :return: The tenant_tags of this CertificateResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_tags

    @tenant_tags.setter
    def tenant_tags(self, tenant_tags):
        """Sets the tenant_tags of this CertificateResource.


        :param tenant_tags: The tenant_tags of this CertificateResource.  # noqa: E501
        :type: list[str]
        """

        self._tenant_tags = tenant_tags

    @property
    def certificate_data_format(self):
        """Gets the certificate_data_format of this CertificateResource.  # noqa: E501


        :return: The certificate_data_format of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._certificate_data_format

    @certificate_data_format.setter
    def certificate_data_format(self, certificate_data_format):
        """Sets the certificate_data_format of this CertificateResource.


        :param certificate_data_format: The certificate_data_format of this CertificateResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pkcs12", "Der", "Pem", "Unknown"]  # noqa: E501
        if certificate_data_format not in allowed_values:
            raise ValueError(
                "Invalid value for `certificate_data_format` ({0}), must be one of {1}"  # noqa: E501
                .format(certificate_data_format, allowed_values)
            )

        self._certificate_data_format = certificate_data_format

    @property
    def archived(self):
        """Gets the archived of this CertificateResource.  # noqa: E501


        :return: The archived of this CertificateResource.  # noqa: E501
        :rtype: datetime
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this CertificateResource.


        :param archived: The archived of this CertificateResource.  # noqa: E501
        :type: datetime
        """

        self._archived = archived

    @property
    def replaced_by(self):
        """Gets the replaced_by of this CertificateResource.  # noqa: E501


        :return: The replaced_by of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._replaced_by

    @replaced_by.setter
    def replaced_by(self, replaced_by):
        """Sets the replaced_by of this CertificateResource.


        :param replaced_by: The replaced_by of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._replaced_by = replaced_by

    @property
    def subject_distinguished_name(self):
        """Gets the subject_distinguished_name of this CertificateResource.  # noqa: E501


        :return: The subject_distinguished_name of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._subject_distinguished_name

    @subject_distinguished_name.setter
    def subject_distinguished_name(self, subject_distinguished_name):
        """Sets the subject_distinguished_name of this CertificateResource.


        :param subject_distinguished_name: The subject_distinguished_name of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._subject_distinguished_name = subject_distinguished_name

    @property
    def subject_common_name(self):
        """Gets the subject_common_name of this CertificateResource.  # noqa: E501


        :return: The subject_common_name of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._subject_common_name

    @subject_common_name.setter
    def subject_common_name(self, subject_common_name):
        """Sets the subject_common_name of this CertificateResource.


        :param subject_common_name: The subject_common_name of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._subject_common_name = subject_common_name

    @property
    def subject_organization(self):
        """Gets the subject_organization of this CertificateResource.  # noqa: E501


        :return: The subject_organization of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._subject_organization

    @subject_organization.setter
    def subject_organization(self, subject_organization):
        """Sets the subject_organization of this CertificateResource.


        :param subject_organization: The subject_organization of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._subject_organization = subject_organization

    @property
    def issuer_distinguished_name(self):
        """Gets the issuer_distinguished_name of this CertificateResource.  # noqa: E501


        :return: The issuer_distinguished_name of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._issuer_distinguished_name

    @issuer_distinguished_name.setter
    def issuer_distinguished_name(self, issuer_distinguished_name):
        """Sets the issuer_distinguished_name of this CertificateResource.


        :param issuer_distinguished_name: The issuer_distinguished_name of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._issuer_distinguished_name = issuer_distinguished_name

    @property
    def issuer_common_name(self):
        """Gets the issuer_common_name of this CertificateResource.  # noqa: E501


        :return: The issuer_common_name of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._issuer_common_name

    @issuer_common_name.setter
    def issuer_common_name(self, issuer_common_name):
        """Sets the issuer_common_name of this CertificateResource.


        :param issuer_common_name: The issuer_common_name of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._issuer_common_name = issuer_common_name

    @property
    def issuer_organization(self):
        """Gets the issuer_organization of this CertificateResource.  # noqa: E501


        :return: The issuer_organization of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._issuer_organization

    @issuer_organization.setter
    def issuer_organization(self, issuer_organization):
        """Sets the issuer_organization of this CertificateResource.


        :param issuer_organization: The issuer_organization of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._issuer_organization = issuer_organization

    @property
    def self_signed(self):
        """Gets the self_signed of this CertificateResource.  # noqa: E501


        :return: The self_signed of this CertificateResource.  # noqa: E501
        :rtype: bool
        """
        return self._self_signed

    @self_signed.setter
    def self_signed(self, self_signed):
        """Sets the self_signed of this CertificateResource.


        :param self_signed: The self_signed of this CertificateResource.  # noqa: E501
        :type: bool
        """

        self._self_signed = self_signed

    @property
    def thumbprint(self):
        """Gets the thumbprint of this CertificateResource.  # noqa: E501


        :return: The thumbprint of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this CertificateResource.


        :param thumbprint: The thumbprint of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._thumbprint = thumbprint

    @property
    def not_after(self):
        """Gets the not_after of this CertificateResource.  # noqa: E501


        :return: The not_after of this CertificateResource.  # noqa: E501
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this CertificateResource.


        :param not_after: The not_after of this CertificateResource.  # noqa: E501
        :type: datetime
        """

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this CertificateResource.  # noqa: E501


        :return: The not_before of this CertificateResource.  # noqa: E501
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this CertificateResource.


        :param not_before: The not_before of this CertificateResource.  # noqa: E501
        :type: datetime
        """

        self._not_before = not_before

    @property
    def is_expired(self):
        """Gets the is_expired of this CertificateResource.  # noqa: E501


        :return: The is_expired of this CertificateResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_expired

    @is_expired.setter
    def is_expired(self, is_expired):
        """Sets the is_expired of this CertificateResource.


        :param is_expired: The is_expired of this CertificateResource.  # noqa: E501
        :type: bool
        """

        self._is_expired = is_expired

    @property
    def has_private_key(self):
        """Gets the has_private_key of this CertificateResource.  # noqa: E501


        :return: The has_private_key of this CertificateResource.  # noqa: E501
        :rtype: bool
        """
        return self._has_private_key

    @has_private_key.setter
    def has_private_key(self, has_private_key):
        """Sets the has_private_key of this CertificateResource.


        :param has_private_key: The has_private_key of this CertificateResource.  # noqa: E501
        :type: bool
        """

        self._has_private_key = has_private_key

    @property
    def version(self):
        """Gets the version of this CertificateResource.  # noqa: E501


        :return: The version of this CertificateResource.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CertificateResource.


        :param version: The version of this CertificateResource.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def serial_number(self):
        """Gets the serial_number of this CertificateResource.  # noqa: E501


        :return: The serial_number of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CertificateResource.


        :param serial_number: The serial_number of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def signature_algorithm_name(self):
        """Gets the signature_algorithm_name of this CertificateResource.  # noqa: E501


        :return: The signature_algorithm_name of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._signature_algorithm_name

    @signature_algorithm_name.setter
    def signature_algorithm_name(self, signature_algorithm_name):
        """Sets the signature_algorithm_name of this CertificateResource.


        :param signature_algorithm_name: The signature_algorithm_name of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._signature_algorithm_name = signature_algorithm_name

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this CertificateResource.  # noqa: E501


        :return: The subject_alternative_names of this CertificateResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this CertificateResource.


        :param subject_alternative_names: The subject_alternative_names of this CertificateResource.  # noqa: E501
        :type: list[str]
        """

        self._subject_alternative_names = subject_alternative_names

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this CertificateResource.  # noqa: E501


        :return: The certificate_chain of this CertificateResource.  # noqa: E501
        :rtype: list[X509Certificate]
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this CertificateResource.


        :param certificate_chain: The certificate_chain of this CertificateResource.  # noqa: E501
        :type: list[X509Certificate]
        """

        self._certificate_chain = certificate_chain

    @property
    def space_id(self):
        """Gets the space_id of this CertificateResource.  # noqa: E501


        :return: The space_id of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this CertificateResource.


        :param space_id: The space_id of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this CertificateResource.  # noqa: E501


        :return: The last_modified_on of this CertificateResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this CertificateResource.


        :param last_modified_on: The last_modified_on of this CertificateResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this CertificateResource.  # noqa: E501


        :return: The last_modified_by of this CertificateResource.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this CertificateResource.


        :param last_modified_by: The last_modified_by of this CertificateResource.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def links(self):
        """Gets the links of this CertificateResource.  # noqa: E501


        :return: The links of this CertificateResource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CertificateResource.


        :param links: The links of this CertificateResource.  # noqa: E501
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
        if issubclass(CertificateResource, dict):
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
        if not isinstance(other, CertificateResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
