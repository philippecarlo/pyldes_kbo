import maya
from typing import List
from datetime import datetime
from rdflib import Graph, URIRef, Literal, RDF, RDFS, ORG, SKOS
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.namespace.locn import LOCN
from pyldes_kbo.namespace.legal import LEGAL
from pyldes_kbo.namespace.termname import TERMNAME
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_code import KboCode
from pyldes_kbo.models.kbo_contact import KboContact
from pyldes_kbo.models.kbo_address import KboAddress
from pyldes_kbo.models.kbo_activity import KboActivity
from pyldes_kbo.models.kbo_denomination import KboDenomination
from pyldes_kbo.models.kbo_establishment import KboEstablishment

class KboEnterprise(KboBase):

    def __init__(self):
        self.enterprise_number: str = None
        self.status: KboCode = None
        self.juridical_situation: KboCode = None
        self.type_of_enterprise: KboCode = None
        self.juridical_form: KboCode = None
        self.start_date: datetime = None
        self.addresses: List[KboAddress] = None
        self.establishments: List[KboEstablishment] = None
        self.denominations: List[KboDenomination] = None
        self.contacts: List[KboContact] = None
        self.activities: List[KboActivity] = None
        self.version = ".2022.11"

    def to_rdf(self, graph: Graph, version_object: bool = True, with_blank_nodes: bool = False) -> URIRef:

        enterprise_ref = URIRef(f"{KBO._NS}{self.enterprise_number.replace('.', '')}")
        status_ref = self.status.to_rdf(graph, as_blank_node=with_blank_nodes)
        juridical_situation_ref = self.juridical_situation.to_rdf(graph, as_blank_node=with_blank_nodes)
        juridical_form_ref = self.juridical_form.to_rdf(graph, as_blank_node=with_blank_nodes)
        #graph.add((enterprise_ref, RDF.type, ORG.Organization))
        graph.add((enterprise_ref, RDF.type, KBO.Enterprise))
        graph.add((enterprise_ref, KBO.status, status_ref))
        graph.add((enterprise_ref, RDF.type, LEGAL.legalEntity))
        graph.add((enterprise_ref, LEGAL.companyType, juridical_form_ref))
        graph.add((enterprise_ref, LEGAL.companyStatus, juridical_situation_ref))
        for denom in self.denominations:
            lang = denom.get_lang()
            if denom.type_of_denomination.code == "001":
                graph.add((enterprise_ref,LEGAL.legalName , Literal(denom.denomination, lang=lang)))
            if denom.type_of_denomination.code == "002":
                graph.add((enterprise_ref,LEGAL.legalName, Literal(denom.denomination, lang=lang)))
        for address in self.addresses:
            address_ref = address.to_rdf(graph, as_blank_node=with_blank_nodes)
            graph.add((enterprise_ref, LEGAL.registeredAddress, address_ref))
        for establishment in self.establishments:
            establishment_ref = establishment.to_rdf(graph, as_blank_node=with_blank_nodes)
            graph.add((enterprise_ref, KBO.establishment, establishment_ref))
        for contact in self.contacts:
            contact.load_entity_contact(graph, enterprise_ref)
        for activity in self.activities:
            activity_ref = activity.to_rdf(graph, as_blank_node=with_blank_nodes)
            graph.add((enterprise_ref, KBO.activity, activity_ref))
        return enterprise_ref

        # To make a version KBO linked data
        # a.	Leave out the codes themselves, only keep references to them (as they do not change)
        # b.	Only keep: Enterpise, Address, Site, Activity
        # c.	Add a versionOf attribute to enterprise and assign it the original id of the enterprise
        # d.	Replace the id with the version URI above
    def to_rdf_version(self, graph: Graph, version_object: bool = True, with_blank_nodes: bool = False) -> URIRef:

        enterprise_ref = URIRef(f"{KBO._NS}{self.enterprise_number.replace('.', '')}{self.version}")
        status_ref = self.status.to_rdf(graph, as_blank_node=with_blank_nodes)
        juridical_situation_ref = self.juridical_situation.to_rdf_version(graph, as_blank_node=with_blank_nodes)
        juridical_form_ref = self.juridical_form.to_rdf_version(graph, as_blank_node=with_blank_nodes)
        graph.add((enterprise_ref, TERMNAME.isVersionOf, URIRef(f"{KBO._NS}{self.enterprise_number.replace('.', '')}")))
        #graph.add((enterprise_ref, RDF.type, ORG.Organization))
        graph.add((enterprise_ref, KBO.status, status_ref))
        graph.add((enterprise_ref, RDF.type, KBO.Enterprise))
        graph.add((enterprise_ref,RDF.type, LEGAL.legalEntity))
        graph.add((enterprise_ref, LEGAL.companyType, juridical_form_ref))
        graph.add((enterprise_ref, LEGAL.companyStatus, juridical_situation_ref))
        for denom in self.denominations:
             lang = denom.get_lang()
             if denom.type_of_denomination.code == "001":
                 graph.add((enterprise_ref,LEGAL.legalName , Literal(denom.denomination, lang=lang)))
             if denom.type_of_denomination.code == "002":
                 graph.add((enterprise_ref,LEGAL.legalName, Literal(denom.denomination, lang=lang)))
        for address in self.addresses:
            address_ref = address.to_rdf_version(graph, as_blank_node=with_blank_nodes)
            graph.add((enterprise_ref, LEGAL.registeredAddress, address_ref))
        for establishment in self.establishments:
            establishment_ref = establishment.to_rdf_version(graph, as_blank_node=with_blank_nodes)
            graph.add((enterprise_ref, KBO.establishment, establishment_ref))
        for activity in self.activities:
            activity_ref = activity.to_rdf_version(graph, as_blank_node=with_blank_nodes)
            graph.add((enterprise_ref, KBO.activity, activity_ref))
        return enterprise_ref