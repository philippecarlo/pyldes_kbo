
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
        data_graph = Graph().parse(requests.request("GET", url_view, headers=headers_get).content, format="ttl")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="json-ld",
            shacl_graph_format="rdfs",
            inference="rdfs",
            debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms
