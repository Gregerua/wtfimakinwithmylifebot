import telebot

bot = telebot.TeleBot("5534683493:AAE8hJ1dZhWWzr8aIN5sd7ZV01PecYIFeDE")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")

    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")
