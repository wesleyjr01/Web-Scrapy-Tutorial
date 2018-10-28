# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = (
        'http://books.toscrape.com/',
    )
    
    #allow will only let the crawler to scrapy URLs from music
#    rules = (Rule(LinkExtractor(allow=('music')),
#                  callback='parse_page', follow=False),)
    
    rules = (Rule(LinkExtractor(),
                  callback='parse_page', follow=False),)

    def parse_page(self, response):
        yield{'URL': response.url}
