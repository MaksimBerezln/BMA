import telebot

bot = telebot.TeleBot('1375519031:AAFLYEf1wfICAZykqtcb5bwlbmXEPx1Xh1s')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Сколько нужно?')

@bot.message_handler(commands=['2'])
def start_message(message):
    bot.send_message(message.chat.id, 'Назначено 2')


@bot.message_handler(commands=['3'])
def start_message(message):
    bot.send_message(message.chat.id, 'Назначено 3')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введи 2 или 3')

bot.polling()
