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
from MergePythonSDK.ticketing.model.linked_account_status import LinkedAccountStatus
from MergePythonSDK.shared.api_client import ApiClient


class TestLinkedAccountStatus(unittest.TestCase):
    """LinkedAccountStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLinkedAccountStatus(self):
        """Test LinkedAccountStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LinkedAccountStatus()  # noqa: E501

        """
        No test json responses were defined for LinkedAccountStatus
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (LinkedAccountStatus,), False)

        assert deserialized is not None

        assert deserialized.linked_account_status is not None
        assert deserialized.can_make_request is not None


if __name__ == '__main__':
    unittest.main()
