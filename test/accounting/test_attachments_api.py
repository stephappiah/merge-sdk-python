"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.attachments_api import AttachmentsApi  # noqa: E501


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attachments_list(self):
        """Test case for attachments_list

        """
        pass

    def test_attachments_retrieve(self):
        """Test case for attachments_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
