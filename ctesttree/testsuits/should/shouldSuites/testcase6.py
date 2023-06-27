# TODO
#
# SPEC for Tree Spec
# SHOULD test case - 26
# SPEC Conform:
#
# VOCAB-DCAT-2 is the standard for Open Data Portals by W3C. In order to find TREE compliant datasets in data
# portals, there SHOULD be a dcat:accessURL from the dcat:Distribution to the entrypoint where the tree:Collections
# are described. Furthermore, there SHOULD be a dct:conformsTo this URI: https://w3id.org/tree.
#
# Verify: the LDES server root lists all tree:Collections and tree:Views and that the corresponding view descriptions
# include a dct:conformsTo property with the value https://w3id.org/tree.
#
import pyshacl
import requests
from rdflib import Graph

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'



class ShouldTestCase6:

    def get_result(self):
        shapes_graph = Graph().parse("../shouldShapes/testcase6.ttl", format="ttl")
        data_graph = Graph().parse(requests.request("GET", url_view, headers=headers_get).content, format="ttl")
        is_empty = len(data_graph) == 0
        if is_empty:
            print("Empty graph, NOT Conform")
            return False
        else:
            results = pyshacl.validate(
                data_graph,
                shacl_graph=shapes_graph,
                data_graph_format="ttl",
                shacl_graph_format="ttl",
                inference="rdfs",
                # debug=True,
                serialize_report_graph="ttl",
            )

            conforms, report_graph, report_text = results

            return conforms
