# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from adv_spider.items import AdvSpiderItem

class AdvspiderSpider(Spider):
    name = 'using_itemsdotpy'
#    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

     #this Request is called when there are no explicity callback
    def parse(self, response):
        loader = ItemLoader(item=AdvSpiderItem(), response=response)
        
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        
        loader.add_value('h1_tag', h1_tag)
        loader.add_value('tags', tags)

        return loader.load_item()