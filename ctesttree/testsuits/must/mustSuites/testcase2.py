#
# SPEC for Tree Spec Must test case - 2
# SPEC Conform:
# When the current page is a tree:Node, there MUST be a property
# linking the current page URL to the URI of the tree:Collection.
#
# Verify: "Each tree:Node in the LDES Collection has
# a link between current page to tree:Collection."
#

import pyshacl
from rdflib import Graph

from ctesttree.testsuits.testconfig.testconfig import data_graph


class MustTestCase2:
    @staticmethod
    def get_result() -> bool:
        shapes_graph = Graph().parse("../mustShapes/testcase2.ttl", format="ttl")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="ntriples",
            shacl_graph_format="rdfs",
            inference="rdfs",
            # debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms
