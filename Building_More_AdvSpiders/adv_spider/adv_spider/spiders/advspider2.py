# -*- coding: utf-8 -*-
import scrapy

class AdvspiderSpider(scrapy.Spider):
    name = 'advspider2'
#    allowed_domains = ['quotes.toscrape.com']
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
                    'Tags':tags[quote],
                    }
            
        next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
        next_page_join = response.urljoin(next_page)
        print('\n Next Page:',next_page)
        yield scrapy.Request(next_page_join, callback = self.parse)

