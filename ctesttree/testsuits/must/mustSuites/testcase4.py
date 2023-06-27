#
# SPEC for Tree Spec
# Must test case - 4
# SPEC Conform:
# A tree:Relation MUST have one tree:node object of the type tree:Node.
#
# Verify:
# Each tree:Relation has one tree:node object of the type tree:Node.
#

import pyshacl
from rdflib import Graph

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'


class MustTestCase4:
    def get_result(self):
        # Validate if each relation has a tree:node
        shapes_graph = Graph().parse("../mustShapes/testcase4.ttl", format="ttl")
        data_graph = Graph().parse("../../../sdk/ldes-test-client/crawldf/items.rdf", format="ntriples")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="ntriples",
            shacl_graph_format="ttl",
            inference="rdfs",
            debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results

        # Execute SPARQL query to have all the values of tree node
        query1 = """
                 PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                 PREFIX legal: <http://www.w3.org/ns/legal#> 
                 PREFIX tree: <https://w3id.org/tree#> 
                 select ?treenode where {
                       ?s tree:node ?treenode.
                       }
             """
        result_treenode = data_graph.query(query1)
        # print(len(result_treenode))
        # for row in result_treenode:
        #      print(row)

        # Execute SPARQL query to have all IRI with a type is a treeNode
        query2 = """
                 PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                 PREFIX legal: <http://www.w3.org/ns/legal#> 
                 PREFIX tree: <https://w3id.org/tree#> 
                 select ?treenode where {
                       ?k tree:node ?treenode. 
                       ?s rdf:type tree:Node.
                       ?s rdf:subject ?treenode.
                       
                       }
             """
        result_treenode1 = data_graph.query(query2)
        # print(len(result_treenode1))
        # for row in result_treenode1:
        #     print(row)
        # # #conpare if two results are identical
        # print(result_treenode == result_treenode1)

        return (result_treenode == result_treenode1) & conforms
