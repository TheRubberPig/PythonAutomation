#! python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

# Starting URL
url = 'https://xkcd.com'
# Store comics in ./xkcd, exist_ok prevents the script throwing an error if the directory already exists
os.makedirs('xkcd', exist_ok=True)
# Changed the loop to download the last 20 comics for testing, replacing the loop with the line below would download all of them
#while not url.endswith('#'):
i = 0
while i <= 20:
    # Download the webpage
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Find the url of the comic image
    comicElement = soup.select('#comic img')
    if comicElement == []:
        print('Could not find comic image')
    else:
        comicUrl = 'https:' + comicElement[0].get('src')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    i += 1

print('Done.')