# -*- coding: utf-8 -*-
from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException

# This spider gets the URLs of the current page, and clicks on the "Next"
# Button to collet data from all the other pages too.
class SeleniumSpider(Spider):
    name = 'selenium2'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('C:\GitRepos\Web-Scrapy-Tutorial\Scrapy_With_Selenium\chromedriver.exe')
        self.driver.get('http://books.toscrape.com')
        
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract() #only a part of URL is returned here
        
        for book in books:# Complete the URLs
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)
        
        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds.')
                next_page.click()
                
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract() #only a part of URL is returned here
                
                for book in books:# Complete the URLs
                    url = 'http://books.toscrape.com/catalogue/' + book
                    yield Request(url, callback=self.parse_book)
                
            except NoSuchElementException:
                self.logger.info('No More Pages to Load.')
                self.driver.quit()
                break
            
    def parse_book(self, response):
        pass