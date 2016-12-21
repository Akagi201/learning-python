#!/usr/bin/env python

import requests, os, threading
from bs4 import BeautifulSoup as bs

""" XKCD Comics Downloader using threading which downloads multiple comics at a time. """

url = 'http://xkcd.com'

""" Check if the Folder xkcd exist or not. If not then create a xkcd folder."""
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')

""" Download Each page untill end of url has # is reached and is between page number startComic and endComic. """


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = bs(res.text, "html.parser")
        """ Select the img tag with comic id to download ."""
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:

            comicUrl = comicElem[0].get('src')
            print('Downloading image %s...' % comicUrl)
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()  # Check for url status
            """ Check if File already exist in xkcd folder or not ."""
            if not os.path.isfile(os.path.join('xkcd', os.path.basename(comicUrl))):
                # os.path.basename(comicUrl) takes the last part of the url.
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                # Downloading chunks of file data and saving it.
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()


downloadThreads = []
# Downloading page from 0 to 1400 at difference of 100 pages.
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done')
