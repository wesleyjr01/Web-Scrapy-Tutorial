# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request

# This spider gets the URLs of only the first page.
class SeleniumSpider(Spider):
    name = 'selenium'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('C:\GitRepos\Web-Scrapy-Tutorial\Scrapy_With_Selenium\chromedriver.exe')
        self.driver.get('http://books.toscrape.com')
        
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract() #only a part of URL is returned here
        
        for book in books:# Complete the URLs
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)
            
    def parse_book(self, response):
        pass