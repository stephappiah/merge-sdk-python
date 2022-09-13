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
from MergePythonSDK.accounting.model.remote_data import RemoteData
from MergePythonSDK.accounting.model.report_item import ReportItem
globals()['CurrencyEnum'] = CurrencyEnum
globals()['RemoteData'] = RemoteData
globals()['ReportItem'] = ReportItem
from MergePythonSDK.accounting.model.cash_flow_statement import CashFlowStatement
from MergePythonSDK.shared.api_client import ApiClient


class TestCashFlowStatement(unittest.TestCase):
    """CashFlowStatement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCashFlowStatement(self):
        """Test CashFlowStatement"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CashFlowStatement()  # noqa: E501

        """
        No test json responses were defined for CashFlowStatement
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CashFlowStatement,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
