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
from MergePythonSDK.hris.model.linked_account_selective_sync_configuration_request import LinkedAccountSelectiveSyncConfigurationRequest
globals()['LinkedAccountSelectiveSyncConfigurationRequest'] = LinkedAccountSelectiveSyncConfigurationRequest
from MergePythonSDK.hris.model.linked_account_selective_sync_configuration_list_request import LinkedAccountSelectiveSyncConfigurationListRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestLinkedAccountSelectiveSyncConfigurationListRequest(unittest.TestCase):
    """LinkedAccountSelectiveSyncConfigurationListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLinkedAccountSelectiveSyncConfigurationListRequest(self):
        """Test LinkedAccountSelectiveSyncConfigurationListRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LinkedAccountSelectiveSyncConfigurationListRequest()  # noqa: E501

        """
        No test json responses were defined for LinkedAccountSelectiveSyncConfigurationListRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (LinkedAccountSelectiveSyncConfigurationListRequest,), False)

        assert deserialized is not None

        assert deserialized.sync_configurations is not None


if __name__ == '__main__':
    unittest.main()
