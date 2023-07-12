from rdflib import Graph, URIRef, RDF, OWL

g = Graph()
id_1 = URIRef("id_1")
id_2 = URIRef("id_2")
g.add((id_1, RDF.type, URIRef("http://www.w3.org/2002/07/owl#Thing")))
g.add((id_2, RDF.type, OWL.Thing))

print(g.serialize(format="json-ld"))
