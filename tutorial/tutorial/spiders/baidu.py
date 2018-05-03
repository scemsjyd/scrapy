# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['shenfenzheng.293.net']
    start_urls = ['http://shenfenzheng.293.net/?_t_t_t=0.9766452528640315']

    def parse(self, response):
        node_list = response.xpath("//tr[@bgcolor='#FFFFFF']")
        for node in node_list:
            item = TutorialItem()

            name_id = node.xpath("./td[1]/text()").extract()[0]
            item['name'] = name_id.split(" ")[0]
            item['id_card'] = name_id.split(" ")[1]
            item['gender'] = node.xpath("./td[2]/text()").extract()[0]
            item['age'] = node.xpath("./td[3]/text()").extract()[0]
            item['address'] = node.xpath("./td[4]/text()").extract()[0]

            yield item
