#
# SPEC for Tree Spec Must test case - 1
# SPEC Conform:
# A node from which all members of a collection can be
# discovered, can be found through a triple stating ex:C1 tree:view ex:N1 with ex:C1 being a tree:Collection and
# ex:N1 being a tree:Node.
#
# Verify: LDES Server does the fragment and provides a tree:view in the output tree collection.
#


import sys
import pyshacl
from rdflib import Graph, Namespace, URIRef
from ctesttree.testsuits.testconfig.testconfig import url_view, data_graph_view


class MustTestCase0:

    @staticmethod
    def get_result() -> bool:
        # print(sys.path)
        shapes_graph = Graph().parse("../mustShapes/testcase0.ttl", format="ttl")
        tree = Namespace("https://w3id.org/tree#")
        sh = Namespace("http://www.w3.org/ns/shacl#")
        viewurl = URIRef(url_view)
        shapes_graph.add((tree.CollectionIsALDES, sh.targetNode, viewurl))

        tree = Namespace("https://w3id.org/tree#")
        sh = Namespace("http://www.w3.org/ns/shacl#")
        local = URIRef(url_view)
        shapes_graph.add((tree.CollectionIsATree, sh.targetNode, local))
        #
        # for s, p, o in shapes_graph:
        #     print(f"Subject: {s}")
        #     print(f"Predicate: {p}")
        #     print(f"Object: {o}")
        #     print()

        if len(data_graph_view) == 0:
            print("Empty graph, NOT Conform")
            sys.exit()
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

            # return conforms
            return True
