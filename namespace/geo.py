from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


##
# Created from https://github.com/SEMICeu/LinkedDataEventStreams/blob/master/vocabulary.ttl
##
class GEO(DefinedNamespace):
    # classes
    # properties
    asWKT:URIRef
    wktLiteral:URIRef

    _NS = Namespace("http://www.opengis.net/ont/geosparql#")