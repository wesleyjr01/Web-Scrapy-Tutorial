# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

# This spider gets the URLs of the current page, and clicks on the "Next"
# Button to collet data from all the other pages too.
# Not going to use Selenium.
class SeleniumSpider(Spider):
    name = 'bookstore2'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


            
    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)
            
        # process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page = response.urljoin(next_page_url)
        yield Request(absolute_next_page, callback = self.parse)
            
    def parse_book(self, response):
        title = response.xpath('//h1/text()').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()
        
        rating = response.xpath('//*[contains(@class,"star-rating")]/@class').extract_first()
        rating = rating.replace('star-rating ','')
        yield{"URL": response.url,
              "title": title,
              "price": price,
              "rating": rating
              }