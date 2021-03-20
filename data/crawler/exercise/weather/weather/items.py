import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    week = scrapy.Field()
    img = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
