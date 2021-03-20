import scrapy

from proxy.items import ProxyItem


class FastspiderSpider(scrapy.Spider):
    name = 'fastSpider'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = []

    for i in range(1, 6):
        start_urls.append('https://www.kuaidaili.com/free/inha/' + str(i) + '/')

    def parse(self, response):
        item = ProxyItem()
        items = []

        proxies = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

        for proxy in proxies:
            ip = proxy.xpath('td/text()').getall()[0]
            port = proxy.xpath('td/text()').getall()[1]

            item['address'] = ip + ':' + port
            items.append(item)

        return items

