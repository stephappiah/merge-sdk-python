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
from MergePythonSDK.accounting.model.validation_problem_source import ValidationProblemSource
globals()['ValidationProblemSource'] = ValidationProblemSource
from MergePythonSDK.accounting.model.warning_validation_problem import WarningValidationProblem
from MergePythonSDK.shared.api_client import ApiClient


class TestWarningValidationProblem(unittest.TestCase):
    """WarningValidationProblem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWarningValidationProblem(self):
        """Test WarningValidationProblem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WarningValidationProblem()  # noqa: E501

        """
        No test json responses were defined for WarningValidationProblem
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (WarningValidationProblem,), False)

        assert deserialized is not None

        assert deserialized.title is not None
        assert deserialized.detail is not None
        assert deserialized.problem_type is not None


if __name__ == '__main__':
    unittest.main()
