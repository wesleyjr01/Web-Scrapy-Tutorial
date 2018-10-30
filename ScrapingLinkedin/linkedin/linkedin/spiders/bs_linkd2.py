
# In[] BeautifulSoup with selenium
from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome('C:\GitRepos\Web-Scrapy-Tutorial\ScrapingLinkedin\chromedriver.exe')
driver.get('https://www.linkedin.com')

username = driver.find_element_by_class_name('login-email')
username.send_keys('wesleyjr0101@gmail.com')
sleep(random.uniform(0.46, 0.97))

#Login password
password = driver.find_element_by_class_name('login-password')
password.send_keys('d134732592889')

#Press sign in
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(random.uniform(2.74, 4.31))

# BeautifulSoup
driver.get('https://www.linkedin.com/company/intexfy/')
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html) # Check

# Get elements with Bs
all_tags = soup.find_all(
        class_="org-similar-orgs__organization-card org-right-rail-list__list-item relative pl4 pr4 mb5")

handles = []
for tag_order in range(len(all_tags)):
    tag = all_tags[tag_order]
    url = [a['href'] for a in tag.find_all('a', href=True) if a.text][0]
    handle = str.replace(url,'/company/','')[:-1] # Remove '/company/' from url
    handles.append(handle)