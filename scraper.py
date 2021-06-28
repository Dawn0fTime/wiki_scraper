#!/bin/python3
# scraper.py
# The scraper will go to a Wikipedia page, scrape the title, and follow
# a random link to the next Wikipedia page.

import requests
from bs4 import BeautifulSoup
import random
import time

BASE_URL = 'https://en.wikipedia.org'


def scrape_wiki_article(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='firstHeading')
    print(title.text)

    # Get all the links
    all_links = soup.find(id='bodyContent').find_all('a')
    random.shuffle(all_links)
    link_to_scrape = 0

    for link in all_links:
        # We are only interested in other wiki articles
        if link['href'].find('/wiki/') == -1:
            continue

        # Use this link to scrape
        link_to_scrape = link
        break

    # Wait for 5 so user has time to kill the app
    time.sleep(5)
    scrape_wiki_article(BASE_URL + link_to_scrape['href'])


scrape_wiki_article(BASE_URL + '/wiki/Web_scraping')
