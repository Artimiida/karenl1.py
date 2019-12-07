import telebot
import os

 
token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(token) 


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()