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
from MergePythonSDK.accounting.model.currency_enum import CurrencyEnum
from MergePythonSDK.accounting.model.purchase_order_status_enum import PurchaseOrderStatusEnum
globals()['CurrencyEnum'] = CurrencyEnum
globals()['PurchaseOrderStatusEnum'] = PurchaseOrderStatusEnum
from MergePythonSDK.accounting.model.purchase_order_request import PurchaseOrderRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestPurchaseOrderRequest(unittest.TestCase):
    """PurchaseOrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPurchaseOrderRequest(self):
        """Test PurchaseOrderRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PurchaseOrderRequest()  # noqa: E501

        """
        No test json responses were defined for PurchaseOrderRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PurchaseOrderRequest,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
