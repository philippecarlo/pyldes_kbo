from ctesttree.testsuits.testconfig import data_graph


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
    @staticmethod
    def get_result() -> bool:
        # Execute SPARQL query
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX legal: <http://www.w3.org/ns/legal#> 
            select ?VersionNumber where {
                  ?Company rdf:type legal:legalEntity .
                  ?Company rdf:subject ?VersionNumber.
                  }
        """
        # Process the query results
        results = data_graph.query(query)
        # clean the duplicated members
        unique_list = []
        for row in results:
            unique_list.append(row.asdict()['VersionNumber'].toPython())
        print(len(sorted(list(set(unique_list)))))
        return len(sorted(list(set(unique_list)))) == 20
