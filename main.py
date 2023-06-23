import os
import telebot
import logging
from flask import Flask, request
BOT_TOKEN = '5778096365:AAE5rXAYGc2L-cQd7fyOgfzP2ckrzkQfJVc'

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def start(message):
   username = message.from_user.username
   bot.reply_to(message, f'Hi, {username}')

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
   json_string = request.get_data().decode("utf-8")
   update = telebot.types.Update.de_json(json_string)
   bot.process_new_updates([update])
   return "!", 200


if __name__ == "__main__":
   bot.remove_webhook()
   server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


