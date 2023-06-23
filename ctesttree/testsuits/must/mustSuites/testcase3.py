from rdflib import Graph
import pyshacl
import requests

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'

#
# SPEC for Tree Spec
# Must test case - 3
# SPEC Conform:
# Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.
#
# Verify:
# The amount of the LDES members = The Input LDES members (20, in the context of BEL20, KBO data).
#

class MustTestCase3:
    def dict_to_tuple(self,dictionary):
        return tuple(sorted(dictionary.items()))

    def get_result(self):
        from rdflib import Graph

        # Create a graph and load data
        graph = Graph()
        graph.parse("../../../sdk/ldes-test-client/crawldf/items.rdf", format="ntriples")

        # Execute SPARQL query
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX legal: <http://www.w3.org/ns/legal#> 
            select ?thing where {
                  ?thing rdf:type legal:legalEntity .}
        """
        results = graph.query(query)
        # Process the query results
        print(len(results))
        return len(results) == 20
