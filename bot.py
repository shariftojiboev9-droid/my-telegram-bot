import os
import telebot
import requests

TELEGRAM_BOT_TOKEN = "8840551930:AAGX6kaDLpS1APQN1bC6WYWgv6v18x1H4JkB"
GROQ_API_KEY = "gsk_TTxQJl07aisQtdWKz6wKWGdyb3FYL6zSxQpNCdguK9ws8E6A52WDGROQ"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        # Здесь продолжится твой код
        pass
    except Exception as e:
        bot.reply_to(message, "Ошибка!")

bot.infinity_polling()

