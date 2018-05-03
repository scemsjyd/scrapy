# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TutorialPipeline(object):

    def __init__(self):
        self.f = open("data.json", "w")

    def process_item(self, item, spider):
        # 使用管道处理item
        content = json.dumps(dict(item), ensure_ascii=False) + ", \n"
        print("--" * 80)
        print(content)
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
