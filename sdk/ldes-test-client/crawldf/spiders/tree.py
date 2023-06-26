import scrapy
from rdflib import RDF, Graph, URIRef, BNode
import pprint
import re

from crawldf.items import CrawledRDFPage

class TreeSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            "crawldf.pipelines.RDFGraphToPageObjectPipeline": 200,
            "crawldf.pipelines.RDFWriterPipeline": 300,
        }
    }

    def parse(self, response):
        content_type = re.search(r"^([^;]*)", str(response.headers["Content-Type"].decode())).group(0)
        
        graph = Graph()
        graph.parse( data=response.body, format=content_type, publicID=response.url)
        # Follow tree:relations
        relations_query = """
            PREFIX tree: <https://w3id.org/tree#>
            SELECT DISTINCT ?relation
            WHERE {
                ?node a tree:Node .
                ?node tree:relation/tree:node ?relation.
            }"""

        relations_query_result = graph.query(relations_query)
        for row in relations_query_result:
            yield scrapy.Request(row.relation)

        # Create item from document
        yield CrawledRDFPage(graph=graph, url=response.url, headers=response.headers)