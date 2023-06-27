from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


###
# created from ISA Programme Location Core Vocabulary
#  https://www.w3.org/ns/locn
##
class LOCN(DefinedNamespace):
    # classes
    Location: URIRef
    Address: URIRef
    Geometry: URIRef

    # property

    # Id of the address
    addressId: URIRef
    # The locn:address property relationship associates any resource with the locn:Address class
    address: URIRef
    # The name or names of a geographic area or locality that groups a number of addressable objects for addressing purposes, without being an administrative unit. This would typically be part of a city, a neighbourhood or village. The domain of locn:addressArea is locn:Address.
    addressArea: URIRef
    # The complete address written as a string, with or without formatting. The domain of locn:fullAddress is locn:Address.
    fullAddress: URIRef

    # administrativeUnitLevel1 (country)
    adminUnitL1: URIRef
    # administrativeUnitLevel2(country / region / state)
    adminUnitL2: URIRef

    # The Post Office Box number. The domain of locn:poBox is locn:Address.
    poBox: URIRef
    postName: URIRef
    # The Post Office Box number. The domain of locn:poBox is locn:Address.
    postCode: URIRef

    # plot the area.
    geometry: URIRef

    # locator Designator
    locatorDesignator: URIRef
    # locatorName
    locatorName: URIRef
    # The name of a passage or way through from one location to another.
    thoroughfare: URIRef
    _NS = Namespace("https://www.w3.org/ns/locn#")
