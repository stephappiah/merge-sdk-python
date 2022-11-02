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
from MergePythonSDK.accounting.model.debug_mode_log import DebugModeLog
from MergePythonSDK.accounting.model.error_validation_problem import ErrorValidationProblem
from MergePythonSDK.accounting.model.expense import Expense
from MergePythonSDK.accounting.model.warning_validation_problem import WarningValidationProblem
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['Expense'] = Expense
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergePythonSDK.accounting.model.expense_response import ExpenseResponse
from MergePythonSDK.shared.api_client import ApiClient


class TestExpenseResponse(unittest.TestCase):
    """ExpenseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExpenseResponse(self):
        """Test ExpenseResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ExpenseResponse()  # noqa: E501

        """
        No test json responses were defined for ExpenseResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ExpenseResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
