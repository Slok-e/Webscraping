from bs4 import BeautifulSoup
import requests
import re

# Request Trader joes Food URL
url = "https://www.traderjoes.com/home/products/category/food-8"
webpage = requests.get(url).text
doc = BeautifulSoup(webpage, "html.parser")

print(doc.prettify)