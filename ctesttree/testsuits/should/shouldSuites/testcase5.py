#
# SPEC for Tree Spec
# SHOULD test case - 14
# SPEC Conform:
# Every tree:Relation SHOULD have a tree:path,
# indicating the path from the member to the object on which the tree:Relation applies.
#
# Each tree:Relation has one tree:path set.
#

from rdflib import Graph
import pyshacl
import requests

# headers_get_json = {
#     'accept': 'application/ld+json'
# }
# url_view = 'https://apim-iow-apimanagement.azure-api.net/ldes/water-quality-observations/water-quality-observations-by-time'


class ShouldTestCase5:

    def get_result(self):
        shapes_graph = Graph().parse("../shouldShapes/testcase5.ttl", format="ttl")
        # data_graph = Graph().parse(requests.request("GET", url_view, headers=headers_get_json).content, format="json-ld")
        data_graph = Graph().parse("../../../../automation/expected/expected_timebase/view.turtle", format="ttl")

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
