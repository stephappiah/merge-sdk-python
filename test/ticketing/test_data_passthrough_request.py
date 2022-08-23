"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.model.method_enum import MethodEnum
from MergePythonSDK.ticketing.model.multipart_form_field_request import MultipartFormFieldRequest
from MergePythonSDK.ticketing.model.request_format_enum import RequestFormatEnum
globals()['MethodEnum'] = MethodEnum
globals()['MultipartFormFieldRequest'] = MultipartFormFieldRequest
globals()['RequestFormatEnum'] = RequestFormatEnum
from MergePythonSDK.ticketing.model.data_passthrough_request import DataPassthroughRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestDataPassthroughRequest(unittest.TestCase):
    """DataPassthroughRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataPassthroughRequest(self):
        """Test DataPassthroughRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DataPassthroughRequest()  # noqa: E501

        """
        No test json responses were defined for DataPassthroughRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (DataPassthroughRequest,), False)

        assert deserialized is not None

        assert deserialized.method is not None
        assert deserialized.path is not None


if __name__ == '__main__':
    unittest.main()
