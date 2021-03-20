import scrapy

from weather.items import WeatherItem


class TyweatherSpider(scrapy.Spider):
    name = 'TYWeather'
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    allowed_domains = ['tianqi.com']
    start_urls = []
    cities = ['taiyuan']

    for city in cities:
    	start_urls.append('https://www.tianqi.com/' + city)

    def parse(self, response):
        items = []

        week = response.xpath('//div[@class="day7"]/ul[@class="week"]/li/span/text()').getall()
        date = response.xpath('//div[@class="day7"]/ul[@class="week"]/li/b/text()').getall()
        img = response.xpath('//div[@class="day7"]/ul[@class="week"]/li/img/@src').getall()
        temperature = response.xpath('//div[@class="day7"]/div[@class="zxt_shuju"]/ul/li/span/text()').getall()
        weather = response.xpath('//div[@class="day7"]/ul[@class="txt txt2"]/li/text()').getall()
        wind = response.xpath('//div[@class="day7"]/ul[@class="txt"]/li/text()').getall()

        for day in range(7):
            item = WeatherItem()
            item['week'] = week[day]
            item['date'] = date[day]
            item['img'] = 'https:' + img[day]
            item['temperature'] = temperature[day]
            item['weather'] = weather[day]
            item['wind'] = wind[day]

            items.append(item)
            
        return items
