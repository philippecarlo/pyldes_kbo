from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


###
# created from ISA Programme Location Core Vocabulary
#  https://www.w3.org/ns/locn
##
class TERMNAME(DefinedNamespace):

    # property

    # Some jurisdictions recognise concepts such as a trading name or alternative forms of a legal entity's name.
    # The alternative name property can be used to record such names but should not be used to record translations of the primary legal name.
    # Where more than one name exists and where they have equal standing but are expressed in different languages,
    # identify the language used in each of the multiple names.
    alternative:URIRef
    identifier:URIRef
    # The date on which the Identifier was assigned.
    issued:URIRef

    _NS = Namespace("http://purl.org/dc/terms/")
