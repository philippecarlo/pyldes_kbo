from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


###
# created from ISA Programme Location Core Vocabulary
#  https://www.w3.org/ns/locn
##
class LEGAL(DefinedNamespace):
    # classes
    legalEntity: URIRef
    # property
    # The name under which the Legal Entity is legally registered
    legalName: URIRef
    legalIdentifier: URIRef
    # This is a general term that encompasses all the economic activities carried out by a company during the course of business.
    # The activity of a company should be recorded using a controlled vocabulary. Several such vocabularies exist,
    # many of which map to the UN's ISIC codes. Where a particular controlled vocabulary is in use within a given context,
    # such as SIC codes in the UK, it is acceptable to use these, however,
    # the preferred choice for European interoperability is NACE.
    companyActivity: URIRef

    # The classification of the Legal Entity as a member of a particular group in the context of legal registration.
    companyType: URIRef

    # Information about the viability of the current position of the legal entity.
    companyStatus: URIRef

    registeredAddress: URIRef
    _NS = Namespace("http://www.w3.org/ns/legal#")
