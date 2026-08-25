import os
import telebot
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": message.text
                }
            ]
        }
        
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        res_json = response.json()
        
        reply_text = res_json["choices"][0]["message"]["content"]
        bot.reply_to(message, reply_text)
        
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

print("Бот запущен и готов к работе!")
bot.polling()
