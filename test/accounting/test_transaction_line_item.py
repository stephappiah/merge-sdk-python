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
from MergePythonSDK.accounting.model.transaction_line_item import TransactionLineItem
from MergePythonSDK.shared.api_client import ApiClient


class TestTransactionLineItem(unittest.TestCase):
    """TransactionLineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionLineItem(self):
        """Test TransactionLineItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionLineItem()  # noqa: E501

        """
        No test json responses were defined for TransactionLineItem
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (TransactionLineItem,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
