# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ProxyPipeline:
    def process_item(self, item, spider):
        with open('proxies.txt', 'a') as file_object:
            file_object.write(item['address'] + '\n')

        return item
