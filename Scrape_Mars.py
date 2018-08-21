
# coding: utf-8

# In[11]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import time 
import os


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)
print(browser)


# ## Visit the NASA mars news site
# 

# In[14]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[15]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[16]:


slide_elem.find("div", class_='content_title')


# In[17]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = news_soup.find("div",class_="content_title").text
print("Title: {news_title}")


# In[18]:


# Use the parent element to find the paragraph text
news_paragraph = news_soup.find("div", class_="article_teaser_body").text
print("Para: {news_paragraph}")


# ## JPL Space Images Featured Image

# In[19]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[20]:


# Find and click the full image button
browser.find_by_id('full_image').click()
featured_image_url = browser.find_by_css('.fancybox-image').first['src']
print(featured_image_url)


# ## Mars Weather
# 

# In[21]:


url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[22]:


html_weather = browser.html
soup = BeautifulSoup(html_weather, "html.parser")
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# ## Mars Facts

# In[23]:


url = 'https://space-facts.com/mars/'
browser.visit(url)


# In[24]:


table = pd.read_html(url)
table [0]


# In[25]:


df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[26]:


mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# Hemispheres

# In[33]:


url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[34]:


html = browser.html
soup = BeautifulSoup('html.parser')
mars_hemispheres = []


# In[35]:


for i in range (4):
    time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemispheres.append(dictionary)
    browser.back()


# In[36]:


print(mars_hemispheres)

