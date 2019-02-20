"""https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html"""

import requests
from bs4 import BeautifulSoup


shameandsurvival = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
req = requests.get(shameandsurvival)
req_html = req.text
soup = BeautifulSoup(req_html, "html.parser")
for title in soup.find_all(class_="content-section"):
    print(title.get_text())
