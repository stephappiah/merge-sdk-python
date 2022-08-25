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
from MergePythonSDK.ticketing.model.model_operation import ModelOperation
from MergePythonSDK.shared.api_client import ApiClient


class TestModelOperation(unittest.TestCase):
    """ModelOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModelOperation(self):
        """Test ModelOperation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ModelOperation()  # noqa: E501

        """
        No test json responses were defined for ModelOperation
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ModelOperation,), False)

        assert deserialized is not None

        assert deserialized.model_name is not None
        assert deserialized.available_operations is not None
        assert deserialized.required_post_parameters is not None
        assert deserialized.supported_fields is not None


if __name__ == '__main__':
    unittest.main()
