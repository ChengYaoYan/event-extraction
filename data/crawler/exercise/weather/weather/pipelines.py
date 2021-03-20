import os
import requests
import json
import codecs
import pymysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeatherPipeline:
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.txt'

        with open(filename, 'a') as file_object:
            file_object.write(item['date'] + '\n')
            file_object.write(item['week'] + '\n')
            file_object.write(item['temperature'] + '\n')
            file_object.write(item['weather'] + '\n')
            file_object.write(item['wind'] + '\n\n')

        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as file_object:
            file_object.write(requests.get(item['img']).content)

        return item


class WeatherPipelineJson:
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        with codecs.open(filename, 'a') as file_object:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file_object.write(line)

        return item            


class WeatherPipelineMysql:
    def process_item(self, item, spider):
        date = item['date']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']
        img = item['img']

        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'wdthsl110711//',
            db = 'scrapyDB',
            charset = 'utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )

        try:
            with connection.cursor() as cursor:

                sql = """ INSERT INTO weather(date, week, temperature, weather, wind, img) 
                        VALUES (%s, %s, %s, %s, %s, %s) """
                cursor.execute(sql, (date, week, temperature, weather, wind, img))

            connection.commit()
        finally:
            connection.close()
        return item