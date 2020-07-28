#!/usr/bin/env python3

import urllib3
from bs4 import BeautifulSoup

def imgsearch(url):
    print(f"[+] Finding images from: {url}")
    urlContent = url.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

