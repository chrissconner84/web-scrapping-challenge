#* Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
#* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
#* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
#* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
#  python Example:
#  hemisphere_image_urls = [
     #{"title": "Valles Marineris Hemisphere", "img_url": "..."},
     #{"title": "Cerberus Hemisphere", "img_url": "..."},
     #{"title": "Schiaparelli Hemisphere", "img_url": "..."},
     #{"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def marshemisphere():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://marshemispheres.com'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get a count of the required hemispheres
    hemispheres=soup.find_all('div',class_='item')


    hem_list=[]
    for hem in hemispheres:
        hem_link=hem.a['href']
        nhm=url+'/'+hem_link
        hem_list.append(nhm)  
       
    browser.quit
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    hemisphere_image_urls={}

    index=0
    for h in hem_list:
     index=index+1
     browser.visit(h)
     html2 = browser.html
     soup2 = bs(html2, "html.parser")
     hem_title = soup2.find("h2",class_="title").text
     hem_image=soup2.find('li')
     image=hem_image.a['href']
     image_link=url+'/'+image
     #hemisphere_image_urls.append({"index":index,"title":hem_title,"image_url":image_link})
     hemisphere_image_urls.update({"title"+str(index):hem_title,"image_url"+str(index):image_link})

    browser.quit()

    return hemisphere_image_urls    