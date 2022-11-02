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
from MergePythonSDK.shared.model.categories_enum import CategoriesEnum
globals()['CategoriesEnum'] = CategoriesEnum
from MergePythonSDK.ats.model.account_integration import AccountIntegration
from MergePythonSDK.shared.api_client import ApiClient


class TestAccountIntegration(unittest.TestCase):
    """AccountIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountIntegration(self):
        """Test AccountIntegration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountIntegration()  # noqa: E501

        """
        No test json responses were defined for AccountIntegration
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AccountIntegration,), False)

        assert deserialized is not None

        assert deserialized.name is not None


if __name__ == '__main__':
    unittest.main()
