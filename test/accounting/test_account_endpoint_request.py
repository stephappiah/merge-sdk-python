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
from MergePythonSDK.accounting.model.account_request import AccountRequest
globals()['AccountRequest'] = AccountRequest
from MergePythonSDK.accounting.model.account_endpoint_request import AccountEndpointRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestAccountEndpointRequest(unittest.TestCase):
    """AccountEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountEndpointRequest(self):
        """Test AccountEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for AccountEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AccountEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()