"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.accounting
from MergePythonSDK.accounting.model.encoding_enum import EncodingEnum
globals()['EncodingEnum'] = EncodingEnum
from MergePythonSDK.accounting.model.multipart_form_field_request import MultipartFormFieldRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestMultipartFormFieldRequest(unittest.TestCase):
    """MultipartFormFieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMultipartFormFieldRequest(self):
        """Test MultipartFormFieldRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MultipartFormFieldRequest()  # noqa: E501

        """
        No test json responses were defined for MultipartFormFieldRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (MultipartFormFieldRequest,), False)

        assert deserialized is not None

        assert deserialized.name is not None
        assert deserialized.data is not None


if __name__ == '__main__':
    unittest.main()
