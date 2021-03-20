# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WikiPipeline:
    def process_item(self, item, spider):
        with open('wiki.txt', 'a+') as file_object:
            file_object.write(f'author: {item["author"]} body: {item["body"]} fun_num: {item["fun_num"]} comment_num: {item["comment_num"]} \n')
            
