#* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).

#* Use splinter to navigate the site and find the image url for the current Featured Mars Image and
#* assign the url string to a variable called `featured_image_url`.

#* Make sure to find the image url to the full size `.jpg` image.

#* Make sure to save a complete url string for this image.

#```python
# Example:
#featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
#```

# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def mars_space_image():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Capture the featured image
    fi = soup.find("img",class_="headerimage")
    fi_image=fi['src']
    featured_image_url=url+'/'+fi_image

    browser.quit()
    fi_url_dict = {"fi_url": featured_image_url} 
    return fi_url_dict
   