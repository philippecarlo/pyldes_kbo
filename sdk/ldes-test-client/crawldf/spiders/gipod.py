import scrapy

from crawldf.spiders.tree import TreeSpider

class GipodSpider(TreeSpider):
    name = "gipod"
    allowed_domains = ["private-api.gipod.beta-vlaanderen.be"]
    start_urls = ["https://private-api.gipod.beta-vlaanderen.be/api/v1/ldes/mobility-hindrances"]
