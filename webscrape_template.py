# All libraries for either web or local file. If scraping a downlowaded file make sure it is in the same
# directory as the python scrape script
from bs4 import BeautifulSoup
import requests
import re

# Copy and paste url between quotes for webscraping.
url = "url"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")