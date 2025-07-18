from telebot import TeleBot
from telebot.types import Message
TOKEN = '7260510231:AAHX2ek219CuKjI91IjExppFv9VvZA1AlKE'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Salom')

@bot.message_handler(commands=['help'])
def help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Adminga murojat: @abdurah1mov_04')


if __name__ == "__main__":
    bot.polling(none_stop=True)