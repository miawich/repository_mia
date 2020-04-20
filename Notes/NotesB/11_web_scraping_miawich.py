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
title = soup.find("title")  # title is just the tag name
print(title)
print(title.text)

# by attribution
print()
authors = soup.find_all(itemprop="author")
print(authors)

for author in authors:
    print(author.text)

# by css class
print()
quotes = soup.find_all(class_="quote")
print(quotes[0].prettify())

# drill down using dot notation
print()
print(quotes[0].span.text)

for quote in quotes:
    print(quote.span.text)

# use authors and quotes together
print()
for i in range(len(quotes)):
    print(quotes[i].span.text)
    print("\t\t---{}".format(authors[i].text))


quotes = soup.find_all("span", class_="text", itemprop="text")

for quote in quotes:
    print(quote.text)