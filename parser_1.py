import requests

from bs4 import BeautifulSoup

URL = "https://tproger.ru/tag/python/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("div", class_="main__posts-wrapper")
post_id = post.find("article", class_="article")["data-post"]
print(post_id)

title = post.find("h2", class_="article__title article__title--icon").text.strip()
description = post.find("div", class_="article__container-excerpt").text.strip()
url = post.find("a", class_="article__link", href=True)["href"].strip()
#url = "https://habr.com" + url


print(title, description, url, sep="\n\n")

