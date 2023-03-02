from hashlib import blake2s
from datetime import datetime
from rdflib import Graph, URIRef, Literal, BNode, RDF, ORG, FOAF, SKOS
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.namespace.locn import LOCN
from pyldes_kbo.namespace.vcard import VCARD
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_code import KboCode

class KboAddress(KboBase):

    def __init__(self):
        self.type_of_address: KboCode = None
        self.zip_code: str = None
        self.municipality: str = None
        self.street: str = None
        self.house_number: str = None
        self.box: str = None
        self.extra_info: str = None
        self.date_striking_off: datetime = None

    def to_rdf(self, graph: Graph, as_blank_node: bool = False) -> URIRef:
        if as_blank_node:
            address_ref = BNode()
        else:
            addr = f"{self.zip_code} {self.street} {self.house_number} {self.box}" 
            h = blake2s(digest_size=10)
            h.update(addr.encode("utf-8"))
            key = h.hexdigest()
            address_ref = URIRef(f"{KBO._NS}{key}")
        graph.add((address_ref, RDF.type, LOCN.Address))
        graph.add((address_ref, LOCN.postCode, Literal(self.zip_code)))
        graph.add((address_ref, LOCN.postName, Literal(self.municipality)))
        graph.add((address_ref, LOCN.fullAddress, Literal(f"{self.street} {self.house_number}, {self.zip_code} {self.municipality}, Belgium")))
        graph.add((address_ref, LOCN.poBox, Literal(self.box)))
        address_type_ref = self.type_of_address.to_rdf(graph, as_blank_node=as_blank_node)
        graph.add((address_ref, KBO.addressType, address_type_ref))
        if self.date_striking_off:
            graph.add((address_type_ref, KBO.dateStrikingOff, Literal(self.date_striking_off)))
        return address_ref

    def to_rdf_version(self, graph: Graph, as_blank_node: bool = False) -> URIRef:
        if as_blank_node:
            address_ref = BNode()
        else:
            addr = f"{self.zip_code} {self.street} {self.house_number} {self.box}"
            h = blake2s(digest_size=10)
            h.update(addr.encode("utf-8"))
            key = h.hexdigest()
            address_ref = URIRef(f"{KBO._NS}{key}")
        graph.add((address_ref, RDF.type, LOCN.Address))
        graph.add((address_ref, LOCN.postCode, Literal(self.zip_code)))
        graph.add((address_ref, LOCN.postName, Literal(self.municipality)))
        graph.add((address_ref, LOCN.fullAddress, Literal(f"{self.street} {self.house_number}, {self.zip_code} {self.municipality}, Belgium")))
        graph.add((address_ref, LOCN.poBox, Literal(self.box)))
        address_type_ref = self.type_of_address.to_rdf_version(graph, as_blank_node=as_blank_node)
        graph.add((address_ref, KBO.addressType, address_type_ref))
        if self.date_striking_off:
            graph.add((address_type_ref, KBO.dateStrikingOff, Literal(self.date_striking_off)))
        return address_ref