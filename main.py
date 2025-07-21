from telebot import TeleBot
from telebot.types import Message
from button import menyu
import database

db = database.Database()

TOKEN = '7260510231:AAHX2ek219CuKjI91IjExppFv9VvZA1AlKE'

bot = TeleBot(TOKEN)

'''Start'''
@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Salom {message.from_user.full_name}.\nFilm janirini tanlang.', reply_markup=menyu())

'''Help'''
@bot.message_handler(commands=['help'])
def help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Adminga murojat: @abdurah1mov_04')

'''Menyu buttons'''
@bot.message_handler(func= lambda message: message.text in ['Fantastic', 'Komediya', 'Ramantika', 'Criminal'])
def reaction_menyu(message: Message):
    chat_id = message.chat.id
    if message.text == 'Fantastic':
        title = db.get_user(1)
        bot.send_message(chat_id, f'Film nomi: {title[0]}\nDescription: {title[1]}')
    elif message.text == 'Komediya':
        title = db.get_user(2)
        bot.send_message(chat_id, f'Film nomi: {title[0]}\nDescription: {title[1]}')
    elif message.text == 'Ramantika':
        title = db.get_user(3)
        bot.send_message(chat_id, f'Film nomi: {title[0]}\nDescription: {title[1]}')
    elif message.text == 'Criminal':
        title = db.get_user(4)
        bot.send_message(chat_id, f'Film nomi: {title[0]}\nDescription: {title[1]}')

if __name__ == "__main__":
    bot.polling(none_stop=True)