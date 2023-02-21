from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef

###
# created from https://github.com/TREEcg/specification/blob/master/tree.ttl
##
class VCARD(DefinedNamespace):

    _NS = Namespace("http://www.w3.org/2006/vcard/")
    
    Address: URIRef
    BBS: URIRef
    Car: URIRef
    Cell: URIRef
    Dom: URIRef
    Email: URIRef
    Fax: URIRef
    Home: URIRef
    ISDN: URIRef
    Internet: URIRef
    Intl: URIRef
    Label: URIRef
    Location: URIRef
    Modem: URIRef
    Msg: URIRef
    Name: URIRef
    Organization: URIRef
    PCS: URIRef
    Pager: URIRef
    Parcel: URIRef
    Postal: URIRef
    Pref: URIRef
    Tel: URIRef
    VCard: URIRef
    Video: URIRef
    Voice: URIRef
    Work: URIRef
    X400: URIRef

    additionalName: URIRef = URIRef(f"{_NS}additional-name")
    adr: URIRef
    agent: URIRef
    bday: URIRef
    category: URIRef
    class_ : URIRef = URIRef(f"{_NS}class")
    countryName: URIRef = URIRef(f"{_NS}country-name")
    email: URIRef
    extendedAddress: URIRef = URIRef(f"{_NS}extended-address")
    familyName: URIRef = URIRef(f"{_NS}family-name")
    fn: URIRef
    geo: URIRef
    givenName: URIRef = URIRef(f"{_NS}given-name")
    honorificPrefix: URIRef = URIRef(f"{_NS}honorific-prefix")
    honorificSuffix: URIRef = URIRef(f"{_NS}honorific-suffix")
    key: URIRef
    label: URIRef
    latitude: URIRef
    locality: URIRef
    logo: URIRef
    longitude: URIRef
    mailer: URIRef
    n: URIRef
    nickname: URIRef
    note: URIRef
    org: URIRef
    organizationName: URIRef = URIRef(f"{_NS}organization-name")
    organizationUnit: URIRef = URIRef(f"{_NS}organization-unit")
    photo: URIRef
    postOfficeBox: URIRef = URIRef(f"{_NS}post-office-box")
    postalCode: URIRef = URIRef(f"{_NS}postal-code")
    prodid: URIRef
    region: URIRef
    rev: URIRef
    role: URIRef
    sortString: URIRef = URIRef(f"{_NS}sort-string")
    sound: URIRef
    streetAddress: URIRef = URIRef(f"{_NS}street-address")
    tel: URIRef
    title: URIRef
    tz: URIRef
    uid: URIRef
    url: URIRef

