import scrapy

from crawldf.spiders.tree import TreeSpider

class GipodSpider(TreeSpider):
    name = "kbo"
    # allowed_domains = ["private-api.gipod.beta-vlaanderen.be"]
    start_urls = ["http://localhost:8080/kbo/by-location"]
