# BeautifulSoup Tutorial
# https://www.dataquest.io/blog/web-scraping-tutorial-python/

# In[]:
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
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
soup.find_all('p')
# Returned a list
soup.find_all('p')[0].get_text()

# In[]: Search for tags by class and ID
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup

# In[]:
soup.find_all('p', class_='outer-text')

# In[]:
soup.find_all(class_="outer-text")

# In[]:
soup.find_all(id="first")

# In[]:
soup.select("div p")

# In[]: Extract Information
# Extract and print the first forecast item.
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

# Extract 4 pieces of information
# The name of the forecast item
period = tonight.find(class_="period-name").get_text()

# The description of the conditions
short_desc = tonight.find(class_="short-desc").get_text()

# The temperature low
temp = tonight.find(class_="temp").get_text()

# In[]: Extracting all the information from the page
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)