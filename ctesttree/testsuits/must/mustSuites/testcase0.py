#
# SPEC for Tree Spec Must test case - 1
# SPEC Conform:
# To Verify if the Generated Output stream conforms the Tree SPEC or LDES SPEC.
# The output should be a TREE Collection and an LDES Collection.
# The current test is a very first case for validating the current conformance.


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

            return conforms
            # return True
