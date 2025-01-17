"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

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
    from MergePythonSDK.ticketing.model.priority_enum import PriorityEnum
    from MergePythonSDK.shared.model.remote_data import RemoteData
    from MergePythonSDK.ticketing.model.ticket_status_enum import TicketStatusEnum
    globals()['PriorityEnum'] = PriorityEnum
    globals()['RemoteData'] = RemoteData
    globals()['TicketStatusEnum'] = TicketStatusEnum

class Ticket(ModelNormal):
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
        ('ticket_url',): {
            'max_length': 2000,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'assignees': ([str, none_type], none_type,),  # noqa: E501
            'creator': (str, none_type, none_type,),  # noqa: E501
            'due_date': (datetime, none_type, none_type,),  # noqa: E501
            'status': (TicketStatusEnum, str, none_type,),
            'description': (str, none_type, none_type,),  # noqa: E501
            'project': (str, none_type, none_type,),  # noqa: E501
            'ticket_type': (str, none_type, none_type,),  # noqa: E501
            'account': (str, none_type, none_type,),  # noqa: E501
            'contact': (str, none_type, none_type,),  # noqa: E501
            'parent_ticket': (str, none_type, none_type,),  # noqa: E501
            'attachments': ([str, none_type], none_type,),  # noqa: E501
            'tags': ([str], none_type,),  # noqa: E501
            'remote_created_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_updated_at': (datetime, none_type, none_type,),  # noqa: E501
            'completed_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
            'ticket_url': (str, none_type, none_type,),  # noqa: E501
            'priority': (PriorityEnum, str, none_type,),
        }
        expands_types = {"account": "Account", "assignees": "User", "attachments": "Attachment", "contact": "Contact", "creator": "User", "parent_ticket": "Ticket", "project": "Project"}

        # update types with expands
        for key, val in expands_types.items():
            if key in defined_types.keys():
                expands_model = import_model_by_name(val, "ticketing")
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
        'assignees': 'assignees',  # noqa: E501
        'creator': 'creator',  # noqa: E501
        'due_date': 'due_date',  # noqa: E501
        'status': 'status',  # noqa: E501
        'description': 'description',  # noqa: E501
        'project': 'project',  # noqa: E501
        'ticket_type': 'ticket_type',  # noqa: E501
        'account': 'account',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'parent_ticket': 'parent_ticket',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'remote_created_at': 'remote_created_at',  # noqa: E501
        'remote_updated_at': 'remote_updated_at',  # noqa: E501
        'completed_at': 'completed_at',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
        'ticket_url': 'ticket_url',  # noqa: E501
        'priority': 'priority',  # noqa: E501
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
        """Ticket - a model defined in OpenAPI

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
            name (str, none_type): The ticket's name.. [optional]  # noqa: E501
            assignees ([str, none_type]): [optional]  # noqa: E501
            creator (str, none_type): [optional]  # noqa: E501
            due_date (datetime, none_type): The ticket's due date.. [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The current status of the ticket.. [optional]  # noqa: E501
            description (str, none_type): The ticket’s description. HTML version of description is mapped if supported by the third-party platform.. [optional]  # noqa: E501
            project (str, none_type): [optional]  # noqa: E501
            ticket_type (str, none_type): The ticket's type.. [optional]  # noqa: E501
            account (str, none_type): [optional]  # noqa: E501
            contact (str, none_type): [optional]  # noqa: E501
            parent_ticket (str, none_type): [optional]  # noqa: E501
            attachments ([str, none_type]): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's ticket was created.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's ticket was updated.. [optional]  # noqa: E501
            completed_at (datetime, none_type): When the ticket was completed.. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_was_deleted (bool): [optional]  # noqa: E501
            ticket_url (str, none_type): The 3rd party url of the Ticket.. [optional]  # noqa: E501
            priority (bool, dict, float, int, list, str, none_type): The priority or urgency of the Ticket. Possible values include: URGENT, HIGH, NORMAL, LOW - in cases where there is no clear mapping - the original value passed through.. [optional]  # noqa: E501
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
        self.assignees = kwargs.get("assignees", None)
        self.creator = kwargs.get("creator", None)
        self.due_date = kwargs.get("due_date", None)
        self.status = kwargs.get("status", None)
        self.description = kwargs.get("description", None)
        self.project = kwargs.get("project", None)
        self.ticket_type = kwargs.get("ticket_type", None)
        self.account = kwargs.get("account", None)
        self.contact = kwargs.get("contact", None)
        self.parent_ticket = kwargs.get("parent_ticket", None)
        self.attachments = kwargs.get("attachments", None)
        self.tags = kwargs.get("tags", None)
        self.remote_created_at = kwargs.get("remote_created_at", None)
        self.remote_updated_at = kwargs.get("remote_updated_at", None)
        self.completed_at = kwargs.get("completed_at", None)
        self.ticket_url = kwargs.get("ticket_url", None)
        self.priority = kwargs.get("priority", None)

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
        """Ticket - a model defined in OpenAPI

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
            name (str, none_type): The ticket's name.. [optional]  # noqa: E501
            assignees ([str, none_type]): [optional]  # noqa: E501
            creator (str, none_type): [optional]  # noqa: E501
            due_date (datetime, none_type): The ticket's due date.. [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The current status of the ticket.. [optional]  # noqa: E501
            description (str, none_type): The ticket’s description. HTML version of description is mapped if supported by the third-party platform.. [optional]  # noqa: E501
            project (str, none_type): [optional]  # noqa: E501
            ticket_type (str, none_type): The ticket's type.. [optional]  # noqa: E501
            account (str, none_type): [optional]  # noqa: E501
            contact (str, none_type): [optional]  # noqa: E501
            parent_ticket (str, none_type): [optional]  # noqa: E501
            attachments ([str, none_type]): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's ticket was created.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's ticket was updated.. [optional]  # noqa: E501
            completed_at (datetime, none_type): When the ticket was completed.. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_was_deleted (bool): [optional]  # noqa: E501
            ticket_url (str, none_type): The 3rd party url of the Ticket.. [optional]  # noqa: E501
            priority (bool, dict, float, int, list, str, none_type): The priority or urgency of the Ticket. Possible values include: URGENT, HIGH, NORMAL, LOW - in cases where there is no clear mapping - the original value passed through.. [optional]  # noqa: E501
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
        self.assignees: Union[List[str, none_type]] = kwargs.get("assignees", list())
        self.creator: Union[str, none_type] = kwargs.get("creator", None)
        self.due_date: Union[datetime, none_type] = kwargs.get("due_date", None)
        self.status: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("status", None)
        self.description: Union[str, none_type] = kwargs.get("description", None)
        self.project: Union[str, none_type] = kwargs.get("project", None)
        self.ticket_type: Union[str, none_type] = kwargs.get("ticket_type", None)
        self.account: Union[str, none_type] = kwargs.get("account", None)
        self.contact: Union[str, none_type] = kwargs.get("contact", None)
        self.parent_ticket: Union[str, none_type] = kwargs.get("parent_ticket", None)
        self.attachments: Union[List[str, none_type]] = kwargs.get("attachments", list())
        self.tags: Union[List[str]] = kwargs.get("tags", list())
        self.remote_created_at: Union[datetime, none_type] = kwargs.get("remote_created_at", None)
        self.remote_updated_at: Union[datetime, none_type] = kwargs.get("remote_updated_at", None)
        self.completed_at: Union[datetime, none_type] = kwargs.get("completed_at", None)
        self.ticket_url: Union[str, none_type] = kwargs.get("ticket_url", None)
        self.priority: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("priority", None)

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



