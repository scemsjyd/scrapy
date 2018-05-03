# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.douyu.com']
    base_url = "https://www.douyu.com/gapi/rkc/directory/1_8/"
    offset = 1
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        body = json.loads(response.body)
        if body['code'] == 0 and body['msg'] == 'success':

            data = body['data']
            data_list = data['rl']
            pgcnt = data['pgcnt']

            for list in data_list:
                item = DouyuItem()
                item['nick_name'] = list['nn']
                item['image'] = list['rs1']
                yield item
            if self.offset <= pgcnt:
                self.offset += 1
                nextpage = self.base_url + str(self.offset)
                yield scrapy.Request(nextpage)
        # pass
