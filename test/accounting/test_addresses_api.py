"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.addresses_api import AddressesApi  # noqa: E501


class TestAddressesApi(unittest.TestCase):
    """AddressesApi unit test stubs"""

    def setUp(self):
        self.api = AddressesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_addresses_retrieve(self):
        """Test case for addresses_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
