"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergePythonSDK.shared.api_client import ApiClient, Endpoint as _Endpoint
from MergePythonSDK.shared.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergePythonSDK.ats.model.attachment import Attachment
from MergePythonSDK.ats.model.attachment_endpoint_request import AttachmentEndpointRequest
from MergePythonSDK.ats.model.attachment_response import AttachmentResponse
from MergePythonSDK.ats.model.meta_response import MetaResponse
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse


class AttachmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.attachments_create_endpoint = _Endpoint(
            settings={
                'response_type': (AttachmentResponse,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/attachments',
                'operation_id': 'attachments_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'attachment_endpoint_request',
                    'is_debug_mode',
                    'run_async',
                ],
                'required': [
                    'x_account_token',
                    'attachment_endpoint_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'attachment_endpoint_request':
                        (AttachmentEndpointRequest,),
                    'is_debug_mode':
                        (bool,),
                    'run_async':
                        (bool,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'is_debug_mode': 'is_debug_mode',
                    'run_async': 'run_async',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'attachment_endpoint_request': 'body',
                    'is_debug_mode': 'query',
                    'run_async': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.attachments_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(Attachment),),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/attachments',
                'operation_id': 'attachments_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'candidate_id',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'page_size',
                    'remote_fields',
                    'remote_id',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'remote_id',
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CANDIDATE": "candidate"
                    },
                    ('remote_fields',): {

                        "ATTACHMENT_TYPE": "attachment_type"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'candidate_id':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'expand':
                        (str,),
                    'include_deleted_data':
                        (bool,),
                    'include_remote_data':
                        (bool,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'page_size':
                        (int,),
                    'remote_fields':
                        (str,),
                    'remote_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'candidate_id': 'candidate_id',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_fields': 'remote_fields',
                    'remote_id': 'remote_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'candidate_id': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'page_size': 'query',
                    'remote_fields': 'query',
                    'remote_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.attachments_meta_post_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (MetaResponse,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/attachments/meta/post',
                'operation_id': 'attachments_meta_post_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                },
                'location_map': {
                    'x_account_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.attachments_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (Attachment,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/attachments/{id}',
                'operation_id': 'attachments_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                    'include_remote_data',
                    'remote_fields',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CANDIDATE": "candidate"
                    },
                    ('remote_fields',): {

                        "ATTACHMENT_TYPE": "attachment_type"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'expand':
                        (str,),
                    'include_remote_data':
                        (bool,),
                    'remote_fields':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                    'remote_fields': 'remote_fields',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
                    'include_remote_data': 'query',
                    'remote_fields': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def attachments_create(
        self,
        x_account_token,
        attachment_endpoint_request,
        **kwargs
    ):
        """attachments_create  # noqa: E501

        Creates an `Attachment` object with the given values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.attachments_create(x_account_token, attachment_endpoint_request, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.
            attachment_endpoint_request (AttachmentEndpointRequest):

        Keyword Args:
            is_debug_mode (bool): Whether to include debug fields (such as log file links) in the response.. [optional]
            run_async (bool): Whether or not third-party updates should be run asynchronously.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            AttachmentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_account_token'] = \
            x_account_token
        kwargs['attachment_endpoint_request'] = \
            attachment_endpoint_request
        return self.attachments_create_endpoint.call_with_http_info(**kwargs)

    def attachments_list(
        self,
        x_account_token,
        **kwargs
    ):
        """attachments_list  # noqa: E501

        Returns a list of `Attachment` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.attachments_list(x_account_token, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.

        Keyword Args:
            candidate_id (str): If provided, will only return attachments for this candidate.. [optional]
            created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
            created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
            cursor (str): The pagination cursor value.. [optional]
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "candidate"
            include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            modified_after (datetime): If provided, will only return objects modified after this datetime.. [optional]
            modified_before (datetime): If provided, will only return objects modified before this datetime.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            remote_fields (str): Which fields should be returned in non-normalized form.. [optional] if omitted the server will use the default value of "attachment_type"
            remote_id (str, none_type): The API provider's ID for the given object.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MergePaginatedResponse(Attachment)
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_account_token'] = \
            x_account_token
        return self.attachments_list_endpoint.call_with_http_info(**kwargs)

    def attachments_meta_post_retrieve(
        self,
        x_account_token,
        **kwargs
    ):
        """attachments_meta_post_retrieve  # noqa: E501

        Returns metadata for `Attachment` POSTs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.attachments_meta_post_retrieve(x_account_token, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MetaResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_account_token'] = \
            x_account_token
        return self.attachments_meta_post_retrieve_endpoint.call_with_http_info(**kwargs)

    def attachments_retrieve(
        self,
        x_account_token,
        id,
        **kwargs
    ):
        """attachments_retrieve  # noqa: E501

        Returns an `Attachment` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.attachments_retrieve(x_account_token, id, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.
            id (str):

        Keyword Args:
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "candidate"
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            remote_fields (str): Which fields should be returned in non-normalized form.. [optional] if omitted the server will use the default value of "attachment_type"
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Attachment
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_account_token'] = \
            x_account_token
        kwargs['id'] = \
            id
        return self.attachments_retrieve_endpoint.call_with_http_info(**kwargs)

