# TODO
# SPEC for Tree Spec
# OPTIONAL test case - 7
# SPEC Conform:
# Multiple tree:view links MAY be provided
#
# Verify:
# Check that LDES Server supports multiple view links per collection
from rdflib import Graph
import pyshacl
import requests

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'

class OptionalTestCase2:

    def get_result(self):
        shapes_graph = Graph().parse("../optionalShapes/testcase2.ttl", format="ttl")
        data_graph = Graph().parse(requests.request("GET", url_view, headers=headers_get).content, format="ttl")
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
