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
from MergePythonSDK.hris.model.earning_type_enum import EarningTypeEnum
globals()['EarningTypeEnum'] = EarningTypeEnum
from MergePythonSDK.hris.model.earning import Earning
from MergePythonSDK.shared.api_client import ApiClient


class TestEarning(unittest.TestCase):
    """Earning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEarning(self):
        """Test Earning"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Earning()  # noqa: E501

        """
        No test json responses were defined for Earning
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Earning,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
