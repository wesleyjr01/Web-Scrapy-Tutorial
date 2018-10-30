# In[]:
import requests
page = requests.get("https://www.linkedin.com/company/intexfy/")
print(page.status_code)
print(page.content)

# In[]:
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# In[]: Check nested levels
list(soup.children)

# In[]: Find all instances at once
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all(class_="org-similar-orgs__organization-list list-style-none")

# In[]
print( soup.find_all(id="ember5779") )
