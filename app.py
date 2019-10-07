import telebot

bot = telebot.TeleBot('875453514:AAGOHpF7rSksQAzb7YqcpCaj0ycA_iOE1Gg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'asd or sth else')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'asd':
        bot.send_message(message.chat.id, 'yes')
    else: bot.send_message(message.chat.id, 'nope')


@bot.message_handler(commands=['start'])
def start(message):
    print(message)


bot.polling()