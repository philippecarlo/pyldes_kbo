from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef

class KBO(DefinedNamespace):

    # classes
    Activity: URIRef
    Code: URIRef
    Denomination: URIRef
    Enterprise: URIRef
    Establishment: URIRef

    # properties
    activity: URIRef
    classification: URIRef
    address: URIRef 
    addressType: URIRef
    codeDescription: URIRef
    codeValue: URIRef
    denomination: URIRef
    denominationType: URIRef
    dateStrikingOff: URIRef
    establishment: URIRef
    juridicalSituation: URIRef
    juridicalForm: URIRef
    naceCode: URIRef
    naceVersion: URIRef
    startDate: URIRef
    status: URIRef

    _NS = Namespace("https://kbopub.economie.fgov.be/kbo#")