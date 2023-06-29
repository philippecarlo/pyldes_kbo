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
from rdflib import Graph

from ctesttree.testsuits.testconfig.testconfig import data_graph_view


class MustTestCase1:
    @staticmethod
    def get_result() -> bool:
        shapes_graph = Graph().parse("../mustShapes/testcase1.ttl", format="ttl")
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
