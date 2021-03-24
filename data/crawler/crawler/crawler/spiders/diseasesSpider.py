import scrapy

class DiseasesSpider(scrapy.Spider):
    name = "diseases"

    start_urls = [
        'https://baike.baidu.com/item/%E6%84%9F%E5%86%92/502565'
    ]

    def parse(self, response):
        para = ''.join(response.css('div.lemma-summary div.para *::text').getall())
        print(para)
