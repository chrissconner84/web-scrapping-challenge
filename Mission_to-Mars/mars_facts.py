### Mars Facts
# Visit the Mars Facts webpage (https://galaxyfacts-mars.com) and 
#use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.

# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
import splinter
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def mars_facts():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    tables = pd.read_html(url)
    df=tables[1]
    df.rename(columns={0:'Fact Question',1:'Fact Answer'}, inplace = True)
    df

    # Convert the data to a HTML table string.
    html_table = df.to_html()
    

    #Close browser
    browser.quit()

    # Return results
    return html_table