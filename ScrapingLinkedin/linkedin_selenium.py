from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome('C:\GitRepos\Web-Scrapy-Tutorial\ScrapingLinkedin\chromedriver.exe')

driver.get('https://www.linkedin.com')

username = driver.find_element_by_class_name('login-email')
username.send_keys('wesleyjr0101@gmail.com')
sleep(random.uniform(0.46, 0.97))

password = driver.find_element_by_class_name('login-password')
password.send_keys('d134732592889')
sleep(random.uniform(0.46, 0.97))

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(random.uniform(2.74, 4.31))

# In[]: Google Search
#driver.get('https://www.google.com/')
#search_query = driver.find_element_by_name('q') #Google Search Box
#search_query .send_keys('site:linkedin.com/in/ AND "python" AND "Florianópolis"')
#
## Click button to search, or send ENTER
##search_button = driver.find_element_by_name('btnK') #Google Search Button
##search_button.click()
#search_query.send_keys(Keys.RETURN)
#random.uniform(2.74, 4.31)

# In[]: Linkedin Companies Search

driver.get('https://www.linkedin.com/company/intexfy/')

# Click in the first recommended company page
#next_company = driver.find_element_by_class_name('org-similar-orgs__organization-card')
#next_company.click()

# In[]: Testes XPath
all_companies = driver.find_element_by_xpath('//ul[@class="org-similar-orgs__organization-list list-style-none"]')
#driver.find_element_by_xpath('//div[@class="ember-view"]').text #Mostra todas as empresas

list_of_companies = []
for company_order in range(1,7,1): #We will iterate through 6 companies
    selec_companies = driver.find_element_by_xpath(
            '//ul[@class="org-similar-orgs__organization-list list-style-none"]/li['+
            str(company_order)+']/a')
#selec_companies2 = driver.find_element_by_xpath('//ul[contains(@class, "org-similar-orgs__organization-list")]/li[2]/a')
    url = selec_companies.get_attribute('href')
    slice_url = str.replace(url,'https://www.linkedin.com/company/','')
    list_of_companies.append(slice_url)
    

#company_tag = elem = driver.find_element_by_xpath('//ul[@class="org-similar-orgs__organization-list list-style-none"]/li[@class="org-similar-orgs__organization-card org-right-rail-list__list-item relative pl4 pr4 mb5"]/a')
#href = company_tag.get_attribute('href')
#
#href = str.replace(href,'https://www.linkedin.com/company/','')
