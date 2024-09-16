# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.rag_usage_graph import RAGUsageGraph

class TestRAGUsageGraph(unittest.TestCase):
    """RAGUsageGraph unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RAGUsageGraph:
        """Test RAGUsageGraph
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RAGUsageGraph`
        """
        model = RAGUsageGraph()
        if include_optional:
            return RAGUsageGraph(
                filter = trieve_py_client.models.rag_analytics_filter.RAGAnalyticsFilter(
                    date_range = null, 
                    rag_type = null, ),
                granularity = 'minute',
                type = 'rag_usage_graph'
            )
        else:
            return RAGUsageGraph(
                type = 'rag_usage_graph',
        )
        """

    def testRAGUsageGraph(self):
        """Test RAGUsageGraph"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()