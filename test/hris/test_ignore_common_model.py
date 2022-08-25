"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.hris
from MergePythonSDK.hris.model.reason_enum import ReasonEnum
globals()['ReasonEnum'] = ReasonEnum
from MergePythonSDK.hris.model.ignore_common_model import IgnoreCommonModel
from MergePythonSDK.shared.api_client import ApiClient


class TestIgnoreCommonModel(unittest.TestCase):
    """IgnoreCommonModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIgnoreCommonModel(self):
        """Test IgnoreCommonModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IgnoreCommonModel()  # noqa: E501

        """
        No test json responses were defined for IgnoreCommonModel
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (IgnoreCommonModel,), False)

        assert deserialized is not None

        assert deserialized.reason is not None


if __name__ == '__main__':
    unittest.main()
