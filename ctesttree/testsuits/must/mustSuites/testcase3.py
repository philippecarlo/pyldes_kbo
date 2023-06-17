from rdflib import Graph
import pyshacl
import requests

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'

#
# SPEC for Tree Spec
# Must test case - 3
# SPEC Conform:
# Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.
#
# Verify:
# The amount of the LDES members = The Input LDES members (20, in the context of BEL20, KBO data).
#

class MustTestCase3:
    def get_result(self):
        shapes_graph = Graph().parse("../mustShapes/testcase3.ttl", format="ttl")
        data_graph = Graph().parse(requests.request("GET", url_view, headers=headers_get).content, format="ttl")
        #data_graph = Graph().parse("../../../../automation/expected/expected_timebase/random.turtle", format="ttl")
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
