# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

def mission_to_mars():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped

    url = 'https://redplanetscience.com/'

    # open browser to visit page
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Capture the Titles from Latest News (I could have used .find to get the first one)
    results = soup.find_all("div",class_="content_title")
    #Capture the first title
    latest_result=results[0].text

    news_paragraphs = soup.find_all("div",class_="article_teaser_body")
    #Capture the text
    news_text=news_paragraphs[0].text
    print(news_text)

    # Store data in a dictionary
    mission_to_mars_data = {
        "m2mtitle": latest_result,
        "newstext": news_text,
    }
    browser.quit()

    return mission_to_mars_data     