# web scraping

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"

page = requests.get(url)
print(page)  # prints the response
# print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

# find data by tag name
# find method just gets the first one
title = soup.find('title')  # title is just the tag name
print(title)
print(title.text)
