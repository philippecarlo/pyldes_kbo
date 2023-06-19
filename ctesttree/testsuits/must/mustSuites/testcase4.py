
#
# SPEC for Tree Spec
# Must test case - 4
# SPEC Conform:
# A tree:Relation MUST have one tree:node object of the type tree:Node.
#
# Verify:
# Each tree:Relation has one tree:node object of the type tree:Node.
#

from rdflib import Graph
import pyshacl
import requests

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'

class MustTestCase4:
    def get_result(self):
        shapes_graph = Graph().parse("../mustShapes/testcase4.ttl", format="ttl")
        data_graph = Graph().parse("../../../sdk/ldes-test-client/crawldf/items.rdf", format="ntriples")
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
