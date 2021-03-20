import scrapy


class WikiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    author = scrapy.Field()
    body = scrapy.Field()
    fun_num = scrapy.Field()
    comment_num = scrapy.Field()
