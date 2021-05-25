#! python3
# link_verification.py - Verifies if a given page has any broken links

import requests, bs4, sys

page = sys.argv[1]
res = requests.get(page)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

atags = soup.select('a')
broken_links = []
# Cause one of the sites I tested complained about it with 403:(
chrome_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
for tag in atags:
    url = tag.get('href')
    if url == None: break
    if not ('.' in url and '/' in url): break 
    if not (url.startswith('http:') or url.startswith('https:')):
        url = 'https:' + url
    print('Looking up %s:' %url)
    res = requests.get(url, headers={'User-Agent': chrome_user_agent})
    if not res.status_code == 200:
        broken_links.append(url)
        print('\tFound %s to be broken, returning %d status code.' %(url, res.status_code))
        continue
    print('\t%s seems to be ok.' %url)

print()
print('Found %d broken links.' %len(broken_links))
print('Done.')