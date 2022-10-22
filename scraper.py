# Search for Multiple Products/ a specific product on on multiple websites to gain a better analasys of a Product. In this example we are searching for search_terms
# This can be used for multiple applications, like E-Commerce, product performance comparisaon, 
from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# Breakdown of getting the amount of pages for the searched topic,item,product,etc.
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

# Loops through the pages to search all the pages available for the searched term.
for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    
    # On Newegg Specifically this is the class we search for in order to hone in on the elements of the search resuls
    # ,which are in a div flex container.
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))
    for item in items:
        parent = item.parent
        link = None
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price']) 

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("--------------------------------")






# prices = {}

# for tr in trs[:10]:
#     name, price = tr.contents[2:4]
#     fixed_name = name.p.string
#     fixed_price = price.a.string 

#     prices[fixed_name] = fixed_price

# print(prices)