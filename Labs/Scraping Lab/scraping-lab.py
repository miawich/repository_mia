# SCRAPING PROBLEMS
# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

#  print("{} {}!".format("Hello", "World"))
import time
import urllib.request
import certifi
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
twitter_url = "https://twitter.com/StephenAtHome"

driver = webdriver.Chrome("/Users/miawichman/PycharmProjects/P2_SP20/Labs/Scraping Lab/chromedriver")
driver.implicitly_wait(10)
driver.get(twitter_url)   # hey mr lee, i have a virus on my chrome so i am not sure if it actually works


last_height = driver.execute_script("return document.body.scrollHeight")
x = 0
pages_to_scroll = 30

while x < pages_to_scroll:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    x += 1

    time.sleep(1)  # seconds to let it load the new posts

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # reached the bottom or maybe didn't load
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())

# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()



