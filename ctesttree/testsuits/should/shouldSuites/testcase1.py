# TODO
# SPEC for Tree Spec
# SHOULD test case - 3
# SPEC Conform:
# Therefore a data publisher SHOULD annotate a tree:Collection
# instance with a SHACL shape. The tree:shape points to a SHACL description of the shape (sh:NodeShape).
#
# Verify:
# There should be a SHACL shape configured for the dataset
#
import pyshacl
from rdflib import Graph

from ctesttree.testsuits.testconfig.testconfig import data_graph, data_graph_view


class ShouldTestCase1:

    def get_result(self):

        # Create a new graph for merging
        merged_graph = Graph()

        # Copy triples from the first graph
        for triple in data_graph:
            merged_graph.add(triple)

        # Copy triples from the second graph
        for triple in data_graph_view:
            merged_graph.add(triple)

        results = pyshacl.validate(
            data_graph,
            shacl_graph=merged_graph,
            data_graph_format="json-ld",
            shacl_graph_format="rdfs",
            inference="rdfs",
            # debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms
