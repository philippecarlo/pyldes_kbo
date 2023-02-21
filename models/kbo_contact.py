from rdflib import Graph, URIRef, Literal, BNode, RDF, ORG, FOAF, SKOS
from pyldes_kbo.namespace.vcard import VCARD
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_code import KboCode

class KboContact(KboBase):

    def __init__(self):
        self.entity_contact: KboCode = None
        self.contact_type: KboCode = None
        self.value: str = None

    def load_entity_contact(self, graph: Graph, enitiy: URIRef):
        if self.contact_type.code == "EMAIL":
            graph.add((enitiy, VCARD.email, Literal(self.value)))
        if self.contact_type.code == "TEL":
            graph.add((enitiy, VCARD.tel, Literal(self.value)))
        if self.contact_type.code == "WEB":
            graph.add((enitiy, VCARD.url, Literal(self.value)))
