from hashlib import blake2s
from rdflib import URIRef, BNode, Literal, Graph, SKOS, RDF, FOAF
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_code import KboCode

class KboDenomination(KboBase):

    def __init__(self):
        self.language: KboCode = None
        self.type_of_denomination: KboCode = None
        self.denomination: str = None

    def load_denomination(self, graph: Graph, entity: URIRef):
        lang = self.get_lang()
        graph.add((entity, FOAF.name, Literal(self.denomination, lang=lang)))
        
    
    def get_lang(self) -> str:
        if self.language.code == "1":
            return "FR"
        elif self.language.code == "2":
            return "NL"
        elif self.language.code == "3":
            return "DE"
        elif self.language.code == "4":
            return "EN"
        else:
            return None
        