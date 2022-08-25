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
from MergePythonSDK.ats.model.validation_problem_source import ValidationProblemSource
globals()['ValidationProblemSource'] = ValidationProblemSource
from MergePythonSDK.ats.model.error_validation_problem import ErrorValidationProblem
from MergePythonSDK.shared.api_client import ApiClient


class TestErrorValidationProblem(unittest.TestCase):
    """ErrorValidationProblem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testErrorValidationProblem(self):
        """Test ErrorValidationProblem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ErrorValidationProblem()  # noqa: E501

        """
        No test json responses were defined for ErrorValidationProblem
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ErrorValidationProblem,), False)

        assert deserialized is not None

        assert deserialized.title is not None
        assert deserialized.detail is not None
        assert deserialized.problem_type is not None


if __name__ == '__main__':
    unittest.main()
