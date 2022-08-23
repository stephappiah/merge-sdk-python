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
from MergePythonSDK.accounting.model.credit_note import CreditNote
globals()['CreditNote'] = CreditNote
from MergePythonSDK.accounting.model.paginated_credit_note_list import PaginatedCreditNoteList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedCreditNoteList(unittest.TestCase):
    """PaginatedCreditNoteList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedCreditNoteList(self):
        """Test PaginatedCreditNoteList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedCreditNoteList()  # noqa: E501

        """
        No test json responses were defined for PaginatedCreditNoteList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedCreditNoteList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
