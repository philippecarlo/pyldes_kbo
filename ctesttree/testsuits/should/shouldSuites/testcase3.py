#
# SPEC for Tree Spec
# SHOULD test case - 1
# SPEC Conform:
# The tree:Relation’s tree:value SHOULD be set.
#
# Verify:
# Each tree:Relation has one tree:value set.
#

import pyshacl
from rdflib import Graph


class ShouldTestCase3:

    def get_result(self):
        shapes_graph = Graph().parse("../shouldShapes/testcase3.ttl", format="ttl")
        data_graph = Graph().parse("../../../sdk/ldes-test-client/crawldf/items.rdf", format="ntriples")
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
