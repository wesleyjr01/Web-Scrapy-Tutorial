from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from scrapy import Spider
from selenium.common.exceptions import NoSuchElementException
import random
import string
from time import sleep
from scrapy.http import Request
# This spider gets the URLs of the current page, and clicks on the "Next"
# Button to collet data from all the other pages too.
class SeleniumSpider(Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('C:\GitRepos\Web-Scrapy-Tutorial\ScrapingLinkedin\chromedriver.exe')
        self.driver.get('https://www.linkedin.com')
        
        #Login email
        username = self.driver.find_element_by_class_name('login-email')
        username.send_keys('wesleyjr0101@gmail.com')
        sleep(random.uniform(0.46, 0.97))
        
        #Login password
        password = self.driver.find_element_by_class_name('login-password')
        password.send_keys('d134732592889')
        sleep(random.uniform(0.46, 0.97))
        
        #Press sign in
        sign_in_button = self.driver.find_element_by_xpath('//*[@type="submit"]')
        sign_in_button.click()
        sleep(random.uniform(2.74, 4.31))

        yield Request('https://www.linkedin.com/company/intexfy/', callback = self.parse_linkedin)
        
    def parse_linkedin(self, response):
        # Go to intexfy company page
        self.driver.get('https://www.linkedin.com/company/intexfy/')
        
        #Find all recommended pages urls
        list_of_companies = []
        for company_order in range(1,7,1): #We will iterate through 6 companies
            print('\n Started scrapping')
            sleep(random.uniform(0.46, 0.97))
            selec_companies = self.driver.find_element_by_xpath(
                    '//ul[@class="org-similar-orgs__organization-list list-style-none"]/li['+
                    str(company_order)+']/a')
            print('\n',selec_companies)
        #selec_companies2 = driver.find_element_by_xpath('//ul[contains(@class, "org-similar-orgs__organization-list")]/li[2]/a')
        url = selec_companies.get_attribute('href')
        slice_url = str.replace(url,'https://www.linkedin.com/company/','')
        list_of_companies.append(slice_url)
        
        print('\n Start Yieldng')
        #Return URL's domains
        yield{
                'domains':list_of_companies
                }
