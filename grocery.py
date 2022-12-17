from selenium import webdriver

from bs4 import BeautifulSoup
import requests
import re
import time
 
PATH = "/Library/chromedriver"
driver = webdriver.Chrome(PATH)

# Request Trader joes Food URL
driver.get("https://www.traderjoes.com/home/products/category/food-8")



# webpage = requests.get(url).text
# doc = BeautifulSoup(webpage, "html.parser")

# print(doc.prettify)