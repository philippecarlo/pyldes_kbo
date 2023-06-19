#
# SPEC for Tree Spec
# OPTIONAL test case - 18
# SPEC Conform:
# Check that LDES Server supports tree:path refers to an implicit property.
#
# Verify:
# Check that LDES Server supports tree:path refers to an implicit property.

from rdflib import Graph
import pyshacl
class OptionalTestCase5:
    def get_result(self):
        shapes_graph = Graph().parse("../optionalShapes/testcase4.ttl", format="ttl")
        data_graph = Graph().parse("../../../../sdk/ldes-test-client/items.rdf", format="ntriples")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="ntriples",
            shacl_graph_format="ttl",
            inference="rdfs",
            debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms
