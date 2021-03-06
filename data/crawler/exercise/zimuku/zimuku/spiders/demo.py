import scrapy

from zimuku.items import ZimukuItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['http://zimuku.net/']
    start_urls = ['http://http://zimuku.net//']

    def parse(self, response):
    	name = response.xpath('//b/text()').extract()[1]

    	items = {}
    	items['first'] = name

    	return items
