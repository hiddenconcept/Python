#import everything

from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

#setup urls
user_url = str(input("Enter the URL of the website you want to scrape: "))
urls = deque()
#user_response = requests.get(user_url)
#user_soup = BeautifulSoup(user_response.content, 'lxml')

#define some stuff
scraped_urls = set()
emails = set()
count = 0
try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url =urls.popleft()
        scraped_urls.add(url)

