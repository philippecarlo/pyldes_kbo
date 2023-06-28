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
from rdflib import Graph

from ctesttree.testsuits.testconfig import data_graph_view


class ShouldTestCase6:

    def get_result(self):
        shapes_graph = Graph().parse("../shouldShapes/testcase6.ttl", format="ttl")
        if len(data_graph_view) == 0:
            print("Empty graph, NOT Conform")
            return False
        else:
            results = pyshacl.validate(
                data_graph_view,
                shacl_graph=shapes_graph,
                data_graph_format="ttl",
                shacl_graph_format="ttl",
                inference="rdfs",
                # debug=True,
                serialize_report_graph="ttl",
            )

            conforms, report_graph, report_text = results

            return conforms
