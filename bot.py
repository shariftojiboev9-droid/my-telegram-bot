import os
import telebot

TOKEN = os.getenv('TG_TOKEN', '8840551930:AAGX6kaDLpS1APQN1bC6WYWgv18x1H4Jk')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я запущен на Render! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Бот запущен...")
bot.infinity_polling()
