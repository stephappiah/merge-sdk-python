"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.contacts_api import ContactsApi  # noqa: E501


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_contacts_list(self):
        """Test case for contacts_list

        """
        pass

    def test_contacts_retrieve(self):
        """Test case for contacts_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
