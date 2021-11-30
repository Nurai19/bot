import telebot

from telebot import types

welcome_text = 'Приветствую тебя любитель шахмат'

TOKEN = '2127680415:AAFk28N5fjEWHzP7foqiC_x1TJPDEJcet10'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or "привет" or "/start":
        bot.send_message(message.from_user.id, welcome_text)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Смотреть партии", url="followchess.com")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Новости", url="chess-news.ru")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Играть онлайн", url="chess.com")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Книги", url="whychess.ru")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Выбери что тебя интересует", reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
