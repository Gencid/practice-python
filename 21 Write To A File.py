"""https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html"""

import requests
from bs4 import BeautifulSoup


nyt_url = 'https://www.nytimes.com/'
r = requests.get(nyt_url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
titlelist = []
for title in soup.find_all("h2", class_="esl82me2"):
    titlelist.append(title.text)
titlestring = str(titlelist)
print("Give me a name and I will take all the article titles from the New York Times page\n"
      "and save them in a txt file.")
filename = input("So, how shall the txt be named?\n>")
with open("{}.txt".format(filename), "w") as write_to_file:
    write_to_file.write(titlestring)
