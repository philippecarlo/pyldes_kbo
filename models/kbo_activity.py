from rdflib import Graph, URIRef, Literal, BNode, RDF, ORG, FOAF, SKOS
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.namespace.legal import LEGAL
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_code import KboCode

class KboActivity(KboBase):

    def __init__(self):
        self.activity_group: KboCode = None
        self.nace_version: str = None
        self.nace_code: KboCode = None
        self.classification: KboCode = None

    def to_rdf(self, graph: Graph, as_blank_node: bool = False) -> URIRef:
        if as_blank_node:
            activity_ref = BNode()
        else:
            activity_ref = URIRef(f"{KBO._NS}{self.nace_version}_{self.nace_code.code}")
        graph.add((activity_ref, RDF.type, KBO.Activity))
        #add nace code
        graph.add((activity_ref, LEGAL.companyActivity, self.nace_code.to_rdf(graph, as_blank_node=as_blank_node)))
        #graph.add((activity_ref, KBO.naceVersion, Literal(self.nace_version)))
        graph.add((activity_ref, KBO.classification, self.classification.to_rdf(graph, as_blank_node=as_blank_node)))
        return activity_ref