from typing import Dict
from rdflib import Graph, URIRef, RDF, Literal, BNode
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.models.kbo_base import KboBase

class KboCode(KboBase):

    def __init__(self):
        self.category: str = None
        self.code: str = None
        self.descriptions: Dict = None

    def to_rdf(self, graph: Graph, as_blank_node: bool = False) -> URIRef:
        if as_blank_node:
            code_ref = BNode()
        else:
            code_ref = URIRef(f"{KBO._NS}{self.category}_{self.code}")
        graph.add((code_ref, RDF.type, KBO.Code))
        graph.add((code_ref, KBO.codeValue, Literal(self.code)))
        for lang in self.descriptions:
            lang_literal = Literal(self.descriptions[lang], lang=lang)
            graph.add((code_ref, KBO.codeDescription, lang_literal))
        return code_ref