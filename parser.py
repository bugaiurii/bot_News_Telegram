import requests

from bs4 import BeautifulSoup

URL = "https://habr.com/ru/search/?target_type=posts&q=python&order_by=date"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("article", class_="tm-articles-list__item", id=True)
post_id = post["id"]
print(post_id)

title = post.find("a", class_="tm-article-snippet__title-link").text.strip()
#description = post.find("div", class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
url = post.find("a", class_="tm-article-snippet__title-link", href=True)["href"].strip()
url = "https://habr.com" + url


print(title, url, sep="\n\n")
