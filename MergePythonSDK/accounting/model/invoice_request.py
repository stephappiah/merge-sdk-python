"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

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
    from MergePythonSDK.accounting.model.currency_enum import CurrencyEnum
    from MergePythonSDK.accounting.model.invoice_type_enum import InvoiceTypeEnum
    globals()['CurrencyEnum'] = CurrencyEnum
    globals()['InvoiceTypeEnum'] = InvoiceTypeEnum

class InvoiceRequest(ModelNormal):
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
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'type': (InvoiceTypeEnum, str, none_type,),
            'contact': (str, none_type, none_type,),  # noqa: E501
            'number': (str, none_type, none_type,),  # noqa: E501
            'issue_date': (datetime, none_type, none_type,),  # noqa: E501
            'due_date': (datetime, none_type, none_type,),  # noqa: E501
            'paid_on_date': (datetime, none_type, none_type,),  # noqa: E501
            'memo': (str, none_type, none_type,),  # noqa: E501
            'currency': (CurrencyEnum, str, none_type,),
            'total_discount': (float, none_type, none_type,),  # noqa: E501
            'sub_total': (float, none_type, none_type,),  # noqa: E501
            'total_tax_amount': (float, none_type, none_type,),  # noqa: E501
            'total_amount': (float, none_type, none_type,),  # noqa: E501
            'balance': (float, none_type, none_type,),  # noqa: E501
            'remote_updated_at': (datetime, none_type, none_type,),  # noqa: E501
            'payments': ([str, none_type], none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'remote_id': 'remote_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'number': 'number',  # noqa: E501
        'issue_date': 'issue_date',  # noqa: E501
        'due_date': 'due_date',  # noqa: E501
        'paid_on_date': 'paid_on_date',  # noqa: E501
        'memo': 'memo',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'total_discount': 'total_discount',  # noqa: E501
        'sub_total': 'sub_total',  # noqa: E501
        'total_tax_amount': 'total_tax_amount',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'balance': 'balance',  # noqa: E501
        'remote_updated_at': 'remote_updated_at',  # noqa: E501
        'payments': 'payments',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """InvoiceRequest - a model defined in OpenAPI

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
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            type (bool, dict, float, int, list, str, none_type): The invoice's type.. [optional]  # noqa: E501
            contact (str, none_type): [optional]  # noqa: E501
            number (str, none_type): The invoice's number.. [optional]  # noqa: E501
            issue_date (datetime, none_type): The invoice's issue date.. [optional]  # noqa: E501
            due_date (datetime, none_type): The invoice's due date.. [optional]  # noqa: E501
            paid_on_date (datetime, none_type): The invoice's paid date.. [optional]  # noqa: E501
            memo (str, none_type): The invoice's private note.. [optional]  # noqa: E501
            currency (bool, dict, float, int, list, str, none_type): The invoice's currency.. [optional]  # noqa: E501
            total_discount (float, none_type): The invoice's total discount.. [optional]  # noqa: E501
            sub_total (float, none_type): The invoice's sub-total.. [optional]  # noqa: E501
            total_tax_amount (float, none_type): The invoice's total tax amount.. [optional]  # noqa: E501
            total_amount (float, none_type): The invoice's total amount.. [optional]  # noqa: E501
            balance (float, none_type): The invoice's remaining balance.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's invoice entry was updated.. [optional]  # noqa: E501
            payments ([str, none_type]): Array of `Payment` object IDs.. [optional]  # noqa: E501
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
        self.type = kwargs.get("type", None)
        self.contact = kwargs.get("contact", None)
        self.number = kwargs.get("number", None)
        self.issue_date = kwargs.get("issue_date", None)
        self.due_date = kwargs.get("due_date", None)
        self.paid_on_date = kwargs.get("paid_on_date", None)
        self.memo = kwargs.get("memo", None)
        self.currency = kwargs.get("currency", None)
        self.total_discount = kwargs.get("total_discount", None)
        self.sub_total = kwargs.get("sub_total", None)
        self.total_tax_amount = kwargs.get("total_tax_amount", None)
        self.total_amount = kwargs.get("total_amount", None)
        self.balance = kwargs.get("balance", None)
        self.remote_updated_at = kwargs.get("remote_updated_at", None)
        self.payments = kwargs.get("payments", None)
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
        """InvoiceRequest - a model defined in OpenAPI

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
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            type (bool, dict, float, int, list, str, none_type): The invoice's type.. [optional]  # noqa: E501
            contact (str, none_type): [optional]  # noqa: E501
            number (str, none_type): The invoice's number.. [optional]  # noqa: E501
            issue_date (datetime, none_type): The invoice's issue date.. [optional]  # noqa: E501
            due_date (datetime, none_type): The invoice's due date.. [optional]  # noqa: E501
            paid_on_date (datetime, none_type): The invoice's paid date.. [optional]  # noqa: E501
            memo (str, none_type): The invoice's private note.. [optional]  # noqa: E501
            currency (bool, dict, float, int, list, str, none_type): The invoice's currency.. [optional]  # noqa: E501
            total_discount (float, none_type): The invoice's total discount.. [optional]  # noqa: E501
            sub_total (float, none_type): The invoice's sub-total.. [optional]  # noqa: E501
            total_tax_amount (float, none_type): The invoice's total tax amount.. [optional]  # noqa: E501
            total_amount (float, none_type): The invoice's total amount.. [optional]  # noqa: E501
            balance (float, none_type): The invoice's remaining balance.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's invoice entry was updated.. [optional]  # noqa: E501
            payments ([str, none_type]): Array of `Payment` object IDs.. [optional]  # noqa: E501
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
        self.type: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("type", None)
        self.contact: Union[str, none_type] = kwargs.get("contact", None)
        self.number: Union[str, none_type] = kwargs.get("number", None)
        self.issue_date: Union[datetime, none_type] = kwargs.get("issue_date", None)
        self.due_date: Union[datetime, none_type] = kwargs.get("due_date", None)
        self.paid_on_date: Union[datetime, none_type] = kwargs.get("paid_on_date", None)
        self.memo: Union[str, none_type] = kwargs.get("memo", None)
        self.currency: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("currency", None)
        self.total_discount: Union[float, none_type] = kwargs.get("total_discount", None)
        self.sub_total: Union[float, none_type] = kwargs.get("sub_total", None)
        self.total_tax_amount: Union[float, none_type] = kwargs.get("total_tax_amount", None)
        self.total_amount: Union[float, none_type] = kwargs.get("total_amount", None)
        self.balance: Union[float, none_type] = kwargs.get("balance", None)
        self.remote_updated_at: Union[datetime, none_type] = kwargs.get("remote_updated_at", None)
        self.payments: Union[List[str, none_type]] = kwargs.get("payments", list())


