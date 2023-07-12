import re

from ctesttree.testsuits.testconfig.testconfig import data_graph


# SPEC for Tree Spec
# Must test case - 22
# SPEC Conform:
# When using tree:GeospatiallyContainsRelation, the tree:path MUST refer to a literal containing a WKT string,
# such as geosparql:asWKT.
# Verify:
# The tree:path of each tree:Relation refers to a literal containing a WKT string, such as geosparql:asWKT.

class MustTestCase8:
    @staticmethod
    def contains_wkt_string(input_string):
        pattern = r'\bPOINT\s*\(|\bLINESTRING\s*\(|\bPOLYGON\s*\(|\bMULTIPOINT\s*\(|\bMULTILINESTRING\s*\(' \
                  r'|\bMULTIPOLYGON\s*\('
        match = re.search(pattern, input_string)
        return match is not None

    def get_result(self):
        conforms = True
        # Execute SPARQL query
        query = """
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX legal: <http://www.w3.org/ns/legal#> 
                PREFIX tree: <https://w3id.org/tree#>
                SELECT ?treevalue WHERE {
                      ?subject rdf:type tree:GeospatiallyContainsRelation.
                      ?subject tree:value ?treevalue .}
            """
        results = data_graph.query(query)

        # Process the query results
        if len(results) == 0:
            return " NOT Geospatial Fragment - TEST DOESN'T APPLY"
        else:
            for result in results:
                # Check if the return string contain a wkt string inside
                treevalue = str(result.asdict()['treevalue'].toPython())
                if not self.contains_wkt_string(treevalue):
                    conforms = False
            return conforms
