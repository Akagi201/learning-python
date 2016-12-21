#!/usr/bin/env python

import requests, os
from bs4 import BeautifulSoup as bs

""" XKCD Comics Downloader using BeautifulSoup which downloads comics and save to xkcd folder. """

url = 'http://xkcd.com'

""" Check if the Folder xkcd exist or not. If not then create a xkcd folder."""
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')

""" Download Each page untill end of url has # is reached """
while not url.endswith('#'):

    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs(res.text, "html.parser")

    comicElem = soup.select('#comic img')
    """ Select the img tag with comic id to download ."""
    if comicElem == []:
        print('Could not find comic image.')
    else:

        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()  # Check for url status

        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        """ Check if File already exist in xkcd folder or not ."""
        if not os.path.isfile(os.path.join('xkcd', os.path.basename(comicUrl))):
            # os.path.basename(comicUrl) takes the last part of the url.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            # Downloading chunks of file data and saving it.
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        """ Find prev link and continue Downloading. """
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

print('Done')
