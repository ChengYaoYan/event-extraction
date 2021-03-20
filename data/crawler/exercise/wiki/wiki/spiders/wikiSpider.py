import scrapy

from wiki.items import WikiItem


class WikispiderSpider(scrapy.Spider):
    name = 'wikiSpider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']

    for i in range(1, 3):
        start_urls.append('https://www.qiushibaike.com/8hr/page/' + str(i) + '/')

    def parse(self, response):
        item = WikiItem()

        posts = response.xpath('//div[@class="recommend-article"]/ul/li')

        for post in posts:
            item['author'] = post.xpath()
            item['body'] = post.xpath('//a[@class="recmd-content"]/text()').get()
            recmd_num = post.xpath('//div[@class="recmd-num"]').getall()
            item['fun_num'] = recmd_num[0].get()
            if len(recmd_num) == 2:
                item['comment_num'] = 0
            else:
                item['comment_num'] = recmd_num[3].get()

            yield item
