# -*- coding: utf-8 -*-
import scrapy
import json

from panda.items import PandaItem


class PhotoSpider(scrapy.Spider):
    name = 'photo'
    allowed_domains = ['web.api.xingyan.panda.tv']
    prefix_url = 'https://web.api.xingyan.panda.tv/room/list?xtype=0&pageno='
    suffix_url = '&pagenum=50&_=1527668502536&__plat=pc_web&__version=1.3.6'
    offset = 1
    start_urls = [prefix_url + str(offset) + suffix_url]

    def parse(self, response):
        body = json.loads(response.body)
        if body['errno'] == 0:
            data = body['data']
            items = data['items']
            for item in items:
                panda_item = PandaItem()
                panda_item['nickName'] = item['nickName']
                photourl = item['s_photo']
                panda_item['photo'] = photourl
                if photourl.startswith('https'):
                    yield panda_item

        if self.offset <= 50:
            self.offset += 1
            next_url = self.prefix_url + str(self.offset) + self.suffix_url
            yield scrapy.Request(next_url)
        pass
