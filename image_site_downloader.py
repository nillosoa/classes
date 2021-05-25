#! python3
# image_site_downloader.py - Search for a given term on Flickr and downloads all images from it

import requests, bs4, sys, os

term = sys.argv[1]
url = 'https://www.flickr.com/search/?text=' + term

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

selectors = soup.select('div.photo-list-photo-view')

path = os.path.join('FlickrDownloads', term)
os.makedirs(path, exist_ok=True)
# Flickr makes use of javascript to update it's divs with images,
# using Chrome with JS disabled, I've found that the images urls are also sent
# on divs with 'photo-list-photo-view' classes with the inline style(background-image).
for i in range(len(selectors)):
    style = str(selectors[i].get('style'))
    style_background = str(style.split('background-image: url(')[1].replace(')', ''))
    style_background_id = style_background[style_background.rfind('/') + 1:] #For naming the file
    print("\tTrying to get https:%s..." %style_background)

    res = requests.get('https:' + style_background)
    res.raise_for_status()
    with open(path + os.sep + style_background_id, 'wb') as image_file:
        print('\t\tWriting %s to file...' %style_background_id)
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

print('Done.')