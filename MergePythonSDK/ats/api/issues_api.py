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
from MergePythonSDK.ats.model.issue import Issue
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse


class IssuesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.issues_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(Issue),),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/issues',
                'operation_id': 'issues_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_token',
                    'cursor',
                    'end_date',
                    'end_user_organization_name',
                    'first_incident_time_after',
                    'first_incident_time_before',
                    'include_muted',
                    'integration_name',
                    'last_incident_time_after',
                    'last_incident_time_before',
                    'page_size',
                    'start_date',
                    'status',
                ],
                'required': [],
                'nullable': [
                    'first_incident_time_after',
                    'first_incident_time_before',
                    'last_incident_time_after',
                    'last_incident_time_before',
                ],
                'enum': [
                    'status',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('status',): {

                        "ONGOING": "ONGOING",
                        "RESOLVED": "RESOLVED"
                    },
                },
                'openapi_types': {
                    'account_token':
                        (str,),
                    'cursor':
                        (str,),
                    'end_date':
                        (str,),
                    'end_user_organization_name':
                        (str,),
                    'first_incident_time_after':
                        (datetime, none_type,),
                    'first_incident_time_before':
                        (datetime, none_type,),
                    'include_muted':
                        (str,),
                    'integration_name':
                        (str,),
                    'last_incident_time_after':
                        (datetime, none_type,),
                    'last_incident_time_before':
                        (datetime, none_type,),
                    'page_size':
                        (int,),
                    'start_date':
                        (str,),
                    'status':
                        (str,),
                },
                'attribute_map': {
                    'account_token': 'account_token',
                    'cursor': 'cursor',
                    'end_date': 'end_date',
                    'end_user_organization_name': 'end_user_organization_name',
                    'first_incident_time_after': 'first_incident_time_after',
                    'first_incident_time_before': 'first_incident_time_before',
                    'include_muted': 'include_muted',
                    'integration_name': 'integration_name',
                    'last_incident_time_after': 'last_incident_time_after',
                    'last_incident_time_before': 'last_incident_time_before',
                    'page_size': 'page_size',
                    'start_date': 'start_date',
                    'status': 'status',
                },
                'location_map': {
                    'account_token': 'query',
                    'cursor': 'query',
                    'end_date': 'query',
                    'end_user_organization_name': 'query',
                    'first_incident_time_after': 'query',
                    'first_incident_time_before': 'query',
                    'include_muted': 'query',
                    'integration_name': 'query',
                    'last_incident_time_after': 'query',
                    'last_incident_time_before': 'query',
                    'page_size': 'query',
                    'start_date': 'query',
                    'status': 'query',
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
        self.issues_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (Issue,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/issues/{id}',
                'operation_id': 'issues_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
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

    def issues_list(
        self,
        **kwargs
    ):
        """issues_list  # noqa: E501

        Gets issues.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issues_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            account_token (str): [optional]
            cursor (str): The pagination cursor value.. [optional]
            end_date (str): If included, will only include issues whose most recent action occurred before this time. [optional]
            end_user_organization_name (str): [optional]
            first_incident_time_after (datetime, none_type): If provided, will only return issues whose first incident time was after this datetime.. [optional]
            first_incident_time_before (datetime, none_type): If provided, will only return issues whose first incident time was before this datetime.. [optional]
            include_muted (str): If True, will include muted issues. [optional]
            integration_name (str): [optional]
            last_incident_time_after (datetime, none_type): If provided, will only return issues whose first incident time was after this datetime.. [optional]
            last_incident_time_before (datetime, none_type): If provided, will only return issues whose first incident time was before this datetime.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            start_date (str): If included, will only include issues whose most recent action occurred after this time. [optional]
            status (str): [optional]
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
            MergePaginatedResponse(Issue)
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
        return self.issues_list_endpoint.call_with_http_info(**kwargs)

    def issues_retrieve(
        self,
        id,
        **kwargs
    ):
        """issues_retrieve  # noqa: E501

        Get a specific issue.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issues_retrieve(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

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
            Issue
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
        kwargs['id'] = \
            id
        return self.issues_retrieve_endpoint.call_with_http_info(**kwargs)

