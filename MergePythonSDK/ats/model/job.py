"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from typing import (
    Optional,
    Union,
    List,
    Dict,
)

from MergePythonSDK.shared.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    OpenApiModel,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from MergePythonSDK.shared.exceptions import ApiAttributeError
from MergePythonSDK.shared.model_utils import import_model_by_name


def lazy_import():
    from MergePythonSDK.ats.model.job_status_enum import JobStatusEnum
    from MergePythonSDK.shared.model.remote_data import RemoteData
    from MergePythonSDK.ats.model.url import Url
    globals()['JobStatusEnum'] = JobStatusEnum
    globals()['RemoteData'] = RemoteData
    globals()['Url'] = Url

class Job(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()

        defined_types = {
            'id': (str, none_type,),  # noqa: E501
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'name': (str, none_type, none_type,),  # noqa: E501
            'description': (str, none_type, none_type,),  # noqa: E501
            'code': (str, none_type, none_type,),  # noqa: E501
            'status': (JobStatusEnum, str, none_type,),
            'job_posting_urls': ([Url], none_type,),  # noqa: E501
            'remote_created_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_updated_at': (datetime, none_type, none_type,),  # noqa: E501
            'confidential': (bool, none_type, none_type,),  # noqa: E501
            'departments': ([str, none_type], none_type,),  # noqa: E501
            'offices': ([str, none_type], none_type,),  # noqa: E501
            'hiring_managers': ([str, none_type], none_type,),  # noqa: E501
            'recruiters': ([str, none_type], none_type,),  # noqa: E501
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
        }
        expands_types = {"departments": "Department", "hiring_managers": "RemoteUser", "offices": "Office", "recruiters": "RemoteUser"}

        # update types with expands
        for key, val in expands_types.items():
            if key in defined_types.keys():
                expands_model = import_model_by_name(val, "ats")
                if len(defined_types[key]) > 0 and isinstance(defined_types[key][0], list):
                    defined_types[key][0].insert(0, expands_model)
                defined_types[key] = (*defined_types[key], expands_model)
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'remote_id': 'remote_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'code': 'code',  # noqa: E501
        'status': 'status',  # noqa: E501
        'job_posting_urls': 'job_posting_urls',  # noqa: E501
        'remote_created_at': 'remote_created_at',  # noqa: E501
        'remote_updated_at': 'remote_updated_at',  # noqa: E501
        'confidential': 'confidential',  # noqa: E501
        'departments': 'departments',  # noqa: E501
        'offices': 'offices',  # noqa: E501
        'hiring_managers': 'hiring_managers',  # noqa: E501
        'recruiters': 'recruiters',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'remote_data',  # noqa: E501
        'remote_was_deleted',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Job - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            name (str, none_type): The job's name.. [optional]  # noqa: E501
            description (str, none_type): The job's description.. [optional]  # noqa: E501
            code (str, none_type): The job's code. Typically an additional identifier used to reference the particular job that is displayed on the ATS.. [optional]  # noqa: E501
            status (bool, date, datetime, dict, float, int, list, str, none_type): The job's status.. [optional]  # noqa: E501
            job_posting_urls ([Url]): [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's job was created.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's job was updated.. [optional]  # noqa: E501
            confidential (bool, none_type): Whether the job is confidential.. [optional]  # noqa: E501
            departments ([str, none_type]): IDs of `Department` objects for this `Job`.. [optional]  # noqa: E501
            offices ([str, none_type]): IDs of `Office` objects for this `Job`.. [optional]  # noqa: E501
            hiring_managers ([str, none_type]): IDs of `RemoteUser` objects that serve as hiring managers for this `Job`.. [optional]  # noqa: E501
            recruiters ([str, none_type]): IDs of `RemoteUser` objects that serve as recruiters for this `Job`.. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)


        self.remote_id = kwargs.get("remote_id", None)
        self.name = kwargs.get("name", None)
        self.description = kwargs.get("description", None)
        self.code = kwargs.get("code", None)
        self.status = kwargs.get("status", None)
        self.job_posting_urls = kwargs.get("job_posting_urls", None)
        self.remote_created_at = kwargs.get("remote_created_at", None)
        self.remote_updated_at = kwargs.get("remote_updated_at", None)
        self.confidential = kwargs.get("confidential", None)
        self.departments = kwargs.get("departments", None)
        self.offices = kwargs.get("offices", None)
        self.hiring_managers = kwargs.get("hiring_managers", None)
        self.recruiters = kwargs.get("recruiters", None)

        # Read only properties
        self._id = kwargs.get("id", str())
        self._remote_data = kwargs.get("remote_data", None)
        self._remote_was_deleted = kwargs.get("remote_was_deleted", bool())
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Job - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            name (str, none_type): The job's name.. [optional]  # noqa: E501
            description (str, none_type): The job's description.. [optional]  # noqa: E501
            code (str, none_type): The job's code. Typically an additional identifier used to reference the particular job that is displayed on the ATS.. [optional]  # noqa: E501
            status (bool, date, datetime, dict, float, int, list, str, none_type): The job's status.. [optional]  # noqa: E501
            job_posting_urls ([Url]): [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's job was created.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's job was updated.. [optional]  # noqa: E501
            confidential (bool, none_type): Whether the job is confidential.. [optional]  # noqa: E501
            departments ([str, none_type]): IDs of `Department` objects for this `Job`.. [optional]  # noqa: E501
            offices ([str, none_type]): IDs of `Office` objects for this `Job`.. [optional]  # noqa: E501
            hiring_managers ([str, none_type]): IDs of `RemoteUser` objects that serve as hiring managers for this `Job`.. [optional]  # noqa: E501
            recruiters ([str, none_type]): IDs of `RemoteUser` objects that serve as recruiters for this `Job`.. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.remote_id: Union[str, none_type] = kwargs.get("remote_id", None)
        self.name: Union[str, none_type] = kwargs.get("name", None)
        self.description: Union[str, none_type] = kwargs.get("description", None)
        self.code: Union[str, none_type] = kwargs.get("code", None)
        self.status: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("status", None)
        self.job_posting_urls: Union[List["Url"]] = kwargs.get("job_posting_urls", None)
        self.remote_created_at: Union[datetime, none_type] = kwargs.get("remote_created_at", None)
        self.remote_updated_at: Union[datetime, none_type] = kwargs.get("remote_updated_at", None)
        self.confidential: Union[bool, none_type] = kwargs.get("confidential", None)
        self.departments: Union[List[str, none_type]] = kwargs.get("departments", list())
        self.offices: Union[List[str, none_type]] = kwargs.get("offices", list())
        self.hiring_managers: Union[List[str, none_type]] = kwargs.get("hiring_managers", list())
        self.recruiters: Union[List[str, none_type]] = kwargs.get("recruiters", list())

        # Read only properties
        self._id: Union[str] = kwargs.get("id", str())
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)
        self._remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())

    # Read only property getters
    @property
    def id(self):
        return self._id

    @property
    def remote_data(self):
        return self._remote_data

    @property
    def remote_was_deleted(self):
        return self._remote_was_deleted



