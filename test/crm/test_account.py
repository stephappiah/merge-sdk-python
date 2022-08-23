"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.crm
from MergePythonSDK.crm.model.address import Address
from MergePythonSDK.crm.model.phone_number import PhoneNumber
from MergePythonSDK.crm.model.remote_data import RemoteData
globals()['Address'] = Address
globals()['PhoneNumber'] = PhoneNumber
globals()['RemoteData'] = RemoteData
from MergePythonSDK.crm.model.account import Account
from MergePythonSDK.shared.api_client import ApiClient


class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccount(self):
        """Test Account"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Account()  # noqa: E501

        """
        No test json responses were defined for Account
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Account,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
