import telebot
import requests
import time

from bs4 import BeautifulSoup

token = "5624381923:AAFaZvIKE7FY6Mr5bAbKid684RWyNANUlgs"
id_channel = "@News_of_Mine"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def commanands(message):
    if message.text == "Старт":
        back_post_id = None
        while True:
            post_text = parser(back_post_id)
            back_post_id = post_text[1]

            if post_text[0] != None:
                bot.send_message(id_channel, post_text[0])
                time.sleep(1800)
    else:
        bot.send_message(message.from_user.id, "Моя твоя не панимать. Напиши Старт")

def parser(back_post_id):
    URL = "https://habr.com/ru/search/?target_type=posts&q=python&order_by=date"
    URL_1 = "https://tproger.ru/tag/python/"

    page = requests.get(URL)
    page_1 = requests.get(URL_1)
    soup = BeautifulSoup(page.content, "html.parser")
    soup_1 = BeautifulSoup(page_1.content, "html.parser")

    post = soup.find("article", class_="tm-articles-list__item", id=True)
    post_1 = soup_1.find("main", class_="main")
    post_id = post["id"]
    post_id_1 = post_1.find("article", class_="article")["data-post"]

    if post_id != back_post_id or post_id_1 != back_post_id:
        title = post.find("a", class_="tm-article-snippet__title-link").text.strip()
        title_1 = post_1.find("h2", class_="article__title article__title--icon").text.strip()
        description_1 = post_1.find("div", class_="article__container-excerpt").text.strip()
        #description = post.find("div", class_="post__text post__text-html post__text_v1").text.strip()
        url = post.find("a", class_="tm-article-snippet__title-link", href=True)["href"].strip()
        url = "https://habr.com" + url
        url_1 = post_1.find("a", class_="article__link", href=True)["href"].strip()

        return f"{title}\n\n{url}\n\n{title_1}\n\n{description_1}\n\n{url_1}", post_id, post_id_1
    else:
        return None, post_id, post_id_1

bot.polling()