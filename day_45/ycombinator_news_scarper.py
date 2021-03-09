import requests
from bs4 import BeautifulSoup

res = requests.get(url="https://news.ycombinator.com/")
res.raise_for_status()
page_html = res.text

soup = BeautifulSoup(page_html, "html.parser")

all_a_tags = soup.select(".storylink")
all_span_tags = soup.find_all(name='span', class_="score")

# print(all_span_tags)

all_news = [(a.getText(), a.get("href")) for a in all_a_tags]
all_points = [int(span.string.split(' ')[0]) for span in all_span_tags]
news_dict = dict(zip(all_points, all_news))
print(dict(zip(all_points, all_news)))

print(all_points)
max_points = max(all_points)
print(max_points)
print(f"Most popular Headline is: {news_dict[max_points]}")


