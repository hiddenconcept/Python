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

        parts = urllib.parse.urlparse(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[url.rfind('/')+1:] if '/' in url else url

        print('[%d/%d] Scraping: %s' % (count, len(urls), url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+',response.text , re.IGNORECASE))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text,"lxml")

        for anchor in soup.find_all('a'):
            link = anchor.get('href') if 'href'in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = base_url + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)




