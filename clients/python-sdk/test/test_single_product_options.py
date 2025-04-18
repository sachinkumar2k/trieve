# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.13.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.single_product_options import SingleProductOptions

class TestSingleProductOptions(unittest.TestCase):
    """SingleProductOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleProductOptions:
        """Test SingleProductOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleProductOptions`
        """
        model = SingleProductOptions()
        if include_optional:
            return SingleProductOptions(
                group_tracking_id = '',
                product_description_html = '',
                product_name = '',
                product_primary_image_url = '',
                product_questions = [
                    ''
                    ],
                product_tracking_id = '',
                rec_search_query = ''
            )
        else:
            return SingleProductOptions(
        )
        """

    def testSingleProductOptions(self):
        """Test SingleProductOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
