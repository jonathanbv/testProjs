#pulls <body> from html page
from bs4 import BeautifulSoup as Bsoup
from lxml import html
import requests

URL = input("Enter URL to be ripped:")
page = requests.get(URL)
wholePage = html.fromstring(page.content)
soup = Bsoup(wholePage, 'html.parser')

print(soup.prettify())
