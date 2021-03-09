import requests
from bs4 import BeautifulSoup


res = requests.get(url="https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
tags = soup.select("div h2 strong")

top100 = [tag.string for tag in tags]
print('\n'.join(top100))
