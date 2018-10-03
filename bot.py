import requests
import telebot
from telebot.types import Message
import random

TOKEN='682534527:AAGPugzizUFz93IHjXQHRqI_LMFgYEHvmuE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def command_handler(message):
    bot.reply_to(message, 'Я Великий Император Цезарь. Мой мозг оцифровали и перенесли в вирутальное пространство.')
    return

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Ave Caesar morituri te salutant' in message.text:
        bot.reply_to(message, 'Тут будет текст загадки')
    else:
        bot.reply_to(message, 'Как ты смешь так обращаться к Императору!')
    return


bot.polling()

