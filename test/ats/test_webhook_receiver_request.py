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
from MergePythonSDK.ats.model.webhook_receiver_request import WebhookReceiverRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestWebhookReceiverRequest(unittest.TestCase):
    """WebhookReceiverRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookReceiverRequest(self):
        """Test WebhookReceiverRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookReceiverRequest()  # noqa: E501

        """
        No test json responses were defined for WebhookReceiverRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (WebhookReceiverRequest,), False)

        assert deserialized is not None

        assert deserialized.event is not None
        assert deserialized.is_active is not None


if __name__ == '__main__':
    unittest.main()
