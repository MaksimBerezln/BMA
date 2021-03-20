import telebot

from telebot import types

bot = telebot.TeleBot('1375519031:AAFLYEf1wfICAZykqtcb5bwlbmXEPx1Xh1s')

@bot.message_handler(content_types=["edy"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text=" ", url="https://vimvd.ru/education/%D0%A018%D0%911,%20%D0%A018%D0%9A1,%20%D0%A018%D0%9A2%20%D0%BE%D1%82%2015.03%20%D0%BD%D0%B0%20%D1%81%D0%B0%D0%B9%D1%82.pdf")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми и прейдешь на сайт с расписанием.", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello mother fucked')


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
