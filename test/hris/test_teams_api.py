"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.hris
from MergePythonSDK.hris.api.teams_api import TeamsApi  # noqa: E501


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_teams_list(self):
        """Test case for teams_list

        """
        pass

    def test_teams_retrieve(self):
        """Test case for teams_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
