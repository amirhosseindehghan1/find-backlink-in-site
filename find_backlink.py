# modules
from colorama import Back
import requests
from bs4 import BeautifulSoup

# set  windows
from colorama import init

init()

# page url
url = r"https://www.jetrender.ir/"

# send get request
response = requests.get(url)

# parse html page
html_page = BeautifulSoup(response.text, "html.parser")

# get all  tags
all_urls = html_page.findAll("a")

internal_urls = set()
external_urls = set()

for link in all_urls:
    href = link.get('href')

    if href:
        if r"jetrender.ir" in href:  # internal link
            internal_urls.add(href)

        elif href[0] == "#":  # same page target link
            internal_urls.add(f"{url}{href}")

        else:  # external link
            external_urls.add(href)

print(Back.MAGENTA + f"Total External URLs: {len(internal_urls)}\n")
for url in internal_urls:
    print(Back.GREEN + f"Internal URL {url}")

print(Back.MAGENTA + f"\n\nTotal External URLs: {len(external_urls)}\n")
for url in external_urls:
    print(Back.RED + f"External URL {url}")