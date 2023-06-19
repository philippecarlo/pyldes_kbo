# TODO:

# SPEC for Tree Spec
# SHOULD test case - 13
# SPEC Conform:
# The object of tree:value SHOULD be accompanied by a data type when it is a literal value.
#
# Verify:
# Each tree:Relation's tree:value is accompanied by a data type when it is a literal value.
#

# How can the LDES Server knows it is a literal if the ingestion data is not accompanied with a datatype?
from rdflib import Graph
import pyshacl
import requests



class ShouldTestCase4:

    def get_result(self):
        return "UNDEFINED"
