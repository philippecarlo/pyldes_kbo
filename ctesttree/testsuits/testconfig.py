import requests
from rdflib import Graph

headers_get = {
    'accept': 'application/turtle'
}
url_view = 'http://localhost:8080/kbo'
#
# # Configuration for the data catalog page
data_graph_view = Graph().parse(requests.request("GET", url_view, headers=headers_get).content, format="ttl")
# whole data graph
data_graph = Graph().parse("../../../sdk/ldes-test-client/crawldf/items.rdf", format="ntriples")
