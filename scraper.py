from flask import Flask

def save(html, path):
    with open(path, 'wb') as f:
        f.write(html)

def open(path):
    with open(path, 'rb') as f:
        return f.read()

# Import Libraries
import requests
from bs4 import BeautifulSoup

# Get page content
page_url = "https://books.toscrape.com/"
getWebsite = requests.get(page_url)

soup = BeautifulSoup(getWebsite.content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))