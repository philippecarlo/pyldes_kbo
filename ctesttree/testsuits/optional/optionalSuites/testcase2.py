# SPEC for Tree Spec
# OPTIONAL test case - 7
# SPEC Conform:
# Multiple tree:view links MAY be provided
#
# Verify:
# Check that LDES Server supports multiple view links per collection
import pyshacl
from rdflib import Graph

from ctesttree.testsuits.testconfig import data_graph_view


class OptionalTestCase2:

    def get_result(self):
        shapes_graph = Graph().parse("../optionalShapes/testcase2.ttl", format="ttl")
        results = pyshacl.validate(
            data_graph_view,
            shacl_graph=shapes_graph,
            data_graph_view_format="ntriples",
            shacl_graph_format="rdfs",
            inference="rdfs",
            # debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms
