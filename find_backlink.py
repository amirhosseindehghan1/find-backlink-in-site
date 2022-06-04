import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlsplit
import re
ext = set()
def getExt(url):
    o = urllib.parse.urlsplit(url)
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^((https://)|(http://))')):
        if 'href' in link.attrs:
            if o.netloc in (link.attrs['href']):
                continue
            else:
                ext.add(link.attrs['href'])
getExt('https://jetrender.ir')
for i in ext:
    print(i)