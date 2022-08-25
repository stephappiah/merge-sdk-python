"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ats
from MergePythonSDK.ats.model.remote_key_for_regeneration_request import RemoteKeyForRegenerationRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestRemoteKeyForRegenerationRequest(unittest.TestCase):
    """RemoteKeyForRegenerationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemoteKeyForRegenerationRequest(self):
        """Test RemoteKeyForRegenerationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RemoteKeyForRegenerationRequest()  # noqa: E501

        """
        No test json responses were defined for RemoteKeyForRegenerationRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (RemoteKeyForRegenerationRequest,), False)

        assert deserialized is not None

        assert deserialized.name is not None


if __name__ == '__main__':
    unittest.main()
