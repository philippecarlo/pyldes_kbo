from hashlib import blake2s
from datetime import datetime
from rdflib import Graph, URIRef, Literal, BNode, RDF, ORG, FOAF, SKOS
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.namespace.locn import LOCN
from pyldes_kbo.namespace.geo import GEO
from pyldes_kbo.namespace.vcard import VCARD
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_code import KboCode
from geopy.geocoders import Nominatim
from shapely import wkt
from shapely.geometry import Point

class KboAddress(KboBase):

    def __init__(self):
        self.type_of_address: KboCode = None
        self.zip_code: str = None
        self.municipality: str = None
        self.street: str = None
        #self.street_no_parenthese:str = self.street.partition('(')[1]
        self.house_number: str = None
        self.box: str = None
        self.extra_info: str = None
        self.date_striking_off: datetime = None
        #self.full_address:str =
        self.full_address:str = None
        self.full_address_no_bracket:str =None

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
        graph.add((address_ref, LOCN.fullAddress, Literal(self.full_address)))
        #print(self.full_address)
        graph.add((address_ref, GEO.asWKT,Literal(self.address_to_wkt(self.full_address_no_bracket))))
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
        graph.add((address_ref, LOCN.fullAddress, Literal(self.full_address)))
        #print(self.full_address)
        graph.add((address_ref, GEO.asWKT,Literal(self.address_to_wkt(self.full_address_no_bracket))))
        graph.add((address_ref, LOCN.poBox, Literal(self.box)))
        address_type_ref = self.type_of_address.to_rdf_version(graph, as_blank_node=as_blank_node)
        graph.add((address_ref, KBO.addressType, address_type_ref))
        if self.date_striking_off:
            graph.add((address_type_ref, KBO.dateStrikingOff, Literal(self.date_striking_off)))
        return address_ref

    def address_to_wkt(self, full_address_no_bracket:str)-> str:
        locator = Nominatim(user_agent="myGeocode")
        #full_address = "Maurice De Moorplein 7, 1020 Brussel, Belgium".replace("Bld d", "Boulevard d" )
        location = locator.geocode(full_address_no_bracket)
        if location is None:
            print("Bad quality address: " + full_address_no_bracket)
            point = Point(0,0)
        else:
            # print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
            point = Point(location.longitude, location.latitude)
            return point.wkt


