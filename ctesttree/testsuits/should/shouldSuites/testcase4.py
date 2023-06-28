# SPEC for Tree Spec
# SHOULD test case - 13
# SPEC Conform:
# The object of tree:value SHOULD be accompanied by a data type when it is a literal value.
#
# Verify:
# Each tree:Relation's tree:value is accompanied by a data type when it is a literal value.
#

import pyshacl
from rdflib import Graph

from ctesttree.testsuits.testconfig import data_graph


class ShouldTestCase4:

    def get_result(self):
        shapes_graph = Graph().parse("../shouldShapes/testcase4.ttl", format="ttl")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="json-ld",
            shacl_graph_format="rdfs",
            inference="rdfs",
            # debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms
