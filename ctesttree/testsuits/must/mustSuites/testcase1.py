#
# SPEC for Tree Spec Must test case - 1
# SPEC Conform:
# A node from which all members of a collection can be
# discovered, can be found through a triple stating ex:C1 tree:view ex:N1 with ex:C1 being a tree:Collection and
# ex:N1 being a tree:Node.
#
# Verify: LDES Server does the fragment and provides a tree:view in the output LDES collection.
#


from rdflib import Graph
import pyshacl
import requests

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'


class MustTestCase1:

    def get_result(self):
        shapes_graph = Graph().parse("../mustShapes/testcase1.ttl", format="ttl")
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
