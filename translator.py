import telebot
import requests

bot = telebot.TeleBot('875453514:AAGOHpF7rSksQAzb7YqcpCaj0ycA_iOE1Gg')
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
key = "yandex translator key"
temp=0


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'type help')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if temp==0:
        params = {
            "key": key,
            "text": message,
            "lang": 'ru-en'
        }
        response = requests.get(URL, params=params)
    else:
        params = {
            "key": key,
            "text": message,
            "lang": 'en-ru'
        }
        response = requests.get(URL, params=params)
    return response.json()

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'commands:\n/ru с русского на англ\n/en с англ на русский')

@bot.message_handler(commands=['ru'])
def ru_message(message):
    temp=0
    bot.send_message(message.chat.id, 'perevodim s rus na angl')

@bot.message_handler(commands=['en'])
def ru_message(message):
    temp=1
    bot.send_message(message.chat.id, 'perevodim s en na ru')


bot.polling()
