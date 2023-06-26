# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pprint
from itemadapter import ItemAdapter
from rdflib import RDF, BNode, Graph, Literal, URIRef
from scrapy.exceptions import DropItem

from crawldf.items import RDFPage

# Nests the retrieved triples as blanknodes inside a page object with metadata about the request.
class RDFGraphToPageObjectPipeline:
    def process_item(self, item, spider):
        out_graph = Graph()

        # Ontology definition
        # -page
        has_subject = RDF.subject
        has_contents = URIRef("http://example.org/has_contents")
        crawled_page = URIRef("http://example.org/CrawledPage")
        # -headers
        has_header = URIRef("http://example.org/has_headers")
        header_rdf_type_uri = URIRef("http://example.org/HTTPHeader")
        header_name_uri = URIRef("http://example.org/headerName")
        header_value_uri = URIRef("http://example.org/headerValue")
        # -prov
        has_source = URIRef("http://example.org/hasPageSource")
        graph = item['graph']

        # Wrap all triples in a 'graph' object
        page_node = BNode()
        out_graph.add((page_node, RDF.type, crawled_page))

        subject_tracker = {}
        for s, p, o in graph:
            if isinstance(s, URIRef):
                if not s in subject_tracker:
                    subject_tracker[s] = BNode()
                    out_graph.add((subject_tracker[s], has_subject, s))
                    out_graph.add((page_node, has_contents, subject_tracker[s]))
                out_graph.add((subject_tracker[s], p, o))
            else:
                out_graph.add((s, p, o))

        # Add HTTP response headers to page object.
        for (header_type, header_value_list) in item['headers'].items():
            for header_value in header_value_list:
                header_bnode = BNode()
                out_graph.add((header_bnode, RDF.type, header_rdf_type_uri))
                out_graph.add((header_bnode, header_name_uri, Literal(header_type.decode())))
                out_graph.add((header_bnode, header_value_uri, Literal(header_value.decode())))
                out_graph.add((page_node, has_header, header_bnode))
        # Add page source (url of fragment/tree:node)
        out_graph.add((page_node, has_source, Literal(item['url'])))

        item['graph'] = out_graph
        return item

# Write the RDF 'page objects' to disk
class RDFWriterPipeline:
    def open_spider(self, spider):
        self.file = open('items.rdf', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if not isinstance(item, RDFPage):
            return item
        self.file.write(adapter.get('graph').serialize(format="ntriples"))
        return item