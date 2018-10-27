# -*- coding: utf-8 -*-
import scrapy


class AdvspiderSpider(scrapy.Spider):
    name = 'advspider'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

     #this Request is called when there are no explicity callback
    def parse(self, response):
        
        quotes = response.xpath('//*[@class="quote"]/*[@class="text"]/text()').extract()    
        authors = response.xpath('//*[@class="author"]/text()').extract()
        tags = response.xpath('//*[@class="keywords"]/@content').extract()
       
        for quote in range(len(quotes)):
            yield {
                    'Quote': quotes[quote],
                    'Author': authors[quote],
                    'Tags':tags[quote]
                    }
