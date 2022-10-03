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

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("article", class_="tm-articles-list__item", id=True)
    post_id = post["id"]

    if post_id != back_post_id:
        title = post.find("a", class_="tm-article-snippet__title-link").text.strip()
        #description = post.find("div", class_="post__text post__text-html post__text_v1").text.strip()
        url = post.find("a", class_="tm-article-snippet__title-link", href=True)["href"].strip()
        url = "https://habr.com" + url

        return f"{title}\n\n{url}", post_id
    else:
        return None, post_id

bot.polling()