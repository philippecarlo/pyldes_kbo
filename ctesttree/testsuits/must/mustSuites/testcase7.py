# TODO
import pyshacl
from rdflib import Graph

from ctesttree.testsuits.testconfig.testconfig import data_graph


# SPEC for Tree Spec
# Must test case - 20
# SPEC Conform:
# Also the comparator relations such as tree:GreaterThanRelation can be used.
# The strings MUST then be compared according to case-sensitive unicode ordering.
# Verify:
# The evaluation based on the tree:value of the tree:path is complaint to case-sensitive unicode ordering

class MustTestCase7:

    def get_result(self):
        shapes_graph = Graph().parse("../mustShapes/testcase7.ttl", format="ttl")
        if len(data_graph) == 0:
            print("Empty graph, NOT Conform")
            sys.exit()
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

            if conforms:
                # TODO
                return "TODO"
            else:
                return "NOT substring fragmentation uses Greater/Less/Equal comparison - TEST DOESN'T APPLY"
