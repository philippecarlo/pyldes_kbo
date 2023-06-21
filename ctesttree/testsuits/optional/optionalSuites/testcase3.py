# SPEC for Tree Spec
# OPTIONAL test case - 9
# SPEC Conform:
# A tree:Node element MAY have one or more tree:relation properties.
#
# Verify:
# Check that if LDES Server supports multiple relations (e.g., by using geospatial or substring fragmentation).

from rdflib import Graph
import pyshacl

class OptionalTestCase3:

    def get_result(self):
        shapes_graph = Graph().parse("../optionalShapes/testcase3.ttl", format="ttl")
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
