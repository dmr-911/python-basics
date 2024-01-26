import requests
from bs4 import BeautifulSoup

url = "https://www.cdda.io"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser') # parse whole page html
for heading in soup.find_all("h2"): # find h2 in the static page
    print(heading.text)

