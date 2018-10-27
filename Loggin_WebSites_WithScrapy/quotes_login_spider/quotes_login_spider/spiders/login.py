# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        
        
        yield FormRequest('http://quotes.toscrape.com/login',
                          formdata={'csrf_token': csrf_token,
                                    'username':'asdf',
                                    'password':'asdf'},
                                    callback=self.parse_after_login)
        
    def parse_after_login(self, response): #Here we check if we succeded in login
        if response.xpath('//a[text()="Logout"]'):
            print('\n You logged in!')