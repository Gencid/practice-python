"""https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html"""

import requests
from bs4 import BeautifulSoup


nyt_url = 'https://www.nytimes.com/'
r = requests.get(nyt_url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
titlelist = []
for title in soup.find_all("h2"):
    titlelist.append(title.text)
print(titlelist)
