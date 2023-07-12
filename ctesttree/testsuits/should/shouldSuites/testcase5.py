#
# SPEC for Tree Spec
# SHOULD test case - 14
# SPEC Conform:
# Every tree:Relation SHOULD have a tree:path,
# indicating the path from the member to the object on which the tree:Relation applies.
#
# Each tree:Relation has one tree:path set.
#

import pyshacl
from rdflib import Graph

from ctesttree.testsuits.testconfig.testconfig import data_graph


class ShouldTestCase5:

    def get_result(self):
        shapes_graph = Graph().parse("../shouldShapes/testcase5.ttl", format="ttl")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="json-ld",
            shacl_graph_format="rdfs",
            inference="rdfs",
            # debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results

        return conforms
