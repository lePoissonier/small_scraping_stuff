# basically retrieving urls from web pages

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Aun.html'
count = 7
position = 18


for _ in range(0, count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.findAll('a')
    print("Retrieving: ", url)

    for tag in tags:
        url = tag.get('href')
        url = tags[position - 1].get('href')

print("Retrieving: ", url)