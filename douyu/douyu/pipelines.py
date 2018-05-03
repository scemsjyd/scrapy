# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
from douyu.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):
    # 重写请求
    def get_media_requests(self, item, info):
        image_link = item['image']
        yield scrapy.Request(image_link)

    # 重写图片名称
    def item_completed(self, results, item, info):
        path = [x['path'] for ok, x in results if ok]
        os.rename(images_store + path[0], images_store + 'full/' +
                  item['nick_name'] + '.jpg')
        return item
